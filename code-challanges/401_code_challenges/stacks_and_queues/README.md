# Stacks and Queues


## Challenge
 Problem Domain: To create a Stack and a Queue, be able to add/push && remove/pop values (nodes) to the Stack as well as peek which will return the value of the node at the top of the Stack.  Create a Queue class that has a top property. It creates an empty queue when instantiated.  This object should be aware of a default empty value assigned to front when the queue is created. Define a method called enqueue which takes any value as an argument and adds a new node with that value to the back of the queue with an O(1) Time performance. Define a method called dequeue that does not take any argument, removes the node from the front of the queue, and returns the node’s value. Define a method called peek that does not take an argument and returns the value of the node located in the front of the stack.

## Approach & Efficiency
 Using TDD (Test Driven Development) I created tests:
 - [x] Can successfully push onto a stack
 - [x] Can successfully push multiple nodes onto a stack
- [x] Can successfully pop off the stack
- [x] Can successfully empty a stack after multiple pops.
- [x] Can successfully peek the next item on the stack.
- [x] Can successfully instantiate an empty stack
- [x] Can successfully enqueue onto a queue
- [x] Can successfully enqueue multiple items into a queue
- [x] Can successfully dequeue off of a queue the expected value
- [x] Can successfully peek into a queue, seeing the expected value
- [x] Can successfully empty a queue after multiple dequeues
- [x] Can successfully instantiate an empty queue
- [x] Mantained a O(1) time proformance for all tasks

