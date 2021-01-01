from res.candidates import CandidateList, Candidate
from res.members import Member


def setup(member_nbr: int, candidate_nbr: int):
    for x in range(candidate_nbr):
        Candidate()
    print(len(CandidateList.get()))


if __name__ == "__main__":
    print("Run as main program")
    setup(10, 10)
