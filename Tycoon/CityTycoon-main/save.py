import json

def load_game(filename):
    with open(filename) as f:
        player1 = json.load(f)
    return player1


def save_game(filename, player1, player2):
    player1 = dict(player1)
    with open(filename, 'w') as f:
        json.dump([player1], f)

        