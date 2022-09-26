
def does_weapon_win(weapon1,weapon2):
    if weapon1 == "rock":
        if weapon2 == "paper":
            return False
        elif weapon2 == "scissors":
            return True
        elif weapon2 == "rock":
            return False
    if weapon1 == "paper":
        if weapon2 == "paper":
            return False
        elif weapon2 == "scissors":
            return False
        elif weapon2 == "rock":
            return True
    if weapon1 == "scissors":
        if weapon2 == "paper":
            return True
        elif weapon2 == "scissors":
            return False
        elif weapon2 == "rock":
            return False


does_win = does_weapon_win("scissors","rock")
print(does_win)