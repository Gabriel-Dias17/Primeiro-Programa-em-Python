from tkinter import *
from tkinter import ttk
janela = Tk()
janela.title("Calculadora")

cor1= "#800080" #roxo
cor2= "#FFFFFF" #branco
cor3= "#FFB5C0" #rosa\
cor4= "#e3c097" #bege
cor5= "#000000" #preto


janela.geometry("235x310")
janela.config(bg=cor4)
frame_tela = Frame(janela, width=235,heigh=50, bg=cor3)
frame_tela.grid(row=0,column=0)
frame_corpo = Frame(janela, width=235,heigh=268)
frame_corpo.grid(row=1,column=0)
todos_valores = ''
def entrar_valores(event):
    global todos_valores
    todos_valores =todos_valores + str(event) 
    valor_texto.set(todos_valores) 
valor_texto = StringVar()
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))
def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("") 

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT,anchor="e", justify=RIGHT,font=('Ivy 18 '),  bg=cor3,  )
app_label.place(x=0,y=0)
janela.resizable(False,False)
b_1 = Button(frame_corpo,command=limpar_tela, text="C", width=24, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0,y=0)
b_2 = Button(frame_corpo,command=lambda:entrar_valores('1'), text="1", width=5, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=0,y=55)
b_3 = Button(frame_corpo, command=lambda:entrar_valores('2'),text="2", width=5, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=65,y=55)
b_4 = Button(frame_corpo, command=lambda:entrar_valores('3'),text="3", width=5, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=130,y=55)
b_5 = Button(frame_corpo, command=lambda:entrar_valores('4'),text="4", width=5, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=0,y=110)
b_6 = Button(frame_corpo, command=lambda:entrar_valores('5'),text="5", width=5, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=65,y=110)
b_7 = Button(frame_corpo, command=lambda:entrar_valores('6'),text="6", width=5, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=130,y=110)
b_8 = Button(frame_corpo, command=lambda:entrar_valores('7'),text="7", width=5, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0,y=165)
b_9 = Button(frame_corpo, command=lambda:entrar_valores('8'),text="8", width=5, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=65,y=165)
b_10 = Button(frame_corpo, command=lambda:entrar_valores('9'),text="9", width=5, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=130,y=165)
b_11 = Button(frame_corpo, command=lambda:entrar_valores('0'),text="0", width=5, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=0,y=220)
b_12 = Button(frame_corpo, command=lambda:entrar_valores('+'), text="+", width=3, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=195,y=55)
b_13 = Button(frame_corpo, command=lambda:entrar_valores('-'), text="-", width=3, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=195,y=110)
b_14 = Button(frame_corpo, command=lambda:entrar_valores('/'),text="/", width=3, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=195,y=165)
b_15 = Button(frame_corpo, command=lambda:entrar_valores('*'), text="*", width=3, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=195,y=220)
b_16 = Button(frame_corpo, command=calcular, text="=", width=12, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=65,y=220)



janela.mainloop()
