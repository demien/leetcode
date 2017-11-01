from base import BaseSort

class QuickSort(BaseSort):

    def sort(self, nums):
        return self.sort_in_place(nums)
        return self.sort_with_extra_list(nums)

    def sort_with_extra_list(self, nums):
        if len(nums) < 2:
            return nums
        i, j = 0, len(nums) - 1
        pivot = nums[0]
        low, high, pivots = [], [], []
        for n in nums:
            if n < pivot:
                low.append(n)
            if n > pivot:
                high.append(n)
            if n == pivot:
                pivots.append(n)
        return self.sort_with_extra_list(low) + pivots + self.sort_with_extra_list(high)


    def sort_in_place(self, nums):
        if len(nums) < 2:
            return nums
        i, j = 0, len(nums) - 1
        base = nums[0]

        def _switch(i, j, nums):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        while i < j:
            while i < j and nums[j] >= base:
                j -= 1
            if i < j:
                _switch(i, j, nums)
            while i < j and nums[i] <= base:
                i += 1
            if i < j:
                _switch(i, j, nums)
        return self.sort(nums[:i]) + [nums[i]] + self.sort(nums[i+1:])


if __name__ == '__main__':
    QuickSort().run()
