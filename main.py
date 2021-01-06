from res.functions import *


if __name__ == "__main__":
    print("Run as main program")
    setup(10, 100)
    print(MemberList.pretty())

    # to remove one candidate from the demand list of one member
    # members[-1].remove_demand(members[-1].get_demands()[0].get('candidate'))
