from stacks_and_queues.stacks_and_queues import Stack, Node


class Queue():
    def __init__(self):
        self.input_stack = Stack()
        self.output = Stack()
       
    

    def enqueue(self, value):
        self.input_stack.push(value)

    def dequeue(self):
        if self.output.peek() is not None:
            return output.pop()
        if self.input_stack.peek() is not None:
            while self.input_stack.peek()is not None:
                self.output.push(self.input_stack.pop())
            return self.output.pop()
        return None
