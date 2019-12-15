import numpy as np


w1 = [[0, 0, 0], [1, 0, 0], [1, 0, 1], [1, 1, 0]]
w1 = np.array(w1)
w1 = w1.T

w2 = [[0, 0, 1], [0, 1, 1], [0, 1, 0], [1, 1, 1]]
w2 = np.array(w2)
w2 = w2.T


tmp = np.ones((1, 4))

w1 = np.concatenate((w1, tmp), axis=0)
w2 = np.concatenate((w2, tmp), axis=0)
w2 = w2 * -1
print(w1)
print(w2)
w = np.concatenate((w1, w2), axis=1)
print(w)

# 解向量设为a
# 初始化解向量
# 取C = 1
a = np.array([[0, 0, 0, 0]])
# print(np.dot(a, w[:, 1].reshape([4, 1]))[0, 0])
# print(flag and True and False)
while True:
    # 初始化标志位
    flag = True
    for _ in range(8):
        if np.dot(a, w[:, _].reshape([4, 1]))[0, 0] > 0:
            a = a
            flag = flag and True
        else:
            a = a + w[:, _].reshape([1, 4])
            flag = flag and False

    if flag:
        break

print(a)
