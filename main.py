from res.candidates import CandidateList, Candidate
from res.members import Member
from random import randint, getrandbits


def setup(member_nbr: int, candidate_nbr: int):
    """
    This function will make a list of potential candidates and a list of member
    Each member has a random list of random demand
    :non-param complexity: T(n^2)
    :param member_nbr: number of member already registered in the 'club'
    :param candidate_nbr: number of candidates who wish join the 'club'
    :return: the list of member and each one list of demands
    """
    for x in range(candidate_nbr):
        Candidate()
    members_list = []
    for y in range(member_nbr):
        this = Member()
        for i in range(randint(1, CandidateList.size())):
            temp = CandidateList.get()[randint(0, CandidateList.size() - 1)]
            accept = bool(getrandbits(1))
            # Check to avoid to have twice same demands or paradoxical demand
            # like demand to accept one candidate and  demand refuse this same one
            while {'candidate': temp, 'accept': (True or False)} in this.get_demands():
                temp = CandidateList.get()[randint(0, CandidateList.size() - 1)]
            this.add_demand(temp, accept)
        members_list.append(this)
    return members_list


if __name__ == "__main__":
    print("Run as main program")

    members = setup(10, 100)

    print("Candidate List size: " + str(CandidateList.size()))
    print("Member List: ")
    for member in members:
        print(str(member))

    # to remove one candidate from the demand list of one member
    # members[-1].remove_demand(members[-1].get_demands()[0].get('candidate'))
