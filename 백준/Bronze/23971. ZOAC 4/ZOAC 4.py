import sys
input = sys.stdin.readline
import math


H,W,N,M = map(int, input().split())

count_h = math.ceil(H/(N+1))
count_w = math.ceil(W/(M+1))

print(count_h*count_w)