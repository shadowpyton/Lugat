from tkinter import *
def btnClick(item) :
    tmp = str(text_input.get())
    text_input.set(tmp+item)

def btnClear():
    text_input.set('')
def btnEq():
    tmp = str(text_input.get())
    s = eval(tmp)
    text_input.set(s)

root = Tk()
text_input = StringVar()

textDisplay = Entry(root, font=('arial', 20, 'bold'), bg="#ff830b", bd=10, justify="right",width=25,
                   textvariable=text_input) .grid(row=0, columnspan=5)

btn7 = Button(root,font= ('arial', 20, 'bold'), width=4, text='7', fg="#ff830b", bg="black", command = lambda:btnClick('7')).grid(row=1, column=0)
btn8 = Button(root,font= ('arial', 20, 'bold'), width=4, text='8', fg="#ff830b", bg="black", command = lambda:btnClick('8')).grid(row=1, column=1)
btn9 = Button(root,font= ('arial', 20, 'bold'), width=4, text='9', fg="#ff830b", bg="black", command = lambda:btnClick('9')).grid(row=1, column=2)
pilus = Button(root,font= ('arial', 20, 'bold'), width=4, text='+', fg="#ff830b", bg="black", command = lambda:btnClick('+')).grid(row=1, column=3)
c = Button(root,font= ('arial', 20, 'bold'), width=4, text='C', fg="#ff830b", bg="black", command = lambda:btnClear()).grid(row=1, column=4)

btn4 = Button(root,font= ('arial', 20, 'bold'), width=4, text='4', fg="#ff830b", bg="black", command = lambda:btnClick('4')).grid(row=2, column=0)
btn5 = Button(root,font= ('arial', 20, 'bold'), width=4, text='5', fg="#ff830b", bg="black", command = lambda:btnClick('5')).grid(row=2, column=1)
btn6 = Button(root,font= ('arial', 20, 'bold'), width=4, text='6', fg="#ff830b", bg="black", command = lambda:btnClick('6')).grid(row=2, column=2)
minus = Button(root,font= ('arial', 20, 'bold'), width=4, text='-', fg="#ff830b", bg="black", command = lambda:btnClick('-')).grid(row=2, column=3)
btn = Button(root,font= ('arial', 20, 'bold'), width=4, text='!', fg="#ff830b", bg="black", command = lambda:btnClick('!')).grid(row=2, column=4)

btn1 = Button(root,font= ('arial', 20, 'bold'), width=4, text='1', fg="#ff830b", bg="black", command = lambda:btnClick('1')).grid(row=3, column=0)
btn2 = Button(root,font= ('arial', 20, 'bold'), width=4, text='2', fg="#ff830b", bg="black", command = lambda:btnClick('2')).grid(row=3, column=1)
btn3 = Button(root,font= ('arial', 20, 'bold'), width=4, text='3', fg="#ff830b", bg="black", command = lambda:btnClick('3')).grid(row=3, column=2)
mult = Button(root,font= ('arial', 20, 'bold'), width=4, text='*', fg="#ff830b", bg="black", command = lambda:btnClick('*')).grid(row=3, column=3)
div = Button(root,font= ('arial', 20, 'bold'), width=4, text='/', fg="#ff830b", bg="black", command = lambda:btnClick('/')).grid(row=3, column=4)

point = Button(root,font= ('arial', 20, 'bold'), width=4, text='.', fg="#ff830b", bg="black", command = lambda:btnClick('.')).grid(row=4, column=0)
btn0 = Button(root,font= ('arial', 20, 'bold'), width=4, text='0', fg="#ff830b", bg="black", command = lambda:btnClick('0')).grid(row=4, column=1)
qav1 = Button(root,font= ('arial', 20, 'bold'), width=4, text='(', fg="#ff830b", bg="black", command = lambda:btnClick('(')).grid(row=4, column=2)
qav2 = Button(root,font= ('arial', 20, 'bold'), width=4, text=')', fg="#ff830b", bg="black", command = lambda:btnClick(')')).grid(row=4, column=3)
btn = Button(root,font= ('arial', 20, 'bold'), width=4, text='=', fg="#ff830b", bg="black", command = lambda:btnEq()).grid(row=4, column=4)

root.mainloop()