#!/usr/bin/env python3

row = 3
col = 4

test_list = [[0] * row] * col

for x in range(len(test_list)):
    for y in range(len(test_list[x])):
        print(test_list[x][y])
