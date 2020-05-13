def switch(case):
    if case == 1:
        return 'monday'.upper()
    elif case == 2:
        return 'tuesday'.upper()
    elif case == 3:
        return 'wednesday'.upper()
    elif case == 4:
        return 'thursday'.upper()
    elif case == 5:
        return 'friday'.upper()
    elif case == 6:
        return 'saturday'.upper()
    elif case == 7:
        return 'sunday'.upper()
    else:
        return 'not a valid day of week'.upper()


print(switch(1))
print(switch(4))
print(switch(10))


def switch(case):
    day_of_week = {1: 'monday'.upper(),
                   2: 'tuesday'.upper(),
                   3: 'wednesday'.upper(),
                   4: 'thursday'.upper(),
                   5: 'friday'.upper(),
                   6: 'saturday'.upper(),
                   7: 'sunday'.upper(),
                   'default': 'not a valid day of week'.upper(),
                   }
    return day_of_week.get(case, day_of_week['default'])


print(switch(1))
print(switch(4))
print(switch(10))
