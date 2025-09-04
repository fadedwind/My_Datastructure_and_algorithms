数组
在 Python 中，数组通常用列表（list）来实现。常用语法如下：

### 1. 创建列表
```python
nums = [1, 2, 3, 4]
```

### 2. 访问元素
```python
print(nums[0])  # 输出 1
print(nums[-1]) # 输出 4（倒数第一个）
```

### 3. 修改元素
```python
nums[1] = 10
print(nums)  # [1, 10, 3, 4]
```

### 4. 添加元素
```python
nums.append(5)      # 末尾添加
nums.insert(1, 20)  # 指定位置插入
```

### 5. 删除元素
```python
nums.pop()      # 删除末尾元素
nums.pop(1)     # 删除指定位置元素
nums.remove(3)  # 删除指定值（只删第一个）
```

### 6. 遍历列表
```python
for num in nums:
    print(num)
```

### 7. 列表切片
```python
print(nums[1:3])  # 输出第2到第3个元素
```

### 8. 获取长度
```python
print(len(nums))
```

### 9. 判断元素是否存在
```python
if 2 in nums:
    print("存在")
```

Python 的 list 是动态数组，可以存放任意类型的数据。