class Candidate:
    _nbr = 0

    def __init__(self, name=""):
        self._nbr = Candidate._nbr
        self.name = name
        Candidate._nbr += 1
        CandidateList.append(self)


class CandidateList:
    inner = []

    def __str__(self):
        return str(CandidateList.inner)

    @staticmethod
    def append(to_add: Candidate):
        CandidateList.inner.append(to_add)

    @staticmethod
    def insert(to_add: Candidate, pos: int):
        CandidateList.inner.insert(pos, to_add)

    @staticmethod
    def get():
        return CandidateList.inner
