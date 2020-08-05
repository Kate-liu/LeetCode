# Array、Linked and Skip List


## Array List

- lookup:
O(1)

- insert:
O(n)

- delete:
O(n)

- prepend:
O(1)

- append:
O(1)



## Linked List

- lookup:
O(n)

- insert:
O(1)

- delete:
O(1)

- prepend:
O(1)

- append:
O(1)



## Skip List

- lookup:
O(log n)

- insert:
O(log n)
 
- delete:
O(log n)

- prepend:
O(1)

- append:
O(1)

- space complexity: 
O(n)



## Code

### java ArrayList add method code

- link: [ArrayList-source](http://developer.classpath.org/doc/java/util/ArrayList-source.html)

- Appends the specified element to the end of this list. 

```java
public void add(int index, E element) {
    rangeCheckForAdd(index);

    ensureCapacityInternal(size + 1);  // Increments modCount!!
    System.arraycopy(elementData, index, elementData, index + 1,
                     size - index);
    elementData[index] = element;
    size++;
}
```


- Inserts the specified element at the specified position in this list.

```java
public void add(int index, E element) {
    rangeCheckForAdd(index);

    ensureCapacityInternal(size + 1);  // Increments modCount!!
    System.arraycopy(elementData, index, elementData, index + 1,
                     size - index);
    elementData[index] = element;
    size++;
}
```

- ensureCapacityInternal

```java
private void ensureCapacityInternal(int minCapacity) {
    ensureExplicitCapacity(calculateCapacity(elementData, minCapacity));
}

private static int calculateCapacity(Object[] elementData, int minCapacity) {
    if (elementData == DEFAULTCAPACITY_EMPTY_ELEMENTDATA) {
        return Math.max(DEFAULT_CAPACITY, minCapacity);
    }
    return minCapacity;
}

private void ensureExplicitCapacity(int minCapacity) {
    modCount++;

    // overflow-conscious code
    if (minCapacity - elementData.length > 0)
        grow(minCapacity);
}

private static final int MAX_ARRAY_SIZE = Integer.MAX_VALUE - 8;

private void grow(int minCapacity) {
    // overflow-conscious code
    int oldCapacity = elementData.length;
    int newCapacity = oldCapacity + (oldCapacity >> 1);
    if (newCapacity - minCapacity < 0)
        newCapacity = minCapacity;
    if (newCapacity - MAX_ARRAY_SIZE > 0)
        newCapacity = hugeCapacity(minCapacity);
    // minCapacity is usually close to size, so this is a win:
    elementData = Arrays.copyOf(elementData, newCapacity);
}
```




### java Linked List Node Class

- link: [Implementing a Linked List in Java using Class](https://www.geeksforgeeks.org/implementing-a-linked-list-in-java-using-class/)

- link: [LinkedList](http://www.cs.cmu.edu/~adamchik/15-121/lectures/Linked%20Lists/code/LinkedList.java)

- Node class (1)
```java
class LinkedList { 
    Node head; // head of list 
  
    /* Linked list Node*/
    class Node { 
        int data; 
        Node next; 
  
        // Constructor to create a new node 
        // Next is by default initialized 
        // as null 
        Node(int d) { data = d; } 
    } 
}
```

- Node class (2)
```java
/*******************************************************
 *
 *  The Node class
 *
 ********************************************************/
private static class Node<AnyType> {
    private AnyType data;
    private Node<AnyType> next;
    
    public Node(AnyType data, Node<AnyType> next) {
        this.data = data;
        this.next = next;
    }
}

```



### java Linked List 

- link: [LinkedList-source](http://developer.classpath.org/doc/java/util/LinkedList-source.html)

- Node class
```java
private static class Node<E> {
    E item;
    Node<E> next;
    Node<E> prev;

    Node(Node<E> prev, E element, Node<E> next) {
        this.item = element;
        this.next = next;
        this.prev = prev;
    }
}
```

- head and tail pointer
```java
/**
 * Pointer to first node.
 * Invariant: (first == null && last == null) ||
 *            (first.prev == null && first.item != null)
 */
transient Node<E> first;

/**
 * Pointer to last node.
 * Invariant: (first == null && last == null) ||
 *            (last.next == null && last.item != null)
 */
transient Node<E> last;
```

### Skip List

- link: [跳跃表](https://redisbook.readthedocs.io/en/latest/internal-datastruct/skiplist.html)

- link: [为啥 redis 使用跳表(skiplist)而不是使用 red-black？](https://www.zhihu.com/question/20202931)



