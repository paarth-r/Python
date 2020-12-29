def kidsWithCandies(candies, extraCandies):
        returnlist = []
        for n in range(len(candies)):
            if candies[n] + extraCandies >= max(candies):
                returnlist.append(True)
            else:
                returnlist.append(False)
        return returnlist
