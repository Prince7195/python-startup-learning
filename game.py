from random import randint

game_running = True
game_result = []

def calc_monstor_attack():
    return randint(monstor["attack_min"], monstor["attack_max"])

def game_end(winner_name):
    print(f"{winner_name} won the Game")

while game_running == True:
    counter = 0
    new_round = True
    player = { "name": "Vijay", "attack": 13, "heal": 16, "health": 100, "rounds": counter }
    monstor = { "name": "Sekhar", "attack_min": 10, "attack_max": 20, "health": 100, "rounds": counter }

    print("---" * 7)
    print("Enter Player Name:")
    player["name"] = input()

    print("Player " + player["name"] + " has " + str(player["health"]) + " health")
    print("Monstor " + monstor["name"] + " has " + str(monstor["health"]) + " health")

    while new_round == True:
        counter = counter + 1
        player_won = False
        monstor_won = False

        print("---" * 7)
        print("Please select Action:")
        print("1) Attack")
        print("2) Heal")
        print("3) Exit Game")
        print("4) Show Result")

        player_choice = input()

        if player_choice == "1":
            monstor["health"] = monstor["health"] - player["attack"]
            if monstor["health"] <= 0:
                player_won = True
            else:
                monstor_attack = randint(monstor["attack_min"], monstor["attack_max"])
                player["health"] = player["health"] - calc_monstor_attack()
                if player["health"] <= 0:
                    monstor_won = True

        elif player_choice == "2":
            monstor_attack = randint(monstor["attack_min"], monstor["attack_max"])
            player["health"] = player["health"] + player["heal"]
            player["health"] = player["health"] - calc_monstor_attack()
            if player["health"] <= 0:
                    monstor_won = True

        elif player_choice == "3":
            new_round = False
            game_running = False

        elif player_choice == "4":
            for result in game_result:
                print(game_result)

        else:
            print("Invalid Input")
            
        if player_won == False and monstor_won == False:
            print("Player " + player["name"] + " has " + str(player["health"]) + " health left")
            print("Monstor " + monstor["name"] + " has " + str(monstor["health"]) + " health left")
        elif player_won:
            game_end(player["name"])
            round_result = { "name": player["name"], "health": player["health"] }
            game_result.append(round_result)
            new_round = False
        elif monstor_won:
            game_end(monstor["name"])
            round_result = { "name": monstor["name"], "health": monstor["health"] }
            game_result.append(round_result)
            new_round = False
