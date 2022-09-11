class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # dict1 = {}
        # for i in nums:
        #     if i in dict1:
        #         dict1[i] += 1
        #     else:
        #         dict1[i] = 1
        # for key,value in dict1.items():
        #     if value > 1:
        #         return True
        #     else:
        #         return False
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False
            
        