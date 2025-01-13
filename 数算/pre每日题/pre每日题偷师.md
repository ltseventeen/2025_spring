# pre每日题偷师

## 二分查找

在Python中实现二分查找，可以使用标准库`bisect`模块，它提供了两个主要函数：`bisect_left`和`bisect_right`（也分别称为`bisect`），用于在一个**已排序**的列表中找到插入元素的位置。如果列表中存在与目标值相等的元素，`bisect_left`会返回最左边的位置，而`bisect_right`则会返回最右边的位置之后。

但是，如果你想要自己实现一个基本的二分查找算法，而不依赖于`bisect`模块，可以参考以下示例代码：

### 基本二分查找
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # 找到目标，返回索引
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1  # 如果找不到目标，返回-1
```

### 使用递归实现二分查找
```python
def binary_search_recursive(arr, target, left, right):
    if right >= left:
        mid = (left + right) // 2

        # 如果找到了目标，返回其索引
        if arr[mid] == target:
            return mid
        # 如果目标小于中间元素，在左半部分继续查找
        elif arr[mid] > target:
            return binary_search_recursive(arr, target, left, mid - 1)
        # 否则，在右半部分继续查找
        else:
            return binary_search_recursive(arr, target, mid + 1, right)
    else:
        # 目标不在数组中
        return -1
```

### 查找左侧边界的二分查找
```python
from bisect import bisect_left

def binary_search_left(arr, target):
    index = bisect_left(arr, target)
    if index != len(arr) and arr[index] == target:
        return index
    else:
        return -1
```

### 查找右侧边界的二分查找
```python
from bisect import bisect_right

def binary_search_right(arr, target):
    index = bisect_right(arr, target)
    if index > 0 and arr[index - 1] == target:
        return index - 1
    else:
        return -1
```

上述代码展示了如何用Python实现二分查找的不同版本。对于简单的情况，你可以直接使用这些函数。如果你需要处理更复杂的情况，例如处理重复元素或查找范围，你可能需要调整这些函数以满足你的需求。记住，使用`bisect`模块时，你需要确保输入的数组是已经排序的。