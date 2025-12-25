import tkinter as tk
import os
print(os.getcwd())
x=tk.Tk()
x.title("Weather in Top 5 Biggest Cities in Jordan")
x.geometry('500x500')
a=tk.Label(x,text="Enter the name of the city:",font=('bold',20))
a.pack()
lbl=tk.Label(x,text="(Amman, Madaba, Aqaba, Jerash, Irbid)",font=('italic',15))
lbl.pack()
b=tk.Entry(x)
b.pack()
def city():
    try:
        f=b.get()
        if f=='Amman':
            d=open(r'Amman.txt','r')
            r.config(text=d.read())
            d.close()
        elif f=='Madaba':
            e=open(r'Madaba.txt','r')
            r.config(text=e.read())
            e.close()
        elif f=='Aqaba':
            g=open(r'Aqaba.txt','r')
            r.config(text=g.read())
            g.close()
        elif f=='Jerash':
            h=open(r'Jerash.txt','r')
            r.config(text=h.read())
            h.close()
        elif f=='Irbid':
            i=open(r'Irbid.txt','r')
            r.config(text=i.read())
            i.close()
        else:
            y=tk.Tk()
            y.title('ERROR MSG')
            s=tk.Label(y,text="The entered city isn't in our system, please enter one of the following:",font=('bold',35),fg='red',bg='black')
            s.pack()
            n=tk.Label(y,text="Amman, Aqaba, Irbid, Jerash, Madaba.",font=('bold',48),fg='red',bg='black')
            n.pack()
            y.mainloop() 
    except:
        z=tk.Tk()
        z.title('ERROR MSG')
        p=tk.Label(z,text="An error happened",font=('bold',48),fg='red',bg='black')
        p.pack()
        z.mainloop()
c=tk.Button(x,text="Check",command=city)
c.pack()
r=tk.Label(x,text="")
r.pack()
x.mainloop()