# calculate the sum of the numbers

def add_numbers(a, b):
    """Return the sum of two numbers"""
    result = a + b
    return result


num1 = 10
num2 = 20

total = add_numbers(num1, num2)

print(f"the sum is :{total}")

# example
import math

MAX_ATTEMPTS = 3


class StudentCalculator:
    """Class to perform basic calculations for students."""
    def __init__(self, name):
        self.name = name

    def add_numbers(self, a, b):
        """Returns sum of the two numbers"""
        result = a + b
        return result

    def find_square_root(self, number):
        """Return the square root of the number"""
        return math.sqrt(number)

    def display_result(self, student_name, value):
        """Displays result with student name """
        print(f"Student: {student_name}")
        print(f"Values: {value}")

    def main(self):
        """Main function is to run the function"""
        sum_result = self.add_numbers(10, 20)
        sqrt_result = self.find_square_root(25)

        self.display_result(self.name, sum_result)
        self.display_result(self.name, sqrt_result)


if __name__ == "__main__":
    student = StudentCalculator("Nishitha")
    student.main()

