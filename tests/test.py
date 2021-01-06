from res.functions import *
from random import randint
import unittest


class TestSetupFunction(unittest.TestCase):

    def test_size(self):
        asrt = randint(10, 100)
        for i in range(asrt):
            if not MemberList.is_empty():
                MemberList.empty_list()
            if not CandidateList.is_empty():
                CandidateList.empty_list()
            member_nbr = randint(0, 100)
            candidate_nbr = randint(member_nbr, 1000)
            setup(member_nbr, candidate_nbr)
            self.assertEqual(MemberList.size(), member_nbr)
            self.assertEqual(CandidateList.size(), candidate_nbr)


if __name__ == '__main__':
    unittest.main(verbosity=2)
