
class RollingAverageNumber:

    def __init__(self, average_count=1):
        self.average_count = average_count
        self.num_list = []

    def add(self, num):
        if len(self.num_list) == self.average_count:
            self.num_list = self.num_list[1:]
        self.num_list.append(num)

    def get_value(self):
        return sum(self.num_list)/self.average_count
