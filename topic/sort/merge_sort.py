from base import BaseSort

class MergeSort(BaseSort):

    def sort(self, nums):
        if len(nums) < 2:
            return nums
        l = nums[:len(nums)/2]
        r = nums[len(nums)/2:]
        l = self.sort(l)
        r = self.sort(r)
        return self.merge(l, r)

    def merge(self, l, r):
        re = []
        while l and r:
            if l[0] < r[0]:
                re.append(l[0])
                l = l[1::]
            else:
                re.append(r[0])
                r = r[1::]
        if l:
            re += l
        if r:
            re += r
        return re


if __name__ == '__main__':
    MergeSort().run()
