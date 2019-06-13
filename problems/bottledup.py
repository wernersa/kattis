import sys
import math

shipment, big, small = map(int, sys.stdin.readline().strip("\n").split(" "))
big_times = math.floor(shipment / big)

for big_i in range(big_times, -1, -1):
    big_vol = big_i * big
    if (shipment - big_vol) % small == 0:
        print(big_i, (shipment - big_vol) // small)
        exit()

print("Impossible")