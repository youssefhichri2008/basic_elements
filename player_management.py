"""
========== PLAYER MANAGEMENT ==========

1. Add a player
2. Display players
3. Search for a player
4. Update a player
5. Delete a player
6. Display the top scorer
7. Calculate the average number of goals
8. Quit
"""

# List of players
players = []


def add_player():
    # Ask for the player's information
    name = input("Player name: ")
    age = int(input("Player age: "))
    position = input("Player position: ")
    goals = int(input("Number of goals: "))
    matches = int(input("Number of matches: "))

    # Create a dictionary containing the player's information
    player = {
        "name": name,
        "age": age,
        "position": position,
        "goals": goals,
        "matches": matches
    }

    # Add the player to the list
    players.append(player)
    print("Player added!")


def display_players():
    # Check if there are no players
    if len(players) == 0:
        print("No players.")

    else:
        # Display each player's information
        for player in players:
            print("--------------------")
            print("Name:", player["name"])
            print("Age:", player["age"])
            print("Position:", player["position"])
            print("Goals:", player["goals"])
            print("Matches:", player["matches"])


def search_player():
    # Ask for the name of the player to search for
    search_name = input("Player name to search for: ")

    # Search for the player in the list
    for player in players:
        if player["name"] == search_name:
            print("Name:", player["name"])
            print("Age:", player["age"])
            print("Position:", player["position"])
            print("Goals:", player["goals"])
            print("Matches:", player["matches"])
            return

    # Display a message if the player is not found
    print("Player not found.")


def update_player():
    # Ask for the name of the player to update
    search_name = input("Player name to update: ")

    # Search for the player
    for player in players:
        if player["name"] == search_name:
            # Update the player's information
            player["age"] = int(input("New age: "))
            player["position"] = input("New position: ")
            player["goals"] = int(input("New number of goals: "))
            player["matches"] = int(input("New number of matches: "))

            print("Player updated!")
            return

    # Display a message if the player is not found
    print("Player not found.")


def delete_player():
    # Ask for the name of the player to delete
    search_name = input("Player name to delete: ")

    # Search for the player
    for player in players:
        if player["name"] == search_name:
            # Remove the player from the list
            players.remove(player)
            print("Player deleted!")
            return

    # Display a message if the player is not found
    print("Player not found.")


def top_scorer():
    # Check if there are no players
    if len(players) == 0:
        print("No players.")
        return

    # Assume the first player is the top scorer
    best_player = players[0]

    # Find the player with the most goals
    for player in players:
        if player["goals"] > best_player["goals"]:
            best_player = player

    # Display the top scorer
    print("Top scorer:", best_player["name"])
    print("Number of goals:", best_player["goals"])


def average_goals():
    # Check if there are no players
    if len(players) == 0:
        print("No players.")
        return

    # Calculate the total number of goals
    total = 0

    for player in players:
        total = total + player["goals"]

    # Calculate and display the average number of goals
    average = total / len(players)

    print("Average number of goals:", average)
