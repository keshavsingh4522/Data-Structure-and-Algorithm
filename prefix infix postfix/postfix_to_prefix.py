'''

Algorith:

- Read the Postfix expression from left to right
- If the symbol is an operand, then push it onto the Stack
- If the symbol is an operator, then pop two operands from the Stack
- Create a string by concatenating the two operands and the operator before them.
- string = operator + operand2 + operand1
- And push the resultant string back to Stack
- Repeat the above steps until end of Prefix expression.

'''
postfix=input("Enter Postfix Expression: ")

operators='+-*/^%'
stack=[]

for i in postfix:
    if i in operators:
        x1=stack.pop()
        x2=stack.pop()
        stack.append(i+x2+x1)
    else:
        stack.append(i)
print(f"Prefix Operation is: ",*stack)
