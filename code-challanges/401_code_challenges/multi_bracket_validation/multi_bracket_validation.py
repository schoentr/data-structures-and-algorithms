from stacks_and_queues.stacks_and_queues import Stack



def bracket_validation(input):
    letters= []
    s = Stack()
    for x in input:
        if x is '{' or x is '(' or x is '[':
            s.push(x)
        if x is '}':
            temp=s.peek()
            if temp is '{':
                s.pop()
            else:
                return False    
        if x is ']':
            # return True
            temp=s.peek()
            if temp is '[':
                s.pop()
            else:
                return False
        if x is ')':
            temp=s.peek()
            if temp is '(':
                s.pop()
            else:
                return False
    if s.peek() is None:
        return True
    else:
        return False