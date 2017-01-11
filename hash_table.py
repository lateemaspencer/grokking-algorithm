#create an empty dictionary to store voters who voted
voted = {}

def check_voter(name):
    if voted.get(name):
        print("kick them out!")
    else:
        voted[name] = True
        print("let them vote!")

check_voter("Lateema")
check_voter("Lateema")