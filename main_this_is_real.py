# -*- coding: utf-8 -*-

import queue
from sys import stdin
import cv2

import image_save

# 길 찾기 검증용 함수

# def printroad(road, path=""):
#     for y, ro in enumerate(road):
#         for x, pos in enumerate(ro):
#             if pos == '1':
#                 start_x = x
#                 start_y = y
#                 break
#             else :
#                 pass

#     i = start_x
#     j = start_y

#     pos = set()
#     for move in path:
#         if move == 'L':
#             i -= 1

#         elif move == 'R':
#             i += 1

#         elif move == 'U':
#             j -= 1

#         elif move == 'D':
#             j += 1
#         pos.add((j, i))
    
#     for j, row in enumerate(road):
#         for i, col in enumerate(row):
#             if (j, i) in pos:
#                 print("+ ", end="")
#             else:
#                 print(col + "0 ", end="")
#         print()


# 경로 찾기
def valid(road, moves):
    for y, ro in enumerate(road):
        for x, pos in enumerate(ro):
            if pos == 1:
                start_x = x
                start_y = y


    i = start_x
    j = start_y

    for move in moves:
        if move == 'L':
            i -= 1

        elif move == 'R':
            i += 1

        elif move == 'U':
            j -= 1

        elif move == 'D':
            j += 1

        if not(0 <= i < len(road[0]) and 0 <= j < len(road)):
            return False
        elif (road[j][i] == 3):
            return False

    return True


# 경로 마지막 지점 파악
def findEnd(road, moves):
    for y, ro in enumerate(road):
        for x, pos in enumerate(ro):
            if pos == 1:
                start_x = x
                start_y = y


    i = start_x
    j = start_y

    for move in moves:
        if move == 'L':
            i -= 1

        elif move == 'R':
            i += 1

        elif move == 'U':
            j -= 1

        elif move == 'D':
            j += 1

    if road[j][i] == 2:
        print("number of moves: {}".format(len(moves)))
        # printroad(road, moves)
        return True

    return False


# MAIN ALGORITHM

n = int(float(input()))     # numbers of test case
a = 0
while a < n :

    nums = queue.Queue()
    nums.put('')
    add = ''

    input = stdin.readline
    N, M = map(int, input().split())
    road = [list(map(int, list(input().split(' ')))) for _ in range(N)]

    while not findEnd(road, add): 
        add = nums.get()
        # print(add)
        for j in ['L', 'R', 'U', 'D']:
            put = add + j
            if valid(road, put):
                nums.put(put)

    img = image_save.image(road, N, M)
    cv2.imwrite("./heven_coding_test/{}.png".format(n), img)
    a += 1