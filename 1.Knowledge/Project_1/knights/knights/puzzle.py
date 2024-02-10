from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # Base Structure of Game.
    Not(And(AKnight, AKnave)),  # cannot be knight and knave at the same time
    Or(AKnight, AKnave),        # Has to be either a Knight or a Knave
    
    # Character Statements
    # A says "I am both a knight and a knave."
    Implication(AKnight, And(AKnight, AKnave)), # If True
    Implication(AKnave, Not(And(AKnight, AKnave))) # If False
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # Base Structure of Game.
    Not(And(AKnight, AKnave)),  # cannot be knight and knave at the same time
    Or(AKnight, AKnave),        # Has to be either a Knight or a Knave

    Not(And(BKnight, BKnave)),  # cannot be knight and knave at the same time
    Or(BKnight, BKnave),        # Has to be either a Knight or a Knave

    # Character Statements
    # A says "We are both knaves."
    Implication(AKnight, And(AKnave, BKnave)),
    Implication(AKnave, Not(And(AKnave, BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # Base Structure of Game.
    Not(And(AKnight, AKnave)),  # cannot be knight and knave at the same time
    Or(AKnight, AKnave),        # will be Knight or Knave

    Not(And(BKnight, BKnave)),  # cannot be knight and knave at the same time
    Or(BKnight, BKnave),        # will be Knight or Knave

    # Character Statements
    # A says "We are the same kind."  
    Implication(AKnight, And(AKnight, BKnight)), # If True
    Implication(AKnave, Not(And(AKnave, BKnave))), # If False
    
    # Character Statements
    # B says "We are of different kinds."
    Implication(BKnight, And(BKnight, AKnave)), # If True
    Implication(BKnave, Not(And(BKnave, AKnight))) # If False
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # Base Structure of Game.
    Not(And(AKnight, AKnave)),  # A cannot be knight and knave at the same time
    Or(AKnight, AKnave),        # A will be Knight or Knave

    Not(And(BKnight, BKnave)),  # B cannot be knight and knave at the same time
    Or(BKnight, BKnave),        # B will be Knight or Knave

    Not(And(CKnight, CKnave)),  # C cannot be knight and knave at the same time
    Or(CKnight, CKnave),        # C will be Knight or Knave
    
    # Character Statements
    # A says either "I am a knight." or "I am a knave.", but you don't know which.
    Or(
        # "I am a knight."
        And(
            Implication(AKnight, AKnight),
            Implication(AKnave, Not(AKnight))
        ), 
        
        # "I am a knave."
        And(
            Implication(AKnight, AKnave),
            Implication(AKnave, Not(AKnave))
        )
    ), # If True

    Not(And(
        # "I am a knight."
        And(
            Implication(AKnight, AKnight),
            Implication(AKnave, Not(AKnight))
        ),
        
        # "I am a knave."
        And(
            Implication(AKnight, AKnave),
            Implication(AKnave, Not(AKnave))
        )
    )), # If False
    
    # Character Statements
    # B says "A said 'I am a knave'."
    Implication(BKnight, And(
        Implication(AKnight, AKnave),
        Implication(AKnave, Not(AKnave))
    )), # If True

    Implication(BKnave, Not(And(
        Implication(AKnight, AKnave),
        Implication(AKnave, Not(AKnave))
    ))), # If False
    
    # Character Statements
    # B says "C is a knave."
    Implication(BKnight, CKnave), # If True
    Implication(BKnave, Not(CKnave)), # If False
    
    # Character Statements
    # C says "A is a knight."
    Implication(CKnight, AKnight), # If True
    Implication(CKnave, Not(AKnight)) # If False
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
