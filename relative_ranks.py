import numpy as np
class Sol:
    def relative_ranks(self,nums):
        sorted_nums = list(np.sort(nums))[::-1]
        for i,num in enumerate(sorted_nums):
            if i==0:
                nums.insert(nums.index(num),'gold')
                nums.remove(num)
            elif i==1:
                nums.insert(nums.index(num),'silver')
                nums.remove(num)
            elif i==2:
                nums.insert(nums.index(num),'bronze')
                nums.remove(num)
            else:
                nums.insert(nums.index(num),str(sorted_nums.index(num)+1))
                nums.remove(num)
        return nums
