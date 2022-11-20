def addBinary(a: str, b: str) -> str:
    """sets variables i, j, carry, and res
    i is a pointer for string a and j is a pointer for b
    carry is for carrying numbers when adding 1+1 which would give a carry of 1
    res is the return value
    """
    i, j, carry, res = len(a) - 1, len(b) - 1, 0, ""
    while i >= 0 or j >= 0:
        sum = carry;  # intitialize sum with carry
        if i >= 0: sum += ord(a[i]) - ord('0')  # ord is use to get value of ASCII character
        if j >= 0: sum += ord(b[j]) - ord('0')
        i, j = i - 1, j - 1
        carry = 1 if sum > 1 else 0;
        res += str(sum % 2)

    if carry != 0: res += str(carry);
    return res[::-1]


# this program will not check if values are not binary as thats not the point of the algorithm
print("Please use enter two binary numbers to add together")
a = input()
b = input()

print(addBinary(a, b))
