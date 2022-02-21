# import numpy as np

# t = np.array([0.,1.,2.,3.,4.,5.,6.])
# print(t)

# #1차원벡터의 차원
# print('Rank of t:', t.ndim)

# #1차원벡터의 크기
# print('Shape of t:', t.shape)

# t = np.array([[1.,2.,3.],[4.,5.,6.],[7.,8.,9.],[10.,11.,12]])
# print(t)

# #2차원벡터의 차원
# print('Rank of t:', t.ndim)

# #2차원벡터의 크기
# print('Shape of t:', t.shape)

import torch

# t = torch.FloatTensor([0., 1., 2., 3., 4., 5., 6.])
# print(t)

# print(t.dim())  # rank. 즉, 차원
# print(t.shape)  # shape
# print(t.size()) # shape

# print(t[0], t[1], t[-1])  # 인덱스로 접근
# print(t[2:5], t[4:-1])    # 슬라이싱
# print(t[:2], t[3:])       # 슬라이싱

# t = torch.FloatTensor([[1., 2., 3.],
#                        [4., 5., 6.],
#                        [7., 8., 9.],
#                        [10., 11., 12.]
#                       ])
# print(t)

# print(t.dim())  # rank. 즉, 차원
# print(t.size()) # shape

# print(t[:, 1]) # 첫번째 차원을 전체 선택한 상황에서 두번째 차원의 첫번째 것만 가져온다.
# print(t[:, 1].size()) # ↑ 위의 경우의 크기

# print(t[:, :-1]) # 첫번째 차원을 전체 선택한 상황에서 두번째 차원에서는 맨 마지막에서 첫번째를 제외하고 다 가져온다.

# m1 = torch.FloatTensor([[3, 3]])
# m2 = torch.FloatTensor([[2, 2]])
# print(m1+m2)

# m1 = torch.FloatTensor([[1, 2]])
# m2 = torch.FloatTensor([3]) # [3] -> [3, 3]
# print(m1 + m2)

# m1 = torch.FloatTensor([[1, 2]])
# m2 = torch.FloatTensor([[3], [4]])
# print(m1+m2)

# # 브로드캐스팅은 항상 주의 원하지않게 사요될 수 있다.

# m1 = torch.FloatTensor([[1,2],[3,4]])
# m2 = torch.FloatTensor([[1],[2]])
# print('Shape of Matrix 1: ', m1.shape) # 2 x 2
# print('Shape of Matrix 2: ', m2.shape) # 2 x 1
# #matmul = 행렬곱셈
# print(m1.matmul(m2)) # 2 x 1

# m1 = torch.FloatTensor([[1, 2], [3, 4]])
# m2 = torch.FloatTensor([[1], [2]])
# print('Shape of Matrix 1: ', m1.shape) # 2 x 2
# print('Shape of Matrix 2: ', m2.shape) # 2 x 1
# #element-wise = 동일한 위치에 있는 원소끼리 곱함(브로드캐스팅 하고)
# print(m1 * m2) # 2 x 2
# print(m1.mul(m2))

# t = torch.FloatTensor([1, 2])
# print(t.mean())

# t = torch.FloatTensor([[1, 2], [3, 4]])
# #dim = 0 => 첫번째 차원, 즉 행, 
# print(t.mean(dim=0))

t = torch.FloatTensor([[1, 2], [3, 4]])
print(t)
print(t.max()) # Returns one value: max
print(t.max(dim=0)) # Returns two values: max and argmax
print('Max: ', t.max(dim=0)[0])
print('Argmax: ', t.max(dim=0)[1])

