try:
    print("life's good")
    print([1,2,3][4])
    print("After life")

except ZeroDivisionError as e:
    print("ZeroError", e)
except IndexError as e:
    print("IndexError",e)
else:
    print("Irun only when ther's no Error")
finally:
    print("I run every time")