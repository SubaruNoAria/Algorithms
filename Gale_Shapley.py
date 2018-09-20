class Gale_Shapley:
    def __init__(self, n, menPreferences, womenPreferences):
        self._n = n
        self._menPreferences = menPreferences
        self._womenPreferences = womenPreferences

    def stableMatching(self, n, menPreferences, womenPreferences):
        """
        Inputs:
            n - total n men and n women
            menPreferences - two-dimensional array of dimensions n by n,
                contains the list of all women sorted according to their rankings by the man number i
            womenPreferences - two-dimensional array of dimensions n by n,
                contains the list of all men sorted according to their rankings by the women number i
        Output:
            return a list of length n, where ith element is the number of woman chosen for the man number i
        """

        # assert n == len(menPreferences) and n == len(womenPreferences)
        self._n = n
        self._menPreferences = menPreferences
        self._womenPreferences = womenPreferences

        # unmarriedMen -- the list of currently unmarried men;
        unmarriedMen = list(range(self._n))
        #print(unmarriedMen)
        # manSpouse -- the list of current spouses of all man;
        manSpouse = [None] * self._n
        #print(manSpouse)
        # womanSpouse -- the list of current spouses of all woman;
        womanSpouse = [None] * self._n
        # nextManChoice -- contains the number of proposals each man has made.
        nextManChoice = [0] * self._n

        # for each man in unmarriedMen, match him with the women using the ordering
        while len(unmarriedMen) != 0:
            #print(unmarriedMen)
            for man in unmarriedMen:
                for woman in self._menPreferences[man][nextManChoice[man]:]:
                    # if the woman accept the matching, (woman does not have a match or this man is a better match)
                    if womanSpouse[woman] == None:
                        # remove the man from unmarriedMen
                        unmarriedMen.remove(man)
                        # update manSpouse
                        manSpouse[man] = woman
                        # update womanSpouse
                        womanSpouse[woman] = man
                        # update nextManChoice
                        nextManChoice[man] += 1
                        # break, move to the next man on the list
                        break
                    elif self.betterMatch(woman, man, womenPreferences, womanSpouse):
                        unmarriedMen.remove(man)
                        manSpouse[man] = woman
                        unmarriedMen.append(womanSpouse[woman])
                        womanSpouse[woman] = man
                        nextManChoice[man] += 1
                        break
                    # else, if the woman reject
                    else:
                        # update nextManChoice
                        nextManChoice[man] += 1
                        # match next woman
                else:
                    continue
                break
        return manSpouse

    def betterMatch(self, woman, man, womenPreferences, womanSpouse):
        """
        Inputs:
            woman - the index of the woman in womenPreferences
            man - the index of the man in menPreferences
            womenPreferences - two-dimensional array of dimensions n by n,
                contains the list of all men sorted according to their rankings by the women number i
            womanSpouse - the list of current spouses of all woman
        Output:
            check if the man is a better match than the current spouse for the woman
            return True if it is
            return False if it isn't
        """
        self._woman = woman
        self._man = man
        self._womenPreferences = womenPreferences
        self._womanSpouse = womanSpouse

        currentIndex = None
        manIndex = None
        # in womanSpouse, distill the current spouse for woman
        currentSpouse = self._womanSpouse[woman]
        # in womenPreferences[woman] (list), check the index of the current spouse for woman
        # in womenPreferences[woman] (list), check the index of the man for woman
        for i, wp in enumerate(self._womenPreferences[woman]):
            if wp == currentSpouse:
                currentIndex = i
            if wp == man:
                manIndex = i
        # if the index of current spouse < index of man
        if currentIndex < manIndex: return False
            # return False
        # else, return True
        return True
n1 = 1
menPreferences1 = [[0]]
womenPreferences1 = [[0]]
n2 = 2
menPreferences2 = [[0, 1], [1, 0]]
womenPreferences2 = [[0, 1], [1, 0]]
match = Gale_Shapley(n1, menPreferences1, womenPreferences1)
match2 = Gale_Shapley(n2, menPreferences2, womenPreferences2)
match.stableMatching(n1, menPreferences1, womenPreferences1)
match2.stableMatching(n2, menPreferences2, womenPreferences2)
