class SquareGenerator:
    @staticmethod
    def e_squares(start, end):
        if start > end:
            raise ValueError("Start index must be smaller than the end one.")
        return [x ** 2 for x in range(start, end)]