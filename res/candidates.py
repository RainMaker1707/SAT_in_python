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
        """
        transform the string reference of the list in a list of string object's reference to
        each candidate stored in it
        :return: a string (list format) of candidate references
        """
        return str(CandidateList._inner)

    @staticmethod
    def append(to_add: Candidate):
        """
        append a candidate on the tail of the CandidateList
        this function is automatically called when a candidate is created
        :param to_add: a Candidate object to store
        """
        CandidateList._inner.append(to_add)

    @staticmethod
    def insert(to_add: Candidate, pos: int):
        """
        Insert a candidate on the position specified in pos argument
        :param to_add: Candidate to insert in the list
        :param pos: the index where you want to store the candidate
        """
        CandidateList._inner.insert(pos, to_add)

    @staticmethod
    def get():
        """
        :return: the list of candidate objects usable in program
        """
        return CandidateList._inner

    @staticmethod
    def size():
        """
        :return: the size of the inner list or the number of candidates stored in the CandidateList
        """
        return len(CandidateList._inner)
