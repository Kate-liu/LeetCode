# Binary Search


## 二分查找的前提
- 目标函数单调性（单调递增或者递减）

- 存在上下界（bounded）

- 能够通过索引访问（index accessible）


## 代码模板

- link: https://shimo.im/docs/hjQqRQkGgwd9g36J/read

- python code:
```python
left, right = 0, len(array) - 1

while left <= right:
    mid = (left + right) / 2
    if array[mid] == target
        # find the target
        break or return result
    elif array[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```


- java code:
```java
public int binarySearch(int[] array, int target) {
    int left = 0, right = array.length - 1, mid;

    while (left <= right) {
        mid = (right - left) / 2 + left;

        if (array[mid] == target) {
            return mid;
        } else if (array[mid] > target) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    
    return -1;
}
```

