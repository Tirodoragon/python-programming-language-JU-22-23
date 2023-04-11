from SingleList import Node, SingleList
import pytest


class TestSingleList:
    @pytest.fixture(scope="class")
    def SingleListA(self):
        SingleListA = SingleList()
        return SingleListA

    @pytest.fixture(scope="class")
    def SingleListB(self):
        SingleListB = SingleList()
        SingleListB.insert_head(Node(12))
        SingleListB.insert_tail(Node(242))
        SingleListB.insert_tail(Node(123))
        return SingleListB

    @pytest.fixture(scope="class")
    def SingleListC(self):
        SingleListC = SingleList()
        SingleListC.insert_head(Node(124))
        SingleListC.insert_tail(Node(125))
        return SingleListC

    @pytest.fixture(scope="class")
    def SingleListD(self):
        SingleListD = SingleList()
        SingleListD.insert_head(Node(341))
        SingleListD.insert_tail(Node(324))
        return SingleListD

    @pytest.fixture(scope="class")
    def SingleListE(self):
        SingleListE = SingleList()
        SingleListE.insert_head(Node(129))
        return SingleListE

    @pytest.fixture(scope="class")
    def SingleListF(self):
        SingleListF = SingleList()
        return SingleListF

    def test_is_empty(self, SingleListA, SingleListB):
        assert SingleListA.is_empty() == True
        assert SingleListB.is_empty() == False

    def test_count(self, SingleListA, SingleListB):
        assert SingleListA.count() == 0
        assert SingleListB.count() == 3

    def test_insert_head(self, SingleListA, SingleListB):
        SingleListA.insert_head(Node(145))
        assert SingleListA.head.data == 145
        SingleListB.insert_head(Node(341))
        assert SingleListB.head.data == 341

    def test_insert_tail(self, SingleListA, SingleListB):
        SingleListA.insert_tail(Node(352))
        assert SingleListA.tail.data == 352
        SingleListB.insert_tail(Node(523))
        assert SingleListB.tail.data == 523

    def test_remove_head(self, SingleListA, SingleListB, SingleListF):
        assert SingleListA.remove_head().data == 145
        assert SingleListB.remove_head().data == 341
        pytest.raises(ValueError, lambda: SingleListF.remove_head())

    def test_remove_tail(self, SingleListA, SingleListB, SingleListF):
        assert SingleListA.remove_tail().data == 352
        assert SingleListB.remove_tail().data == 523
        pytest.raises(ValueError, lambda: SingleListF.remove_tail())

    def test_join(self, SingleListA, SingleListB, SingleListC, SingleListD, SingleListE):
        SingleListA.join(SingleListB)
        assert SingleListA.tail.data == 123
        assert SingleListB.is_empty() == True
        SingleListC.join(SingleListD)
        assert SingleListC.tail.data == 324
        assert SingleListD.is_empty() == True
        pytest.raises(ValueError, lambda: SingleListE.join(1))

    def test_clear(self, SingleListA, SingleListC):
        SingleListA.clear()
        assert SingleListA.is_empty() == True
        SingleListC.clear()
        assert SingleListC.is_empty() == True


if __name__ == "__main__":
    pytest.main()
