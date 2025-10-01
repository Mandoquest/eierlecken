import discord 
import random
import json



async def choose_impostor(players):
    print("Choosing impostor from players")
    try:
        with open("Impostor_wörter.json", "r") as file:
            data = json.load(file)
        print(f"Loaded words: {data}")  # Added line to print loaded words
    except Exception as e:
        print(f"Error loading words: {e}")
        return

    word = random.choice(data)    
    impostor = random.choice(players)

    print(f"Players to DM: {players}")  # Added line to print players

    for player in players:
        print(f"DMing: {player}")
        try:
            if player == impostor:
                await player.send("You are the impostor! You have to guess the word")
            else:
                await player.send(f"The word is {word}")
                print(word)
        except Exception as e:
            print(f"Failed to DM {player}: {e}")