def push(stack, element):
    stack.insert(0, element)
    print(element, "inserted into stack")

def pop(stack,element):
    if len(stack) == 0:
        print("stack is empty")
        return
    else:
        print(stack[0],"deleted successfully")
        stack.pop(0)

stack = []
for i in range(10):
    push(stack,i)
pop(stack, 5)