# implement commonly used functions here

import random


# generate and return a unique and random string
# other expectation:
# - at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter
# - it must be unique in the list
#
# @table: list of lists
# @generated: string - randomly generated string (unique in the @table)
def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation.

    Args:
        table: list containing keys. Generated string should be different then all of them

    Returns:
        Random and unique string
    """

    generated = ''

    for times in range(0, 2):
        chosen_number = random.randint(97, 122)
        generated += chr(chosen_number)
        chosen_number = random.randint(65, 90)
        generated += chr(chosen_number)
        chosen_number = random.randint(58, 64)
        generated += chr(chosen_number)
        chosen_number = random.randint(0, 9)
        generated += str(chosen_number)
    generated = ''.join(random.sample(generated, len(generated)))

    return generated
