import sys
from math import log2, floor


def solve(number):
    a = int(floor(log2(abs(number))))
    eps = 10e-8
    for j in reversed(range(2, a + 1)):

        root = abs(number) ** (1 / j)
        if (root % 1) < eps or ((root % 1) - 1) < eps:
            # Might be worth trying
            if not int(round(root)) ** j == abs(number):
                # print(root, int(round(root)), j,  number)
                # print(' continue here')
                continue

            else:

                if number > 0:
                    return j
                    break
                else:
                    # It's negative
                    if j % 2 == 0:
                        continue
                    else:
                        # It's odd
                        return j
                        break

    return 1


for number in sys.stdin:

    number = int(number.strip("\n"))

    if number == 0:
        break

    print(solve(number))
