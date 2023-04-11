from stack import Stack
import pytest


class TestStack:
    @pytest.fixture
    def StackA(self):
        StackA = Stack(3)
        return StackA

    @pytest.fixture
    def StackB(self):
        StackB = Stack(3)
        StackB.push(123)
        StackB.push(456)
        StackB.push(789)
        return StackB

    def test_is_empty(self, StackA, StackB):
        assert StackA.is_empty()
        assert not StackB.is_empty()
    
    def test_is_full(self, StackA, StackB):
        assert not StackA.is_full()
        assert StackB.is_full()
    
    def test_push(self, StackA, StackB):
        StackA.push(1)
        assert StackA.items[0] == 1
        assert StackA.n == 1
        pytest.raises(ValueError, lambda: StackB.push(0))
        StackA.push(2)
        assert StackA.pop() == 2
    
    def test_pop(self, StackA, StackB):
        pytest.raises(ValueError, lambda: StackA.pop())
        assert StackB.pop() == 789
        assert StackB.n == 2


if __name__ == "__main__":
    pytest.main()
