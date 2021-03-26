import rolls

# I can't imagine a unit test for roll (because of alea)

def test_initialList():
    """Check that `initialList()` is ordered in the right order"""

    L=initialList(10)
    assert L[0] >= L[1]

def test_transformedList():
    """Check that `transformedList()` works as expected"""

    L1=transformedList([10,10,6,5,1])
    L2=transformedList([10,6,5,1,1])
    L3=transformedList([8,6,5,1,1])
    L4=transformedList([10,10,6,5,2])
    assert L1 == [10,6,5]
    assert L2 == [6,5,1]
    assert L3 == [8,6,5,1,1]
    assert L4 == [10,10,6,5,2]

def test_countSuccess() :
    """Check that `countSuccess()` works as expected"""

    L1=[10,9,8,7,6,5,4,3,2]
    L2=[10,10,8,7,6,5,4,3,2]
    L3=[9,9,8,7,6,5,4,3,2]
    L4=[9,8,7,6,5,4,3,2,1]
    L5=[9,8,7,6,5,4,3,1,1]
    assert countSuccess(L1,6,False) == 5
    assert countSuccess(L1,8,False) == 3
    assert countSuccess(L1,6,True) == 6
    assert countSuccess(L2,6,False) == 5
    assert countSuccess(L2,6,True) == 7
    assert countSuccess(L3,6,False) == 5
    assert countSuccess(L3,6,True) == 5
    assert countSuccess(L4,6,False) == 3
    assert countSuccess(L5,6,True) == 2

def test_rollsStats() :
    """Check that `rollsStats()` works as expected with a margin of 0.2"""

    def withMargin(L1,L2) :
        for i in range(len(L1)) :
            assert abs(L1[i]-L2[i]) <= 0.2

    withMargin(rollsStats(1,6,hero=False), [0.4, 0.5, 0.4, 0.1])
    withMargin(rollsStats(1,8,hero=False), [0.2, 0.2, 0.7, 0.1])
    withMargin(rollsStats(1,6,hero=True), [0.5, 0.5, 0.4, 0.1])
    withMargin(rollsStats(2,6,hero=False), [0.84, 0.64, 0.28, 0.08]) #verified by enumerating
    withMargin(rollsStats(2,6,hero=True), [0.97, 0.64, 0.28, 0.08]) #verified by enumerating
    withMargin(rollsStats(2,8,hero=False), [0.51, 0.43, 0.45, 0.12]) #verified by enumerating
    withMargin(rollsStats(2,8,hero=True), [0.62, 0.43, 0.45, 0.12]) #verified by enumerating

# array and prettyArray are only visuals