
class RollingAverageNumber:

    def __init__(self, average_count=1):
        self.average_count = average_count
        self.num_list = [0] * self.average_count
        self.value, self.prev_value = 0, 0

    def add(self, num):
        if len(self.num_list) == self.average_count:
            self.num_list = self.num_list[1:]
        self.num_list.append(num)
        self.prev_value = self.value
        self.value = self.get_value()

        if self.prev_value == self.value and self.value != self.num_list[-1]:
            self.reset()

    def get_value(self):
        return sum(self.num_list)/self.average_count

    def reset(self):
        self.num_list = [0] * self.average_count
        self.value, self.prev_value = 0, 0

    def __str__(self):
        return f"RollingAverageNumber(" \
               f"num_list=[{''.join([str(num).rjust(3) for num in self.num_list])}]), " \
               f"value={self.get_value()})"
