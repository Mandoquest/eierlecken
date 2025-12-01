import discord
from io import BytesIO
import aiohttp
from datenbanken.datenbanken_test import ändere_guthaben
from funktionen.inv_interface import get_inventory, add_item, remove_item
from datenbanken.aktive_Spiele import aktive_spiele
from funktionen.utils import kombiniere_kartenbilder
from funktionen.utils import Zahlen_verkleineren


class BlackjackView(discord.ui.View):
    def __init__(self, user_id, deck_id, player_cards, dealer_cards, einsatz, spiel_id):
        super().__init__(timeout=None)
        self.user_id = user_id
        self.deck_id = deck_id
        self.player_cards = player_cards
        self.dealer_cards = dealer_cards
        self.einsatz = einsatz
        self.spiel_id = spiel_id

    async def button_lock_check(self, interaction):
        spiel = aktive_spiele.get(self.spiel_id)
        if not spiel:
            await interaction.response.send_message(
                "Spiel existiert nicht mehr.", ephemeral=True
            )
            return False
        if spiel.get("aktion_laeuft", False):
            await interaction.response.send_message(
                "Bitte warten, Aktion läuft noch.", ephemeral=True
            )
            return False
        spiel["aktion_laeuft"] = True
        return True

    async def button_unlock(self):
        spiel = aktive_spiele.get(self.spiel_id)
        if spiel:
            spiel["aktion_laeuft"] = False

    async def ziehe_karte(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"https://deckofcardsapi.com/api/deck/{self.deck_id}/draw/?count=1"
            ) as resp:
                return (await resp.json())["cards"][0]

    def punkte(self, karten):
        punkte, asse = 0, 0
        for karte in karten:
            v = karte["value"]
            if v in ["KING", "QUEEN", "JACK"]:
                punkte += 10
            elif v == "ACE":
                punkte += 11
                asse += 1
            else:
                punkte += int(v)
        while punkte > 21 and asse:
            punkte -= 10
            asse -= 1
        return punkte

    def kartenbilder(self, karten):
        return [k["image"] for k in karten]

    async def sende_embed(self, interaction, titel, text, karten, farbe):
        bild = kombiniere_kartenbilder(self.kartenbilder(karten))
        byte = BytesIO()
        bild.save(byte, format="PNG")
        byte.seek(0)
        file = discord.File(byte, filename="hand.png")
        embed = discord.Embed(title=titel, description=text, color=farbe)
        embed.set_image(url="attachment://hand.png")
        Guthaben = get_inventory(self.user_id, "MandoCoins")
        Konto = Zahlen_verkleineren(Guthaben)
        embed.set_footer(text=f"Balance: {Konto} Coins")
        await interaction.edit_original_response(
            embed=embed, attachments=[file], view=self
        )

    @discord.ui.button(label="Hit", style=discord.ButtonStyle.green)
    async def hit(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.id != self.user_id:
            await interaction.response.send_message("Not your game!", ephemeral=True)
            return

        if not await self.button_lock_check(interaction):
            return

        button.disabled = True
        await interaction.response.edit_message(view=self)
        karte = await self.ziehe_karte()
        self.player_cards.append(karte)

        if self.punkte(self.player_cards) > 21:
            self.clear_items()
            await self.sende_embed(
                interaction,
                "💥 BUST!",
                "You Lost.",
                self.player_cards,
                discord.Color.red(),
            )
        else:
            button.disabled = False
            await self.sende_embed(
                interaction,
                "♠️ Your Cards",
                f"Points: {self.punkte(self.player_cards)}",
                self.player_cards,
                discord.Color.green(),
            )
            await interaction.edit_original_response(view=self)

        await self.button_unlock()

    @discord.ui.button(label="Stand", style=discord.ButtonStyle.red)
    async def stand(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.id != self.user_id:
            await interaction.response.send_message("Not your game!", ephemeral=True)
            return

        if not await self.button_lock_check(interaction):
            return
        button.disabled = True
        await interaction.response.edit_message(view=self)

        self.clear_items()
        while self.punkte(self.dealer_cards) < 17:
            karte = await self.ziehe_karte()
            self.dealer_cards.append(karte)

        sp, dp = self.punkte(self.player_cards), self.punkte(self.dealer_cards)
        if dp > 21 or sp > dp:
            Einsatz = self.einsatz * 2
            add_item(self.user_id, "MandoCoins", Einsatz)
            titel, farbe = "✅ You win!", discord.Color.green()
            text = f"You: {sp} | Dealer: {dp}"
        elif sp == dp:
            add_item(self.user_id, "MandoCoins", self.einsatz)
            titel, farbe = "➖ Tie", discord.Color.greyple()
            text = f"Both: {sp} Points"
        else:
            titel, farbe = "❌ Lost", discord.Color.red()
            text = f"You: {sp} | Dealer: {dp}"

        await self.sende_embed(
            interaction,
            titel,
            f"{text}\n\nYour cards: {', '.join([c['value'] for c in self.player_cards])}\nDealer cards: {', '.join([c['value'] for c in self.dealer_cards])}",
            self.dealer_cards,
            farbe,
        )
        await self.button_unlock()
