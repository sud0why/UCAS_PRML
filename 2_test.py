# 两类模式具有正态概率密度函数
# ω1 {(0,0),(2,0),(2,2),(0,2)}
# ω2 {(4,4),(6,4),(6,6),(4,6)}
# P(ω1) = P(ω2) = 1/2
# 1. 求这两类模式之间的贝叶斯判别界面的方程式
# 2. 绘出判别界面

import numpy as np

# for test
test = [[1, 0, 1], [1, 0, 0], [0, 0, 0], [1, 1, 0]]
test = np.array(test)
test = test.T
m_test = np.mean(test, axis=1).reshape(3, 1)
print(test)
print(m_test)
n_test = np.size(test, 1)
tmp_test = test - m_test
print(tmp_test)
c_test = np.zeros([3, 3])

for i in range(n_test):
    test_i = tmp_test[:, i].reshape([3, 1])
    c_test = c_test + test_i * test_i.T

c_test = c_test/n_test
print(c_test)

c_mat = np.mat(c_test)
c_inv = np.linalg.inv(c_mat)
print(c_inv)

# for solution
# w1 = [[0, 0], [2, 0], [2, 2], [0, 2]]
# w2 = [[4, 4], [6, 4], [6, 6], [4, 6]]
# w1 = np.array(w1)
# w2 = np.array(w2)
# w1 = w1.T
# w2 = w2.T
# print(w1)
# print(w2)
# print(w2.shape)
# m1 = np.mean(w1, axis=1).reshape(2, 1)
# m2 = np.mean(w2, axis=1).reshape(2, 1)
# print(m1)
# print(m2)
# n1 = np.size(w1, 1)
# n2 = np.size(w1, 1)
# print(n1)
# print(n2)
# # print(w1[:, 1])
#
# tmp1 = w1 - m1
# tmp2 = w2 - m2
# print(tmp1)
# print(tmp2)
#
# c1 = np.zeros([2, 2])
# c2 = np.zeros([2, 2])
#
# for i in range(n1):
#     w1_i = tmp1[:, i].reshape([2, 1])
#     c1 = c1 + w1_i * w1_i.T
#
# for i in range(n2):
#     w2_i = tmp2[:, i].reshape([2, 1])
#     c2 = c2 + w2_i * w2_i.T
#
# c1 = c1/n1
# c2 = c2/n2

