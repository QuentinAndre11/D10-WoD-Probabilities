import random

"""
The goal of this code is to get the probability of success when you roll your dices with the World of Darkness roleplaying system.

Brief reminder of the WoD system :

- Roll as many D10 (dices with 10 faces) as your character score in attribute + skill
    (example : you want to give a sword blow, you have a strength of 3 and a score in melee of 2, you roll 3+2=5 dices)

- Difficulty threshold is given by the Game Master. A dice is a success if the value of the dice is greater or equal than the difficulty, except if the value is one. In this case, it substracts one success at the total.

- If the total is strictly positive, the action is a success. If you have 0 success, it is a failure. If it is negative, it is a critical failure.
    (example : you roll your 5 dices, you have 10,10,6,5,1. Your GM says the difficulty is set at 6. You have 3-1=2 success, you success in your action)

- Special rule : if your character has the attribute "hero", your 10 are counted as 2 success, but are cancelled by the 1 in the first place.
    (example : with the same roll, you have now one 10 which is cancelled by the one, and the other 10 counts two success. So you have 3 success)

In this code, there are two useful functions :
    - rollsStats(dices,diff,hero) which gives the useful statistics for a given number of dices and difficulty (and the optional hero attribute)
    - prettyArray(hero,maxDices,value) which gives an array with difficulty as columns and number of dices as rows. You can choose what statistic is shown with the input "value", and you can input whether you want an array for hero attribute, and the maximum number of rows (number of dices). We stored these arrays in the readme for 20 dices.
"""

def roll(dices, diff, hero=False) :

    """
    Returns the number of success for one roll. A negative number of success is a critical failure, no success corresponds to a failure and one or more
    success corresponds to a success for the roll.

    Parameters
    ----------
    dices : int
        Number of dices (D10) which will be rolled.
    diff : int
        Difficulty of the roll. A dice is counted as a success if the value of the dice is greater or equal to the difficulty.
    hero : optional bool
        If the character is a hero, its 10 count two success instead of one, but are cancelled first by a critical failure (a one on another dice).

    Raises
    ------
    ValueError
        If the number of dices is negative or null, or the difficulty is not between 1 and 10 (we use a D10).
    """

    if (dices < 1 or diff < 1 or diff > 10):
        raise ValueError

    L = initialList(dices)
    L = transformedList(L)
    return countSuccess(L, diff, hero)


def initialList(dices) :

    """
    Creates a list L with all the rolled dices, we sort it by decreasing order to use it more easily.

    Parameters
    ----------
    dices : int
        Number of dices (D10) which will be rolled.
    """

    L = []
    for i in range(dices) :
        L.append(random.randint(1,10))
    L.sort(reverse = True)
    return L


def transformedList(L) :

    """
    Creates a list R which is the list L whithout the dices with value 10 cancelled by those with value 1

    Parameters
    ----------
    L: int list
        Decreasing sorted list with values between 1 and 10.
    """

    R = []
    for r in L :
        if r == 10 :
            if L[-1] == 1 :
                L.pop()
            else :
                R.append(r)
        else :
            R.append(r)
    return R


def countSuccess(L, diff, hero) :

    """
    Counts the number of success for the roll.

    Parameters
    ----------
    L: int list
        Decreasing sorted list with values between 1 and 10.
    diff : int
        Difficulty of the roll. A dice is counted as a success if the value of the dice is greater or equal to the difficulty.
    hero : optional bool
        If the character is a hero, its 10 count two success instead of one, but are cancelled first by a critical failure (a one on another dice).
    """

    success = 0
    for val in L :
        if val == 1 :
            success -= 1
        elif val == 10 :
            if hero :
                success += 2
            else :
                success += 1
        elif val >= diff :
            success += 1
    return success


def rollsStats(dices,diff,hero=False) :

    """
    Launches a serie of 10000 rolls to return a list with average number of success, probability of success, failure and critical failure.

    Parameters
    ----------
    dices : int
        Number of dices (D10) which will be rolled.
    diff : int
        Difficulty of the roll. A dice is counted as a success if the value of the dice is greater or equal to the difficulty.
    hero : optional bool
        If the character is a hero, its 10 count two success instead of one, but are cancelled first by a critical failure (a one on another dice).

    Raises
    ------
    ValueError
        If the number of dices is negative or null, or the difficulty is not between 1 and 10 (we use a D10).
    """

    if (dices < 1 or diff < 1 or diff > 10):
        raise ValueError

    m = 0 #m is the average number of success
    successRate = 0
    failureRate = 0
    criticRate = 0
    for i in range (10000) :
        success = roll(dices,diff,hero)
        m += success
        if success < 0 :
            criticRate +=1
        elif success == 0 :
            failureRate += 1
        else :
            successRate += 1
    S = [m,successRate,failureRate,criticRate]
    res = []
    for s in S :
        res.append(round(s/100)/100) #limits probability with 2 decimal numbers to keep it readable
    return res

def array(hero=False, maxDices=20, value="Average number of success") :

    """
    Creates a complete array for the wanted information (average number of success by default, or success rate, failure rate or critical failure rate)
    giving the information for all difficulties and a number of dices between 1 and maxDices

    Parameters
    ----------
    hero : optional bool
        If the character is a hero, its 10 count two success instead of one, but are cancelled first by a critical failure (a one on another dice).
    maxDices : optional int
        Defines the number of rows (range of values for the number of dices)
    value : optional string
        Information needed (average number of success by default, or success rate, failure rate or critical failure rate)

    Raises
    ------
    ValueError
        If the information needed is not with the right format, raises the right format.
    """

    ind = 0
    if (value == "average number of success" or value == "0") :
        ind = 0
    elif (value == "success rate" or value == "1") :
        ind = 1
    elif (value == "failure rate" or value == "2") :
        ind = 2
    elif (value == "critical failure rate" or value == "3") :
        ind = 3
    else :
        raise ValueError("Try with average number of success, success rate, failure rate, critical failure rate, or 0, 1, 2, 3")

    T = []
    for dices in range (maxDices) :
        print(dices)
        T.append([])
        for d in range(10) :
            stats = rollsStats(dices+1,d+1,hero)
            T[dices].append(stats[ind])
    return T

def prettyArray(hero=False, maxDices=20, value="Average number of success") :

    """
    Prints the same array as array() but prettier

    Parameters
    ----------
    hero : optional bool
        If the character is a hero, its 10 count two success instead of one, but are cancelled first by a critical failure (a one on another dice).
    maxDices : optional int
        Defines the number of rows (range of values for the number of dices)
    value : optional string
        Information needed (average number of success by default, or success rate, failure rate or critical failure rate)
    """

    #data
    a = array(hero,maxDices,value)

    #labels
    columns = [i+1 for i in range(10)]
    rows = [i+1 for i in range(maxDices)]

    row_format ="{:>8}" * (len(columns) + 1)
    print(row_format.format("", *columns))
    for t, row in zip(rows, a):
        print(row_format.format(t, *row))