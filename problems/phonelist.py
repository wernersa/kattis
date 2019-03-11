import sys
lines = [k.strip('\n') for k in sys.stdin.readlines()]

i_left = 0
i_phone_list = -1

for i, line in enumerate(lines):
    if i == 0:
        phone_lists = list(range(int(line)))
        continue
    if i_left == 0:
        i_phone_list += 1
        phone_lists[i_phone_list] = list(range(int(line)))
        i_left = int(line)
        continue
    else:
        phone_lists[i_phone_list][i_left - 1] = line
        i_left -= 1


def check_list(phone_list: list):
    phone_list.sort()
    for i, number in enumerate(phone_list[:-1]):
        if phone_list[i+1][0:len(number)] == number:
            return "NO"
    return "YES"

for phone_list in phone_lists:
    print(check_list(phone_list))