# excepition

try:
    x = 1/0
except ZeroDivisionError as e:
    # division by zero
    print(e)