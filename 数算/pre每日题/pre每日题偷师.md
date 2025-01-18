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

------



## 找最大公因数和最小公倍数

### 最大公因数（GCD）

求两个数的最大公因数（Greatest Common Divisor, GCD）在Python中可以通过多种方式实现。最常用的方法是使用**辗转相除法**，也称为欧几里得算法。Python标准库中的**`math`模块提供了一个名为`gcd`的函数**可以直接用于计算最大公因数。

下面是几种求解两个数的最大公因数的方法：

#### 使用 math.gcd 函数

这是最简单直接的方法：

```python
import math

def find_gcd(x, y):
    return math.gcd(x, y)

# 示例
x = 48
y = 18
print(f"The GCD of {x} and {y} is {find_gcd(x, y)}")
```

#### 使用欧几里得算法手动实现

如果不想要使用内置函数，可以自己实现一个基于欧几里得算法的函数：

```python
def gcd_euclidean(x, y):
    while(y):
        x, y = y, x % y
    return x

# 示例
x = 48
y = 18
print(f"The GCD of {x} and {y} is {gcd_euclidean(x, y)}")
```

==这段代码实现了欧几里得算法的核心思想：两个数a和b的最大公因数等于b和a%b（a除以b的余数）的最大公因数。==

### 最小公倍数 (LCM)

最小公倍数可以通过最大公因数来计算，因为==两数乘积等于这两个数的最大公因数与最小公倍数的乘积。==

为了找到最小公倍数，我们可以先定义一个函数，这个函数将利用最大公因数来计算最小公倍数。公式为：`lcm(a, b) = abs(a*b) // gcd(a, b)`。

```python
def find_lcm(x, y):
    return abs(x * y) // math.gcd(x, y)

# 示例
lcm_value = find_lcm(x, y)
print(f"The LCM of {x} and {y} is {lcm_value}")
```

如果你想要在一个步骤中同时计算GCD和LCM，你可以这样做：

```python
def find_gcd_and_lcm(x, y):
    gcd_val = math.gcd(x, y)
    lcm_val = abs(x * y) // gcd_val
    return gcd_val, lcm_val

# 示例
gcd_result, lcm_result = find_gcd_and_lcm(x, y)
print(f"The GCD of {x} and {y} is {gcd_result}, and the LCM is {lcm_result}")
```

这段代码首先计算了两个数的最大公因数，然后用它来计算最小公倍数，并返回两者的结果。请确保输入的数值都是整数，因为这些操作对于浮点数可能会产生意外的结果。

------



## 检查字符串是否为数字

### isdigit（）

Python isdigit() 方法检测字符串是否只由数字组成。

**语法**

isdigit()方法语法：

```
str.isdigit()
```

**参数**

- 无。

**返回值**

如果字符串只包含数字则返回 True 否则返回 False。

**实例**

```python
\#!/usr/bin/python3

str = "123456";
**print** (str.isdigit())

str = "Runoob example....wow!!!"
**print** (str.isdigit())
```

以上实例输出结果如下：

```
True
False
```

==isdigit() 方法只对正整数有效，负数及小数均返回不正确。==

### 识别负数及小数

```python
# 判断是否为数字
def is_number(s):        
    try:    # 如果能运⾏ float(s) 语句，返回 True（字符串 s 是浮点数）                
        float(s)                
        return True        
    except ValueError:  # ValueError 为 Python 的⼀种标准异常，表⽰"传⼊⽆效的参数"             
        pass  # 如果引发了 ValueError 这种异常，不做任何事情（pass：不做任何事情，⼀般⽤做占位语句）
    try:                
        import unicodedata  # 处理 ASCII 码的包                
        unicodedata.numeric(s)  # 把⼀个表⽰数字的字符串转换为浮点数返回的函数                
        return True        
    except (TypeError, ValueError):                
        pass            
    	return False
    
print(is_number(1)) 
print(is_number(1.0)) 
print(is_number(0)) 
print(is_number(-2))
print(is_number(-2.0))
print(is_number("abc"))
```

输出结果为：

```
True
True
True
True
True
False
```

------

