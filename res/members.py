from res.candidates import Candidate


class Member:
    def __init__(self, nbr):
        self._nbr = nbr
        self._demands = []

    # ----- getter and setter -----

    # getter
    def get_id(self):
        return self._nbr

    def get_demands(self):
        return self._demands

    # setter
    def add_demand(self, to_add: Candidate):
        self._demands.append(to_add)

    def remove_demand(self, to_remove: Candidate):
        self._demands.remove(to_remove)
