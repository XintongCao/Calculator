from tkinter import *
# instantiating an object - calculator
calculator=Tk()
# define the title of the pop-up interface
calculator.title('<CALCULATOR>')
# define a label to explain how to use this calculator
Label(calculator,\
      text='Please enter the numbers in the first two input boxes and select a operator symbol.\
            \nClick on \'ENTER\' button to calculate the results. Click on the \'EXIT\' button to exit the calculator.',\
      justify=CENTER)\
      .pack(padx=10,pady=10)
# set the frame of the pop-up interface
calc_frame=Frame(calculator)
calc_frame.pack(padx=10,pady=10)
# define input text variables
var1=StringVar()
var2=StringVar()
var3=StringVar()
# define a function, to validate if the input text is numbers
def test(content):
    return content.isdigit()
# calling the register() to validate the test() function
testCMD=calculator.register(test)
# define labels for entering numeric text
Label(calc_frame,text='Enter a number:').grid(row=1,column=0)
Label(calc_frame,text='Enter a number:').grid(row=1,column=2)
Label(calc_frame,text='Result:').grid(row=1,column=4)
# setting the input boxes
num1=Entry(calc_frame,width=10,textvariable=var1,\
           validate='key',validatecommand=(testCMD,'%P'))\
           .grid(row=2,column=0)
num2=Entry(calc_frame,width=10,textvariable=var2,\
           validate='key',validatecommand=(testCMD,'%P'))\
           .grid(row=2,column=2)
calc_result=Entry(calc_frame,width=10,textvariable=var3,\
                  state='readonly').grid(row=2,column=4)
# setting the operational symbols
#operators=[('+',1),('-',2),('*',3),('/',4)]
var_operator=IntVar()
# define a function, to show the outputs of the Radiobutton
def selection():
    operator=var_operator.get()
    if operator==1:
        output='+'
    elif operator==2:
        output='-'
    elif operator==3:
        output='*'
    elif operator==4:
        output='/'
    return output
Radiobutton(calc_frame,text='+',variable=var_operator,value=1,command=selection).grid(row=0,column=1)
Radiobutton(calc_frame,text='-',variable=var_operator,value=2,command=selection).grid(row=1,column=1)
Radiobutton(calc_frame,text='*',variable=var_operator,value=3,command=selection).grid(row=2,column=1)
Radiobutton(calc_frame,text='/',variable=var_operator,value=4,command=selection).grid(row=3,column=1)
var_operator.set(1)
# define a label for '='
Label(calc_frame,text='=').grid(row=1,column=3)
# define a function, to calculate the results
def calc():
    if var_operator.get()==1:
        result=int(var1.get())+int(var2.get())
    elif var_operator.get()==2:
        result=int(var1.get())-int(var2.get())
    elif var_operator.get()==3:
        result=int(var1.get())*int(var2.get())
    elif var_operator.get()==4:
        result=int(var1.get())/int(var2.get())
    var3.set(str(result))
    print(f'{var1.get()} {selection()} {var2.get()} = {var3.get()}')

# setting buttons to show the calculation results or exit
Button(calc_frame,text='ENTER',command=calc).grid(row=4,column=0)
Button(calc_frame,text='EXIT',command=calc_frame.quit).grid(row=4,column=4)

mainloop()
