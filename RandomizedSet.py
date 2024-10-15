import random


class RandomizedSet:

    def __init__(self):
        self.numMap = {}
        self.numList = []

    def insert(self, val: int) -> bool:
        res = val not in self.numMap
        if res:
            self.numMap[val] = len(self.numList)
            self.numList.append(val)
        return res

    def remove(self, val: int) -> bool:
        res = val in self.numMap
        if res:
            idx = self.numMap[val]
            self.numList[idx] = self.numList[-1]
            self.numMap[self.numList[-1]] = idx
            self.numList.pop()
            del self.numMap[val]

        return res

    def getRandom(self) -> int:
        if not len(self.numList):
            return False
        return random.choice(self.numList)


obj = RandomizedSet()
val = 2
resut1 = obj.getRandom()
resut2 = obj.remove(val)
resut2 = obj.insert(val)
