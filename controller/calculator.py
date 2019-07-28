# Python imports
import math

# Flask imports

# Project imports
from model.announcement import Announcement

__Author__ = "Amir Mohammad"


def convert_rooms_to_number(number):
    if number == 'یک':
        return 1
    elif number == 'دو':
            return 2
    elif number == 'سه':
            return 3
    elif number == 'چهار':
            return 4
    elif number == 'پنج':
            return 5
    else:
        return 0

def convert_deposit_amount(number):
    pass