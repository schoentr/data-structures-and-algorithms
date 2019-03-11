from stacks_and_queues import Stack, Node

class Queue():
    def __init__(self):
    input = Stack()
    output = Stack()

    def enqueue(self,value):
        self.stack_in.push(value)
       
    def dequeue(self):
        if output.peek() is not None:
            return output.pop()
        if input.peek() is not None:
            while input.peek()is not None:
                output.push(input.pop())
            return output.pop()
        return None



        # print('top-in',self.stack_in.top.value)
        # self.front= self.stack_in.top.value
        # curr = self.stack_in.top
        
        # print(curr.value, curr._next.value)
        # self.stack_out.push(curr.value)
        # array_values=[]
        # while curr:
        #     array_values.append(curr.value)
        #     curr = curr._next
        #     print(curr.value, curr._next.value)
        #     self.stack_out.push(curr.value)
        # print(array_values)
        # print('serrr',self.stack_out.top.value)
            # i+=1
            # curr = curr._next
            # curr._next = None
            # temp_value = self.stack_in.pop()
            # self.stack_out.push(temp_value)
            # # curr=self.stack_out.top
            # print('stack_out-top',self.stack_out.top.value,i)
            # print('stack_out_front')
        # exit_value =self.stack_in.pop()
        # curr=self.stack_out.top
        # while curr._next    :
        #     temp_value = self.stack_out.pop()
        #     self.stack_in.push(temp_value)
        #     curr=curr._next
        #     # print(curr.value)
        # return exit_value
    
    # def peek(self):
    #     return self.front.value

