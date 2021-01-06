from res.members import *
from res.candidates import *
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
