import numpy as np

"""
0 -> rock
1 -> paper
2 -> scissors
"""
MOVES = {
    "A": 0,
    "B": 1,
    "C": 2,
    "X": 0,
    "Y": 1,
    "Z": 2,
}

SHAPE_SCORES = {0: 1, 1: 2, 2: 3}

"""
win is (0, 1), (1, 2), (2, 0) = 2
all (i, i) are draws = 1
loss is (1, 0), (2, 1), (0, 2) = 0

"""
OUTCOMES = np.identity(3)
OUTCOMES[0, 1] = OUTCOMES[1, 2] = OUTCOMES[2, 0] = 2

OUTCOME_SCORES = {0: 0, 1: 3, 2: 6}


def parse_input():

    # with open("input_day2.txt") as f:
    with open("input_day2.txt") as f:
        lines = f.readlines()

    opp_moves = []
    my_moves = []
    for line in lines:
        opp_move, my_move = line.strip().split()
        opp_moves.append(opp_move)
        my_moves.append(my_move)

    return opp_moves, my_moves


def play_game(opp_moves, my_moves):

    score = 0
    for opp_move_code, my_move_code in zip(opp_moves, my_moves):

        round_score = 0

        opp_move, my_move = MOVES[opp_move_code], MOVES[my_move_code]
        round_score += SHAPE_SCORES[my_move]

        # print(round_score)

        outcome = OUTCOMES[opp_move, my_move]
        round_score += OUTCOME_SCORES[outcome]
        # print(f"outcome: {outcome}")

        print(round_score)
        score += round_score

    return score


def main():
    opp_moves, my_moves = parse_input()
    score = play_game(opp_moves, my_moves)
    print(score)


if __name__ == "__main__":
    main()
