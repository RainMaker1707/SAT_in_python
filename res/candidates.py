class Candidate:
    _inner_id = 0

    def __init__(self, name=""):
        self._id = Candidate._inner_id
        self.name = name
        Candidate._inner_id += 1
        CandidateList.append(self)


class CandidateList:
    _inner = []

    def __str__(self):
        return str(CandidateList._inner)

    @staticmethod
    def append(to_add: Candidate):
        CandidateList._inner.append(to_add)

    @staticmethod
    def insert(to_add: Candidate, pos: int):
        CandidateList._inner.insert(pos, to_add)

    @staticmethod
    def get():
        return CandidateList._inner

    @staticmethod
    def size():
        return len(CandidateList._inner)
