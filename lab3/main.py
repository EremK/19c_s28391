# Task 1
# squares_list = [x ** 2 for x in range(1, 11)]
# print(squares_list)


# Task 2
# def e_squares(start, end):
#     return [x ** 2 for x in range(start, end)]
#
#
# print(e_squares(3, 15))


# Task 3
class SquareGenerator:
    @staticmethod
    def e_squares(start, end):
        return [x ** 2 for x in range(start, end)]


print(SquareGenerator.e_squares(5, 21))
