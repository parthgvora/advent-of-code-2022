"""
0 -> rock
1 -> paper
2 -> scissors
"""
MOVES = {
    "A": 0,
    "B": 1,
    "C": 2,
}

SHAPE_SCORES = {0: 1, 1: 2, 2: 3}

"""
Outcome matrix

X: opp move

Y: outcome
0 -> loss
1 -> draw
2 -> win

store: what move to make
(0, 0) -> 2
(0, 1) -> 0
(0, 2) -> 1
(1, 0) -> 0
(1, 1) -> 1
(1, 2) -> 2
(2, 0) -> 1
(2, 1) -> 2
(2, 2) -> 0

Basically
move to make ->
lose: (opp + 2) % 3
win: (opp + 1) % 3
draw: opp

=> move to make = (opp + (outcome + 2) % 3) % 3

"""
OUTCOMES = {
    "X": 0,  # loss
    "Y": 1,  # draw
    "Z": 2,  # win
}

OUTCOME_SCORES = {0: 0, 1: 3, 2: 6}


def parse_input():

    with open("input_day2.txt") as f:
        lines = f.readlines()

    opp_moves = []
    outcomes = []
    for line in lines:
        opp_move, outcome = line.strip().split()
        opp_moves.append(opp_move)
        outcomes.append(outcome)

    return opp_moves, outcomes


def play_game(opp_moves, outcomes):

    score = 0
    for opp_move_code, outcome_code in zip(opp_moves, outcomes):

        round_score = 0
        opp_move = MOVES[opp_move_code]
        outcome = OUTCOMES[outcome_code]
        round_score += OUTCOME_SCORES[outcome]

        my_move = (opp_move + (outcome + 2) % 3) % 3
        round_score += SHAPE_SCORES[my_move]

        score += round_score

    return score


def main():
    opp_moves, outcomes = parse_input()
    score = play_game(opp_moves, outcomes)
    print(score)


if __name__ == "__main__":
    main()
