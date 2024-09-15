import random
from typing import List


class Demonstration:

    def __init__(self):
        self.num_columns = self.request_num_columns()
        self.max_depth = self.request_max_depth()
        self.multiplier = self.request_multiplier()

    def do_process(self) -> None:
        self.recursive_method(1)

    def recursive_method(self, depth: int) -> None:
        if depth > self.max_depth:
            return
        self.draw_row(depth)
        self.test_sort(depth)
        self.recursive_method(depth+1)
        self.draw_row(depth)

    @staticmethod
    def request_num_columns() -> int:
        """
        requests a number of columns from the user
        :return: an int input from user.
        """
        num_columns = -1
        response = input("How many columns should I draw? ")
        try:
            num_columns = int(response)
        except ValueError as v_err:
            print(v_err)
            print("There was a problem. ")
        return num_columns

    @staticmethod
    def request_max_depth() -> int:
        """
        requests a max depth from the user
        :return: an int input from user.
        """
        max_depth = -1
        response = input("How deep should the recursion go? ")
        try:
            max_depth = int(response)
        except ValueError as v_err:
            print(v_err)
            print("There was a problem. ")
        return max_depth

    @staticmethod
    def request_multiplier() -> int:
        """
        requests a multiplier from the user
        :return: an int input from user.
        """
        multiplier = -1
        response = input("By what factor should the sort increase? ")
        try:
            multiplier = int(response)
        except ValueError as v_err:
            print(v_err)
            print("There was a problem. ")
        return multiplier

    def draw_row(self, d: int) -> None:
        """
        prints a row consisting of the number, d, a tab, and then self.num_columns characters... spaces except for some
        asterisks when a factor of d is reached.
        :param d: the common factor of all locations that get a "*".
        :return: None
        """
        output = f"{d}\t"
        for i in range(0, self.num_columns):
            if i % d == 0:
                output += "*"
            else:
                output += " "
        print(output)

    def test_sort(self, power: int) -> None:
        size = pow(self.multiplier, power)
        randomized_list = self.build_list(size)
        self.sort_randomized_list(randomized_list, size)

    @staticmethod
    def build_list(size: int) -> List[int]:
        """
        construct a shuffled list of numbers from 0 to size-1, inclusive, with no repeats.
        :param size: how many numbers should be in the list
        :return: a list of <size> random integers, from 0 to size-1, inclusive.
        """
        result = random.sample(range(0, size), size)
        return result

    @staticmethod
    def sort_randomized_list(list_to_sort: List[int], size: int) -> None:
        """
        checks that the list is of the correct length, and then sorts it.
        :param list_to_sort: the list we wish to sort
        :param size: this should be the length of the list.
        :return: None
        """
        assert size == len(list_to_sort)
        list_to_sort.sort()


if __name__ == "__main__":
    demo = Demonstration()
    demo.do_process()
