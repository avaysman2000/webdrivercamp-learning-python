#!/usr/bin/python3
def divide_safe(a, b):

    try:
        result = a / b
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
        return None
    finally:
        if 'result' in locals():
            print(f"Result: {result}")
        else:
            print("Result: None")
    return result

if __name__ == "__main__":
    a = 9
    b = 3
    result = divide_safe(a, b)
    print(f"{a} / {b} = {result}")
    
    b = 0
    result = divide_safe(a, b)
    print(f"{a} / {b} = {result}")
