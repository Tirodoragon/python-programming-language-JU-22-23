from randomqueue import RandomQueue
import pytest


class TestRandomQueue:
    @pytest.fixture
    def RandomQueueA(self):
        RandomQueueA = RandomQueue(3)
        return RandomQueueA

    @pytest.fixture
    def RandomQueueB(self):
        RandomQueueB = RandomQueue(3)
        RandomQueueB.insert(123)
        RandomQueueB.insert(456)
        RandomQueueB.insert(789)
        return RandomQueueB
    
    def test_insert(self, RandomQueueA, RandomQueueB):
        RandomQueueA.insert(1)
        assert RandomQueueA.items[0] == 1
        assert len(RandomQueueA.items) == 1
        pytest.raises(ValueError, lambda: RandomQueueB.insert(0))

    def test_remove(self, RandomQueueA, RandomQueueB):
        l_elements1 = RandomQueueB.items.copy()
        ele1 = RandomQueueB.remove()
        assert len(RandomQueueB.items) == 2
        assert ele1 in l_elements1
        assert ele1 not in RandomQueueB.items
        l_elements2 = RandomQueueB.items.copy()
        ele2 = RandomQueueB.remove()
        assert len(RandomQueueB.items) == 1
        assert ele2 in l_elements2
        assert ele2 not in RandomQueueB.items
        l_elements3 = RandomQueueB.items.copy()
        ele3 = RandomQueueB.remove()
        assert ele3 in l_elements3
        assert ele1 not in RandomQueueB.items
        assert len(RandomQueueB.items) == 0
        pytest.raises(ValueError, lambda: RandomQueueA.remove())
    
    def test_is_empty(self, RandomQueueA, RandomQueueB):
        assert RandomQueueA.is_empty()
        assert not RandomQueueB.is_empty()
    
    def test_is_full(self, RandomQueueA, RandomQueueB):
        assert not RandomQueueA.is_full()
        assert RandomQueueB.is_full()
    
    def test_clear(self, RandomQueueB):
        RandomQueueB.clear()
        assert RandomQueueB.is_empty()
        

if __name__ == "__main__":
    pytest.main()
