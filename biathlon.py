import random

players = []
HIT_CHANCE = 0.8


def generate_player():
    player = {
        "name": len(players) + 1,
        "hit_targets": [],
        "shots_fired": 0,
    }
    players.append(player)


targets = ["*", "*", "*", "*", "*"]


def reset_targets():
    global targets
    targets = ["*", "*", "*", "*", "*"]


def start_game():
    reset_targets()
    player_count = int(input("Enter the number of players: "))
    for _ in range(player_count):
        generate_player()

    print(len(players), "players have been added to the game.")

    # Let each player fire 5 shots
    for player in players:
        reset_targets()  # Reset targets for each player
        print(f"\nPlayer {player['name']}'s turn:")

        print("You got 5 shots!\n")
        for shot in range(5):
            print("\n1 2 3 4 5\n")
            print(" ".join(targets) + "\n")

            target = int(input(f"Shot nr {shot + 1} at: "))
            allowed_targets = [1, 2, 3, 4, 5]

            while target not in allowed_targets:
                print("Invalid target. Please choose a target between 1 and 5.")
                target = int(input(f"Shot nr {shot + 1} at: "))

            player["shots_fired"] += 1
            if targets[target - 1] == "*" and random.random() < HIT_CHANCE:
                player["hit_targets"].append(target)
                targets[target - 1] = "0"  # Mark the target as hit

                print("Hit!")

            else:
                print("Miss!")

    # Display results
    print("\nGame Over! Here are the results:")
    for player in players:
        print(
            f"Player {player['name']} hit {len(player['hit_targets'])} targets with {player['shots_fired']} shots fired."
        )


start_game()
