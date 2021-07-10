import tkinter as tk
app=tk.Tk()
app.title('Calculator')
app.geometry('350x450')
expr=''

result=tk.Variable(app)
result.set('')
tk.Label(app,textvariable=result,bg='white',width='35',height='4').place(x=50,y=50)

def operate(num):
    global expr
    expr = expr + str(num)
    result.set(expr)

def clear():
    global expr
    expr=''
    result.set(expr)

def equal():
    global expr
    result.set(eval(expr))
    expr=''


tk.Button(app,text='1',width='5',height='2',command=lambda:operate('1')).place(x=50,y=200)
tk.Button(app,text='2',width='5',height='2',command=lambda:operate('2')).place(x=120,y=200)
tk.Button(app,text='3',width='5',height='2',command=lambda:operate('3')).place(x=190,y=200)
tk.Button(app,text='4',width='5',height='2',command=lambda:operate('4')).place(x=50,y=250)
tk.Button(app,text='5',width='5',height='2',command=lambda:operate('5')).place(x=120,y=250)
tk.Button(app,text='6',width='5',height='2',command=lambda:operate('6')).place(x=190,y=250)
tk.Button(app,text='7',width='5',height='2',command=lambda:operate('7')).place(x=50,y=300)
tk.Button(app,text='8',width='5',height='2',command=lambda:operate('8')).place(x=120,y=300)
tk.Button(app,text='9',width='5',height='2',command=lambda:operate('9')).place(x=190,y=300)
tk.Button(app,text='0',width='5',height='2',command=lambda:operate('0')).place(x=120,y=350)
tk.Button(app,text='=',width='5',height='2',command=lambda:equal()).place(x=190,y=350)
tk.Button(app,text='.',width='5',height='2',command=lambda:operate('.')).place(x=50,y=350)
tk.Button(app,text='+',width='5',height='2',command=lambda:operate('+')).place(x=260,y=200)
tk.Button(app,text='-',width='5',height='2',command=lambda:operate('-')).place(x=260,y=250)
tk.Button(app,text='x',width='5',height='2',command=lambda:operate('*')).place(x=260,y=300)
tk.Button(app,text='/',width='5',height='2',command=lambda:operate('/')).place(x=260,y=350)
tk.Button(app,text='CLR',width='10',height='2',command=lambda:clear()).place(x=50,y=150)

app.mainloop()
