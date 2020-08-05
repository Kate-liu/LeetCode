# Time and Space Complexity analyse


## c

- O(1): Constant Complexity （常数复杂度）

- O(log n): Logarithmic Complexity (对数时间复杂度)

- O(n): Linear Complexity (线性时间复杂度)

- O(n^2): N square Complexity (平方时间复杂度)

- O(n^3): N cubic Complexity (立方时间复杂度)

- O(2^n): Exponential Growth (指数时间复杂度)

- O(n!): Factorial (阶乘时间复杂度)

![](./Data/Big%20O%20notation.jpeg)


### O(1): Constant Complexity （常数复杂度）

```java
public class TestDemo {
    public static void main(String[] args) {
        int a = 1;
        System.out.println("O(1): Constant Complexity ->" + a);
    }
}
```


### O(log n): Logarithmic Complexity (对数时间复杂度)

```java
public class TestDemo {
    public static void main(String[] args) {
        int n = 10000;
        for (int i = 1; i < n; i *= 2) {
            System.out.println("O(log n): Logarithmic Complexity ->" + i);
        }
    }
}


```

### O(n): Linear Complexity (线性时间复杂度)

```java
public class TestDemo {
    public static void main(String[] args) {
        int n = 10000;
        for (int i =1; i < n; i++) {
            System.out.println("O(n): Linear Complexity ->" + i);
        }
    }
}

```

### O(n^2): N square Complexity (平方时间复杂度)

```java
public class TestDemo {
    public static void main(String[] args) {
        int n = 10000;
        for (int i = 1; i < n; i++) {
            for (int j = 1; j < n; j++) {
                System.out.println("O(n^2): N square Complexity ->" + i + "and" + j);
            }
        }
    }
}
```


### O(n^3): N cubic Complexity (立方时间复杂度)

```java
public class TestDemo {
    public static void main(String[] args) {
        int n = 10000;
        for (int i = 1; i < n; i++) {
            for (int j = 1; j < n; j++) {
                for (int k = 1; k < n; k++) {
                    System.out.println("O(n^3): N cubic Complexity ->" + i + "and" + j + "and" + k);
                }
            }
        }
    }
}
```


### O(2^n): Exponential Growth (指数时间复杂度)

```java
public class TestDemo {
    public static void main(String[] args) {
        TestDemo testDemo = new TestDemo();
        int result = testDemo.fib(9);
        System.out.println("O(2^n): Exponential Growth ->" + result);
    }

    public int fib(int n) {
        if (n < 2) {
            return n;
        }
        return fib(n - 1) + fib(n - 2);
    }
}

```




## Master Theorem

- link: [Master_theorem_(analysis_of_algorithms)](https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms))

- link: [主定理](https://zh.wikipedia.org/wiki/%E4%B8%BB%E5%AE%9A%E7%90%86)


### Consider

- 二叉树遍历-前序、中序、后序：时间复杂度是多少？
answer：O(n)

- 图的遍历：时间复杂度是多少？
answer：O(n)

- 搜索算法：DFS、BFS时间复杂度是多少？
answer：O(n)

- 二分查找复杂度是多少？
answer：O(log n)



## Space Complexity

- Array list (1D, 2D, ...)

- Recursion depth 



## Reference

- link: [如何理解算法时间复杂度的表示法，例如 O(n²)、O(n)、O(1)、O(nlogn) 等？](https://www.zhihu.com/question/21387264)




