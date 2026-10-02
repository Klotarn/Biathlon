import random

players = []
HIT_CHANCE = 0.8
INTRO_TEXT = """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
               Biathlon

          a hit or miss game
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""


# Function to get a player name from the user
def get_player_name(naming_offset):
    name = input("Enter player name: ").strip()

    if not name:
        name = f"{len(players) + naming_offset}"
        print(f'No name entered. Assigning default name "{name}".')
        naming_offset += 1

    return name, naming_offset


def generate_player():
    name, offset = get_player_name(1)

    # If name is not unique, try again until a unique name is provided
    while any(player["name"] == name for player in players):
        print(f"Name '{name}' is already taken. Please choose a different name.")
        name, offset = get_player_name(offset)

    player = {
        "name": name,
        "hit_targets": [],
    }
    players.append(player)


targets = ["*", "*", "*", "*", "*"]


def reset_targets():
    global targets
    targets = ["*", "*", "*", "*", "*"]


def print_targets():
    print("\n1 2 3 4 5\n")
    print(" ".join(targets) + "\n")


def start_game():
    print(INTRO_TEXT)

    reset_targets()
    player_count = int(input("Enter the number of players: "))
    for _ in range(player_count):
        generate_player()

    print(len(players), "players have been added to the game.")

    for player in players:
        print(f"Player {player['name']} is ready to play!")

    # Let each player fire 5 shots
    for i, player in enumerate(players):
        reset_targets()  # Reset targets for each player
        print(f"\nPlayer {player['name']}'s turn:")

        print("You got 5 shots!\n")
        for shot in range(5):
            print_targets()

            target_str = input(f"Shot nr {shot + 1} at: ").strip()
            allowed_targets = [1, 2, 3, 4, 5]

            # Make sure the input is valid and within the allowed range
            while not target_str.isdigit() or int(target_str) not in allowed_targets:
                print(
                    "\n!!! Invalid target. Please choose a target between 1 and 5. !!!\n"
                )
                target_str = input(f"Shot nr {shot + 1} at: ").strip()

            target = int(target_str)

            if targets[target - 1] == "*" and random.random() < HIT_CHANCE:
                player["hit_targets"].append(target)
                targets[target - 1] = "0"  # Mark the target as hit

                print("Hit!")

            else:
                print("Miss!")

        # Represent how many targets are hit after each player is finnished
        print(f"\nPlayer {player['name']} hit {len(player['hit_targets'])} targets.")

        print_targets()  # Show the final state of targets after the player's turn

        # Display different messages based on whether it's the last player or not
        if i < len(players) - 1:
            input("Press Enter to continue to the next player...")
        else:
            input("Press Enter to see the results...")

    # Display results
    # Determine if there is a winner or if it's a multi-way tie
    if len(players) > 1:
        max_hits = max(len(player["hit_targets"]) for player in players)
        winners = [
            player for player in players if len(player["hit_targets"]) == max_hits
        ]

        if len(winners) == 1:
            print(
                f"\n-------- Game Over --------\n\nPlayer {winners[0]['name']} is the winner with {max_hits} hits!"
            )
        else:
            print(
                "\n-------- Game Over --------\n\nIt's a tie between the following players:"
            )
            for winner in winners:
                print(f"Player {winner['name']} with {max_hits} hits.")

    # Display the results for all players
    print("\n------ Final Results ------\n")
    sorted_players = sorted(players, key=lambda x: len(x["hit_targets"]), reverse=True)
    for player in sorted_players:
        print(f"Player {player['name']} hit {len(player['hit_targets'])} targets.")
    print()


start_game()
