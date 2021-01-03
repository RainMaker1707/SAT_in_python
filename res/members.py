from res.candidates import Candidate


class Member:
    _inner_id = 0

    def __init__(self):
        self._id = Member._inner_id
        self._demands = []
        Member._inner_id += 1

    def __str__(self):
        """
        Make a dictionary string to be pretty readable
        :return: formatted string
        """
        return "{" + \
               "\n\tid: {0}\n\tdemands: {1}\n\tdemands size: {2}".format(self._id, self._demands, len(self._demands)) \
               + "\n}"

    # ----- getter and setter -----

    # getter
    def get(self):
        """
        :return: return a json/dictionary which contains the member information
        """
        return {'id': self._id, 'demands': self._demands}

    def get_id(self):
        """
        :return: return the member's id
        """
        return self._id

    def get_demands(self):
        """
        :return: the demands list
        """
        return self._demands

    def demands_size(self):
        """
        :return: the size of the demands list
        """
        return len(self._demands)

    # setter
    def add_demand(self, to_add: Candidate, accept: bool = True):
        """
        Append a demand in the demands list
        :param to_add: Candidate to add
        :param accept: True if member want to accept him False either
        :return: None
        """
        self._demands.append({'candidate': to_add, 'accept': accept})

    def remove_demand(self, to_remove: Candidate):
        """
        Remove the json/dictionary which contain the Candidate passed as argument
        from the demands list
        :param to_remove: Candidate to remove
        :return: None
        """
        self._demands.remove({'candidate': to_remove, 'accept': (True or False)})
