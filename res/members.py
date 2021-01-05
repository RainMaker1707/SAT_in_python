from res.candidates import Candidate


class Member:
    _inner_id = 0

    def __init__(self, add_to_list=True):
        self._id = Member._inner_id
        self._demands = []
        Member._inner_id += 1
        if add_to_list:
            MemberList.append(self)

    def __str__(self):
        """
        Make a dictionary string to be pretty readable
        :return: formatted string
        """
        return "{" + \
               "\n\tmember id: {0}\n\tdemands: {1}\n\tdemands size: {2}".format(self._id,
                                                                                self._demands,
                                                                                len(self._demands)) \
               + "\n}"

    # ----- getter and setter -----

    # getter
    def get(self):
        """
        :return: return a json/dictionary which contains the member information
        """
        return {'member id': self._id, 'demands': self._demands}

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


class MemberList:
    _inner = []

    def __str__(self):
        return MemberList._inner

    @staticmethod
    def pretty():
        """
        This function should transform the list object in string readable of item json like:
        {
            member id: int e[0, n] with n == nbr of members
            demands: [
                        {'candidate' : candidate object, 'accept': bool {True == accept or False == refuse}}
                    ]
            demands: size: int e[0, m] with m == len(demands)
        }
        :return: A pretty string human readable
        """
        ret_string = ""
        for member in MemberList._inner:
            ret_string += str(member) + ",\n"
        return ret_string.rstrip(',\n')

    @staticmethod
    def append(to_add: Member):
        """
        append a member on the tail of the MemberList
        this function is automatically called when a member is created
        :param to_add: a Member object to store
        """
        MemberList._inner.append(to_add)

    @staticmethod
    def insert(to_add: Member, pos: int):
        """
        Insert a member on the position specified in pos argument
        :param to_add: Member to insert in the list
        :param pos: the index where you want to store the member
        """
        MemberList._inner.insert(pos, to_add)

    @staticmethod
    def get():
        """
        :return: the list of member objects usable in program
        """
        return MemberList._inner

    @staticmethod
    def size():
        """
        :return: the size of the inner list or the number of members stored in the MemberList
        """
        return len(MemberList._inner)
