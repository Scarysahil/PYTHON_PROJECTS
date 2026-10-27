def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

check = is_even(4)
check2 = is_even(5)
check3 = is_even(0)
print(f"Is the number even? {check}")
print(f"Is the number even? {check2}")
print(f"Is the number even? {check3}")