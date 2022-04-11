#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
class Conversion:
    def __init__(self):
        self.top = -1
        self.array = []
        
        self.output = []
        self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
    
    def isEmpty(self):
        return True if self.top == -1 else False
    
    def peek(self):
        return self.array[-1]
    
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"
    def push(self, op):
        self.top += 1
        self.array.append(op)

    def isOperand(self, ch):
        return ch.isalpha()
    
    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a <= b else False
        except KeyError:
            return False
        
    def infixToPostfix(self, exp):
        for i in exp:
            if self.isOperand(i):
                self.output.append(i)
            elif i == '(':
                self.push(i)
            elif i == ')':
                while( (not self.isEmpty()) and self.peek() != '('):
                    a = self.pop()
                    self.output.append(a)
                if (not self.isEmpty() and self.peek() != '('):
                    return -1
                else:
                    self.pop()
            else:
                while(not self.isEmpty() and self.notGreater(i)):
                    self.output.append(self.pop())
                self.push(i)
        while not self.isEmpty():
            self.output.append(self.pop())

        output.set("".join(self.output))
    
    
    # infix to prefix.
    
    def isOperator(self,c):
        return (not (c >= 'a' and c <= 'z') and not(c >= '0' and c <= '9') and not(c >= 'A' and c <= 'Z'))
    def getPriority(self,C):
        if (C == '-' or C == '+'):
            return 1
        elif (C == '*' or C == '/'):
            return 2
        elif (C == '^'):
            return 3
        return 0
    def infixToPrefix(self,infix):
        operators = []
        operands = []
        for i in range(len(infix)):
            if (infix[i] == '('):
                operators.append(infix[i])
            elif (infix[i] == ')'):
                while (len(operators)!=0 and operators[-1] != '('):
                    op1 = operands[-1]
                    operands.pop()
                    op2 = operands[-1]
                    operands.pop()
                    op = operators[-1]
                    operators.pop()
                    tmp = op + op2 + op1
                    operands.append(tmp)
                operators.pop()
            elif (not self.isOperator(infix[i])):
                operands.append(infix[i] + "")
            else:
                while (len(operators)!=0 and self.getPriority(infix[i]) <= self.getPriority(operators[-1])):
                    op1 = operands[-1]
                    operands.pop()
                    op2 = operands[-1]
                    operands.pop()
                    op = operators[-1]
                    operators.pop()
                    tmp = op + op2 + op1
                    operands.append(tmp)
                operators.append(infix[i])
        while (len(operators)!=0):
            op1 = operands[-1]
            operands.pop()
            op2 = operands[-1]
            operands.pop()
            op = operators[-1]
            operators.pop()
            tmp = op + op2 + op1
            operands.append(tmp)
        for i in range(len(operands)):
            self.output.append(operands[i])
        #return operands[-1]
        
        output.set("".join(self.output))
    
    
    def click(event):
        global output
        global exp
        text= event.widget.cget("text")
        if text=="C":
            output.set("")
            screen.update()
        elif text=="postfix":
            c=Conversion()
            c.infixToPostfix(output.get())
        elif text=="prefix":
            c=Conversion()
            c.infixToPrefix(output.get())
        else:
            output.set(output.get() + text)
            screen.update()



root =Tk()
root.geometry("550x480")
root.minsize(650,550)
root.maxsize(650,550)
root.title("InfixToPostfixPrefixConversion")

output= StringVar()
output.set("")
screen= Entry(root,textvar=output,font="lucida 20 bold")
screen.pack(fill=X,ipadx=7,pady=5,padx=12)

f=Frame(root,bg="cadetblue")
b=Button(f,text="9", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>", Conversion.click)
b=Button(f,text="8", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>", Conversion.click)
b=Button(f,text="7", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>", Conversion.click)
b=Button(f,text="C", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>", Conversion.click)
b=Button(f,text="(", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>", Conversion.click)
b=Button(f,text="a", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>", Conversion.click)
b=Button(f,text="b", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>", Conversion.click)
b=Button(f,text="c", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>", Conversion.click)
b=Button(f,text="d", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>", Conversion.click)
b=Button(f,text="e", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>", Conversion.click)
f.pack()

f=Frame(root,bg="cadetblue")
b=Button(f,text="6", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=9,pady=7)
b.bind("<Button-1>", Conversion.click)
b=Button(f,text="5", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=9,pady=7)
b.bind("<Button-1>", Conversion.click)
b=Button(f,text="4", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=9,pady=7)
b.bind("<Button-1>", Conversion.click)
b=Button(f,text="/", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>", Conversion.click)
b=Button(f,text=")", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>", Conversion.click)
b=Button(f,text="f", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>", Conversion.click)
b=Button(f,text="g", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>", Conversion.click)
b=Button(f,text="h", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>", Conversion.click)
b=Button(f,text="i", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>", Conversion.click)
b=Button(f,text="j", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>", Conversion.click)
f.pack()

f=Frame(root,bg="cadetblue")
b=Button(f,text="3", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=11,pady=7)
b.bind("<Button-1>", Conversion.click)
b=Button(f,text="2", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=9,pady=7)
b.bind("<Button-1>", Conversion.click)
b=Button(f,text="1", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=9,pady=7)
b.bind("<Button-1>", Conversion.click)
b=Button(f,text="*", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>", Conversion.click)
b=Button(f,text="{", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>", Conversion.click)
b=Button(f,text="k", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>", Conversion.click)
b=Button(f,text="l", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>", Conversion.click)
b=Button(f,text="m", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>", Conversion.click)
b=Button(f,text="n", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>", Conversion.click)
b=Button(f,text="o", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>", Conversion.click)
f.pack()

f=Frame(root,bg="cadetblue")
b=Button(f,text="0", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>", Conversion.click)
b=Button(f,text="00", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>", Conversion.click)
b=Button(f,text="=", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")###############
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>", Conversion.click)
b=Button(f,text="-", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>", Conversion.click)
b=Button(f,text="}", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>", Conversion.click)

b=Button(f,text="p", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>", Conversion.click)
b=Button(f,text="q", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>", Conversion.click)
b=Button(f,text="r", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=7,pady=7)

b.bind("<Button-1>", Conversion.click)
b=Button(f,text="s", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>", Conversion.click)
b=Button(f,text="t", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>", Conversion.click)
f.pack()

f=Frame(root,bg="cadetblue")
b=Button(f,text="+", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>", Conversion.click)
b=Button(f,text="^", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>", Conversion.click)
b=Button(f,text="[", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>", Conversion.click)
b=Button(f,text="]", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>", Conversion.click)
b=Button(f,text="u", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>", Conversion.click)
b=Button(f,text="v", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>", Conversion.click)
b=Button(f,text="w", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>", Conversion.click)
b=Button(f,text="x", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>", Conversion.click)
b.bind("<Button-1>", Conversion.click)
b=Button(f,text="y", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=7,pady=7)
b.bind("<Button-1>", Conversion.click)
b=Button(f,text="z", bg="cadetblue",fg="yellow", activebackground="cadetblue", activeforeground="yellow",font="lucida 20 bold")
b.pack(side=LEFT,padx=7,pady=7)
f.pack()


f=Frame(root,bg="aliceblue")

b=Button(f,text="postfix", bg="cadetblue",fg="yellow", activebackground="yellow", activeforeground="cadetblue",font="lucida 20 bold")
b.pack(side=LEFT,padx=53,pady=20)
b.bind("<Button-1>", Conversion.click)
b=Button(f,text="prefix", bg="cadetblue",fg="yellow", activebackground="yellow", activeforeground="cadetblue",font="lucida 20 bold")
b.pack(side=LEFT,padx=53,pady=20)
b.bind("<Button-1>", Conversion.click)

f.pack()

root.mainloop()


# In[ ]:




