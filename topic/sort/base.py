class BaseSort(object):

    def __init__(self):
        self.data = [
            38,94,89,86,10,47,17,16,75,33,78,41,63,16,33,13,74,61,61,41,18,4,
            22,10,22,69,96,2,64,23,86,82,75,94,15,63,96,6,69,79,7,37,14,18,62,
            31,14,18,62,31,20,23,44,19
        ]
        self.sorted_data = sorted(self.data)

    def sort(self, nums):
        raise NotImplemented

    def run(self):
        result = self.sort(self.data)
        if result == self.sorted_data:
            print("Succ!")
        else:
            print("Failed!")
