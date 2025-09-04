import numpy as np

# 初始化
n = 7
p = [0.04, 0.06, 0.08, 0.02, 0.10, 0.12, 0.14]
q = [0.06, 0.06, 0.06, 0.06, 0.05, 0.05, 0.05, 0.05]

e = np.zeros((n+2, n+1))
w = np.zeros((n+2, n+1))
root = np.zeros((n+1, n+1), dtype=int)

# 初始化 w 和 e 表格
for i in range(1, n+2):
    e[i, i-1] = q[i-1]
    w[i, i-1] = q[i-1]

for l in range(1, n+1):
    for i in range(1, n-l+2):
        j = i + l - 1
        e[i, j] = float('inf')
        w[i, j] = w[i, j-1] + p[j-1] + q[j]
        
        for r in range(i, j+1):
            t = e[i, r-1] + e[r+1, j] + w[i, j]
            if t < e[i, j]:
                e[i, j] = t
                root[i, j] = r

# 打印结果  
print(" 表格:")
print(w[1:n+1, 0:n+1])
print("e 表格:")
print(e[1:n+1, 0:n+1])
print("\nroot 表格:")
print(root[1:n+1, 1:n+1])


    
    