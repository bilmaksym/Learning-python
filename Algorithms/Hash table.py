# Here I will show how to work with hash tables

# book = dict()
#
# book["apple"] = 0.67
# book["milk"] = 1.49
# book["avocado"] = 1.49
#

phone_book = dict()
phone_book2 = {} # The same as phone_book = dict()

phone_book["Jenny"] = 380994312652
phone_book["emergency"] = 102

print(phone_book["Jenny"])

# Lets create simulator of election
voted = {}
#value = voted.get("tom")

def check_for_vote(name):
    """
    This function check if you already voted or not
    :param name:
    :return:
    """
    if voted.get(name):
        print("Already voted, kick them out")
    else:
        voted[name] = True
        print("Let tem vote!")
    pass