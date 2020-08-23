# Recursion

- 递归-循环
    - 通过函数体来进行的循环


- 向下进入不同的层，向上又回到原来的一层

- 思维要点
    - 不要人肉递归

    - 找最近重复子问题
    
    - 数学归纳法的思维


## Recursion Template

- link: https://shimo.im/docs/DjqqGCT3xqDYwPyY/read

```python
def recursion(level, param1, param2, ...):
    # recursion terminator
    if level > MAX_LEVEL:
        # process_result
        return
    
    # process logic in current level
    process(level, data, ...)

    # drill down
    self.recorsion(level + 1, param1, param2, ...)

    # reverse the current level status if needed 
```


```java
public void recursion(int level, int param) {
    // terminator
    if (level > MAX_LEVEL) {
        // process result
        return;
    }

    // process current logic
    process(level, param)

    // drill dowm
    recur(level: level+1, newParam)
    
    // restore current status

}
```


