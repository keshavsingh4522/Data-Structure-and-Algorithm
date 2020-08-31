'''

Algorith:

1.While there are input symbol left
…1.1 Read the next symbol from the input.
2.If the symbol is an operand
…2.1 Push it onto the stack.
3.Otherwise,
…3.1 the symbol is an operator.
…3.2 Pop the top 2 values from the stack.
…3.3 Put the operator, with the values as arguments and form a string.
…3.4 Push the resulted string back to stack.
4.If there is only one value in the stack
…4.1 That value in the stack is the desired infix string.

'''
postfix=input('Enter Postfix Expression : ')
stack=[]
operators='/*-+^%'
for i in postfix:
    if i in operators:
        x1=stack.pop()
        x2=stack.pop()
        stack.append(x2+i+x1)
    else:
        stack.append(i)
print("Infix Expression is : ",*stack)
