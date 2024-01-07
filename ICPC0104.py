import re
import math

for _ in range(int(input())):
    x = input()
    numbers = re.findall(r'[0-9]+', x)
    numbers = [int(x) for x in numbers]
    print(max(numbers))