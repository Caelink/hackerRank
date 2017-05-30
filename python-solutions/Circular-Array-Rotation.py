import sys

def right_rotate(a, k_r):
    new_front = a[(n-k_r):]
    new_back = a[:(n-k_r)]
    return new_front + new_back
    
n, k, q = map(int,raw_input().split(' '))
arr = map(int,raw_input().split(' '))
m_list = []
for x in range(0, q):
    m_list.append(int(raw_input()))
    
if k > n:
    k = k%n
    
arr = right_rotate(arr, k)

for m in m_list:
    print arr[m]
