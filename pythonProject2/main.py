# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def fact(n):
    if n == 0:
        return 1
    else:
        return (n * fact(n-1))

def pas_tri_row(numRows):
    result = [0] * numRows
    for i in range(numRows):
        result[i] = int(fact(numRows-1) / (fact(i) * fact(numRows - i - 1)))
    return result

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    result = []
    for i in range(5):
        result.append(pas_tri_row(i+1))
    print(result)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
