#!/usr/bin/python3
def divide_list_safe(list_1, list_2, list_len):

    result = []
    try:
        for i in range(list_len):
            try:
                a = float(list_1[i])  # Try converting to float
                b = float(list_2[i])  # Try converting to float
                if b == 0:
                    raise ZeroDivisionError("division by 0")
                result.append(a / b)
            except ValueError:
                print("wrong type")
                result.append(0)
            except IndexError:
                print("out of range")
                result.append(0)
            except ZeroDivisionError:
                print("division by 0")
                result.append(0)
    finally:
        return result

if __name__ == "__main__":
    list_1 = [9, 2, 6]
    list_2 = [3, 2, 2]
    res = divide_list_safe(list_1, list_2, max(len(list_1), len(list_2)))
    print(res)
    print(10*"_")
    print()

    list_1 = [9, 2, 6, 10]
    list_2 = ["one", 0, 1, 2, 7]
    res = divide_list_safe(list_1, list_2, max(len(list_1), len(list_2)))
    print(res)
