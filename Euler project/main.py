# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import itertools


def euler_test(op):
    result = 0
    for i in range(2, op):
        for j in range(2, op):
            temp = i ** j
            temp_result = 0
            for k in str(temp):
                temp_result += int(k)
            result = max(result, temp_result)
    return result


def euler_test_2(op):
    result = 0
    for i, j in itertools.product(range(2, op), range(2, op)):
        temp = i ** j
        temp_result = 0
        for k in str(temp):
            temp_result += int(k)
        result = max(result, temp_result)
    return result


# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    # print(euler_test(1000))
    print(euler_test_2(1000))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
