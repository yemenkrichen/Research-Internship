
import math

# One simulation step = 1 hour
TIME_STEP_SECONDS = 3600

# Assumption from your model
RESTRAINT_TIME = 12

TRANSITION_RATES = {

    "S->D": 9.24527898496082E-07,
    "S->I": 1.0863202807329E-05,
    "S->N": 1.23655606423851E-05,
    "S->P": 3.69811159398433E-06,

    "D->I": 1.62666692693338E-06,
    "D->P": 1.62666692693338E-06,

    "N->D": 5.7488953784975E-07,
    "N->I": 3.4493372270985E-07,
    "N->P": 1.8396465211192E-06,

    "P->D": 2.85040937579455E-07,
    "P->I": 5.7008187515891E-07,
    "P->N": 5.7008187515891E-07
}

TRANSITION_PROBABILITIES = {}

for transition, rate in TRANSITION_RATES.items():

    TRANSITION_PROBABILITIES[transition] = (
        1 - math.exp(-rate * TIME_STEP_SECONDS)
    )
