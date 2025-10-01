import discord
from datenbanken.job_list import jobs
from datenbanken.jobs import set_job


class WorkView(discord.ui.View):
    def __init__(self, jobs):
        super().__init__(timeout=None)
        self.jobs = jobs

        for job in jobs:
            button = discord.ui.Button(
                label=job["name"], style=discord.ButtonStyle.primary
            )
            button.callback = self.make_callback(job)
            self.add_item(button)

    def make_callback(self, job):
        async def callback(interaction: discord.Interaction):
            user_id = interaction.user.id
            set_job(user_id, job)
            await interaction.response.send_message(
                f"Job **{job['name']}** gespeichert!", ephemeral=True
            )

        return callback
