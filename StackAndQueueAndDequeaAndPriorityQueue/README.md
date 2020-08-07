# Stack、Queue、Deque and Priority Queue 

## Stack
   
- first in(push) last out(pop) (FILO)

- lookup:
O(n)

- insert:
O(1)

- delete:
O(1)



## Queue

- fist in first out

- lookup:
O(n)

- insert:
O(1)

- delete:
O(1)



## Deque: Double-End Queue

- double end in double end out

- lookup:
O(n)

- insert:
O(1)

- delete:
O(1)


## Priority Queue

- It's complex, can implement by heap、BST(binary search tree)、treap 

- lookup:
O(log n)

- insert:
O(1)

- delete:
O(1)


## Big O Complexity

- link: https://www.bigocheatsheet.com/

- Complexity:
    
    ![](../Data/Common%20Data%20Structure%20Operations%20complexity.png)




## Demo

### stack
```java
public class StackDemo {
    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<>();

        stack.push(1);
        stack.push(2);
        stack.push(3);
        stack.push(4);

        System.out.println(stack);
        System.out.println(stack.search(1));  // Returns the 1-based position where an object is on this stack.

        stack.pop();
        stack.pop();

        Integer top = stack.peek();  // Looks at the object at the top of this stack without removing it from the stack.
        System.out.println(top);
        System.out.println(stack);

    }
}

```


### Queue
```java
public class QueueDemo {
    public static void main(String[] args) {
        Queue<String> queue = new LinkedList<String>();

        queue.offer("one");
        queue.offer("two");
        queue.offer("three");
        queue.offer("four");

        System.out.println(queue);

        String polled = queue.poll();  // Retrieves and removes the head of this queue, or returns {@code null} if this queue is empty.
        System.out.println(polled);
        System.out.println(queue);

        String peek = queue.peek();  // Retrieves, but does not remove, the head of this queue
        System.out.println(peek);
        System.out.println(queue);

        while (queue.size() > 0){
            System.out.println(queue.poll());
        }
    }
}
```


### Deque
```java
public class DequeDemo {
    public static void main(String[] args) {
        Deque<String> deque = new LinkedList<String>();

        deque.offer("one");  // add to last
        deque.offerFirst("two");
        deque.offerLast("three");
        deque.offer("four");
        System.out.println(deque);

        String peek = deque.peek();  // peek to first
        String peekFirst = deque.peekFirst();
        String peekLast = deque.peekLast();
        System.out.println(peek);
        System.out.println(peekFirst);
        System.out.println(peekLast);
        System.out.println(deque);

        while (deque.size() > 0){
            System.out.println(deque.pop());  // pop the first
        }

        System.out.println(deque);
    }
}
```




## Code

### java Stack Class

- link: https://docs.oracle.com/en/java/javase/12/docs/api/java.base/java/util/Stack.html

- methods:

```java
boolean     empty()	            Tests if this stack is empty.

E	    peek()	            Looks at the object at the top of this stack without removing it from the stack.

E	    pop()	            Removes the object at the top of this stack and returns that object as the value of this function.

E	    push​(E item)	    Pushes an item onto the top of this stack.

int	    search​(Object o)	    Returns the 1-based position where an object is on this stack.
```


### java Stack Interface

- link: http://developer.classpath.org/doc/java/util/Stack-source.html

- push method
    
    ```java
    // pop
    public E push(E item) {
        addElement(item);

        return item;
    }
    
    // addElement
    public synchronized void addElement(E obj) {
        modCount++;
        ensureCapacityHelper(elementCount + 1);
        elementData[elementCount++] = obj;
    }  
    // ensureCapacityHelper
    private void ensureCapacityHelper(int minCapacity) {
        // overflow-conscious code
        if (minCapacity - elementData.length > 0)
            grow(minCapacity);
    }
  
    private static final int MAX_ARRAY_SIZE = Integer.MAX_VALUE - 8;
    // grow
    private void grow(int minCapacity) {
        // overflow-conscious code
        int oldCapacity = elementData.length;
        int newCapacity = oldCapacity + ((capacityIncrement > 0) ?
                                         capacityIncrement : oldCapacity);
        if (newCapacity - minCapacity < 0)
            newCapacity = minCapacity;
        if (newCapacity - MAX_ARRAY_SIZE > 0)
            newCapacity = hugeCapacity(minCapacity);
        elementData = Arrays.copyOf(elementData, newCapacity);
    }
    // hugeCapacity
    private static int hugeCapacity(int minCapacity) {
        if (minCapacity < 0) // overflow
            throw new OutOfMemoryError();
        return (minCapacity > MAX_ARRAY_SIZE) ?
            Integer.MAX_VALUE :
            MAX_ARRAY_SIZE;
    }
  
    // copyOf
    public static <T> T[] copyOf(T[] original, int newLength) {
        return (T[]) copyOf(original, newLength, original.getClass());
    }
    public static <T,U> T[] copyOf(U[] original, int newLength, Class<? extends T[]> newType) {
        @SuppressWarnings("unchecked")
        T[] copy = ((Object)newType == (Object)Object[].class)
            ? (T[]) new Object[newLength]
            : (T[]) Array.newInstance(newType.getComponentType(), newLength);
        System.arraycopy(original, 0, copy, 0,
                         Math.min(original.length, newLength));
        return copy;
    }
  
  ```

- pop method
    
    ```java
    public synchronized E pop() {
        E       obj;
        int     len = size();

        obj = peek();
        removeElementAt(len - 1);

        return obj;
    }
  
    // size
    public synchronized int size() {
        return elementCount;
    }
    
    // peek
    public synchronized E peek() {
        int     len = size();

        if (len == 0)
            throw new EmptyStackException();
        return elementAt(len - 1);
    }
    
    //  removeElementAt
    public synchronized void removeElementAt(int index) {
        modCount++;
        if (index >= elementCount) {
            throw new ArrayIndexOutOfBoundsException(index + " >= " +
                                                     elementCount);
        }
        else if (index < 0) {
            throw new ArrayIndexOutOfBoundsException(index);
        }
        int j = elementCount - index - 1;
        if (j > 0) {
            System.arraycopy(elementData, index + 1, elementData, index, j);
        }
        elementCount--;
        elementData[elementCount] = null; /* to let gc do its work */
    }
      
    // arraycopy
    public static native void arraycopy(Object src,  int  srcPos,
                                        Object dest, int destPos,
                                        int length);
    ```




### java Queue Interface

- link: https://docs.oracle.com/en/java/javase/12/docs/api/java.base/java/util/Queue.html
- link: http://fuseyism.com/classpath/doc/java/util/Queue-source.html

- Implementing Classes:

        AbstractQueue, ArrayBlockingQueue, ArrayDeque, ConcurrentLinkedDeque, 
        ConcurrentLinkedQueue, DelayQueue, LinkedBlockingDeque, LinkedBlockingQueue, 
        LinkedList, LinkedTransferQueue, PriorityBlockingQueue, PriorityQueue, 
        SynchronousQueue

- methods:
```java
	    Throws exception	Returns special value
Insert	    add(e)	        offer(e)
Remove	    remove()	        poll()
Examine	    element()	        peek()

---------------------------------------------------------------
boolean	add​(E e)	Inserts the specified element into this queue if it is possible to do 
                        so immediately without violating capacity restrictions, returning true 
                        upon success and throwing an IllegalStateException if no space is currently available.

E	element()	Retrieves, but does not remove, the head of this queue.

boolean	offer​(E e)	Inserts the specified element into this queue if it is possible to do 
                        so immediately without violating capacity restrictions.

E	peek()	        Retrieves, but does not remove, the head of this queue, or returns null if this queue is empty.

E	poll()	        Retrieves and removes the head of this queue, or returns null if this queue is empty.

E	remove()	Retrieves and removes the head of this queue.
```



### java Deque Interface

- link: https://docs.oracle.com/en/java/javase/12/docs/api/java.base/java/util/Deque.html

- Implementing Classes:

      ArrayDeque, ConcurrentLinkedDeque, LinkedBlockingDeque, LinkedList

- methods:
```java
	First Element (Head)	                Last Element (Tail)
        Throws  exception	Special value	Throws exceptio     Special value
Insert	addFirst(e)	        offerFirst(e)	addLast(e)	    offerLast(e)
Remove	removeFirst()	        pollFirst()	removeLast()	    pollLast()
Examine	getFirst()	        peekFirst()	getLast()	    peekLast()

---------------------------------------------------------------
boolean	add​(E e)	Inserts the specified element into the queue represented by this deque (in other words, at the tail of this deque) if it is possible to do so immediately without violating capacity restrictions, returning true upon success and throwing an IllegalStateException if no space is currently available.
boolean	addAll​(Collection<? extends E> c)	Adds all of the elements in the specified collection at the end of this deque, as if by calling addLast(E) on each one, in the order that they are returned by the collection's iterator.
void	addFirst​(E e)	Inserts the specified element at the front of this deque if it is possible to do so immediately without violating capacity restrictions, throwing an IllegalStateException if no space is currently available.
void	addLast​(E e)	Inserts the specified element at the end of this deque if it is possible to do so immediately without violating capacity restrictions, throwing an IllegalStateException if no space is currently available.
boolean	contains​(Object o)	Returns true if this deque contains the specified element.
Iterator<E>	descendingIterator()	Returns an iterator over the elements in this deque in reverse sequential order.
E	element()	Retrieves, but does not remove, the head of the queue represented by this deque (in other words, the first element of this deque).
E	getFirst()	Retrieves, but does not remove, the first element of this deque.
E	getLast()	Retrieves, but does not remove, the last element of this deque.
Iterator<E>	iterator()	Returns an iterator over the elements in this deque in proper sequence.
boolean	offer​(E e)	Inserts the specified element into the queue represented by this deque (in other words, at the tail of this deque) if it is possible to do so immediately without violating capacity restrictions, returning true upon success and false if no space is currently available.
boolean	offerFirst​(E e)	Inserts the specified element at the front of this deque unless it would violate capacity restrictions.
boolean	offerLast​(E e)	Inserts the specified element at the end of this deque unless it would violate capacity restrictions.
E	peek()	Retrieves, but does not remove, the head of the queue represented by this deque (in other words, the first element of this deque), or returns null if this deque is empty.
E	peekFirst()	Retrieves, but does not remove, the first element of this deque, or returns null if this deque is empty.
E	peekLast()	Retrieves, but does not remove, the last element of this deque, or returns null if this deque is empty.
E	poll()	Retrieves and removes the head of the queue represented by this deque (in other words, the first element of this deque), or returns null if this deque is empty.
E	pollFirst()	Retrieves and removes the first element of this deque, or returns null if this deque is empty.
E	pollLast()	Retrieves and removes the last element of this deque, or returns null if this deque is empty.
E	pop()	Pops an element from the stack represented by this deque.
void	push​(E e)	Pushes an element onto the stack represented by this deque (in other words, at the head of this deque) if it is possible to do so immediately without violating capacity restrictions, throwing an IllegalStateException if no space is currently available.
E	remove()	Retrieves and removes the head of the queue represented by this deque (in other words, the first element of this deque).
boolean	remove​(Object o)	Removes the first occurrence of the specified element from this deque.
E	removeFirst()	Retrieves and removes the first element of this deque.
boolean	removeFirstOccurrence​(Object o)	Removes the first occurrence of the specified element from this deque.
E	removeLast()	Retrieves and removes the last element of this deque.
boolean	removeLastOccurrence​(Object o)	Removes the last occurrence of the specified element from this deque.
int	size()	Returns the number of elements in this deque.
```


### java Priority Class

- link: https://docs.oracle.com/en/java/javase/12/docs/api/java.base/java/util/PriorityQueue.html


### python heapq

- link: https://docs.python.org/2/library/heapq.html

- link: https://docs.python.org/3/library/heapq.html

### python collections: deque

- link: https://docs.python.org/2/library/collections.html#deque-objects

- link: https://docs.python.org/3/library/collections.html




