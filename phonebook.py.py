from Tkinter import *
import sqlite3
con=sqlite3.Connection('csedb')
front=Tk()
front.title("My Phonebook")             # front  with my details
front.configure(bg='black')
Label(front,text='Phonebook',font='times 30 bold',bg='black',fg='green').grid(row=0,column=0)
Label(front,text='      ',bg='black').grid(row=1,column=0)
img=PhotoImage(file='logo.gif')                  # logo
Label(front,image=img).grid(row=2,column=0)
Label(front,text='      ',bg='black').grid(row=3,column=0)
Label(front,text='  Programmed by : Abhishek Chauhan  ',bg='black',fg='green',font='times 20 bold').grid(row=4,column=0)
Label(front,text='                    Er_No :181B011',bg='black',fg='green',font='times 20 bold').grid(row=5,column=0,sticky=W)
Label(front,text='      ',bg='black').grid(row=6,column=0)
def go():
    front.destroy()
    main=Tk()
    main.configure(bg='black')
    main.geometry('416x425')
    main.title('HULK Theme')
    cur=con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS PBOOK(ID INTEGER PRIMARY KEY AUTOINCREMENT,FNAME VARCHAR(20) DEFAULT NULL,LNAME VARCHAR(20) DEFAULT NULL,COMPANY VARCHAR(20) DEFAULT NULL,WEB VARCHAR(40) DEFAULT NULL,DOB DATE DEFAULT NULL,STREET VARCHAR(30) DEFAULT NULL,LANDMARK VARCHAR(20) DEFAULT NULL,CITY VARCHAR(20) DEFAULT NULL)')
    cur.execute('CREATE TABLE IF NOT EXISTS PHONE(ID INTEGER ,PNO NUMBER,FOREIGN KEY(ID) REFERENCES PBOOK(ID) ON DELETE CASCADE)')
    cur.execute('CREATE TABLE IF NOT EXISTS MAIL(ID INTEGER,EMAIL VARCHAR(40) DEFAULT NULL,FOREIGN KEY(ID) REFERENCES PBOOK(ID) ON DELETE CASCADE)')
    Label(main,text='Contacts',bg='black',fg='green').grid(row=0,column=0,sticky=W)
    
    src=Entry(main,width=66)
    src.grid(row=1,column=0)
    scrollbar = Scrollbar(orient="vertical")
    Label(main,text=' ',bg='black').grid(row=2,column=0)
    lb=Listbox(main,height=19,width=66,highlightcolor='green',selectbackground='green',selectforeground='black')
    lb.grid(row=3,column=0,sticky=N+S+W)
    lb.yscrollcommand=scrollbar.set
    scrollbar.command=lb.yview
    scrollbar.grid(row=3,column=1, sticky=N+S+W)
    lb.yview_scroll(1,"units")
    lb.yview_scroll(1,"units")
    Label(main,text=' ',bg='black').grid(row=4,column=0)
    rec=cur.execute('SELECT FNAME,LNAME FROM PBOOK P INNER JOIN PHONE E ON P.ID=E.ID ORDER BY FNAME')                  ### Problem 1 @ How to display multiple data in same row of listbox ?
    for val in rec:
        lb.insert(END,val)
    def fun(e=1):
        B=[1]
        B[0]=['%'+src.get()+'%']
        lb.delete(0,END)
        y=cur.execute("SELECT FNAME,LNAME FROM PBOOK WHERE FNAME LIKE  ? ",(B[0]))
        for i in y:
            lb.insert(END,i)
    lb.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=lb.yview)

    main.bind('<Key>',fun)
    def fn():
        show=Tk()
        show.configure(bg='black')
        show.geometry('350x320')
        show.title('INFO')
        cs=lb.curselection()
        N=lb.get(cs)
        cur.execute('SELECT  ID FROM PBOOK WHERE FNAME =(?) AND LNAME =(?)',(N[0],N[1]))
        t=cur.fetchall()
        for i in t:
            for j in i:
                I_D=j
        data=cur.execute('SELECT * FROM PBOOK WHERE ID=(?)',(I_D,))
        Label(show,text=' INFORMATION  ',bg='black',fg='green').grid(row=0,column=0,sticky=W)
        Label(show,text=' ',bg='black').grid(row=1,column=0)
        for value in data:
            Label(show,text=' Fname : ',bg='black',fg='green').grid(row=2,column=0,sticky=W)
            Label(show,text=value[1],bg='black',fg='green').grid(row=2,column=1,sticky=W)
            Label(show,text=' Lname : ',bg='black',fg='green').grid(row=3,column=0,sticky=W)
            Label(show,text=value[2],bg='black',fg='green').grid(row=3,column=1,sticky=W)
            Label(show,text=' Company : ',bg='black',fg='green').grid(row=4,column=0,sticky=W)
            Label(show,text=value[3],bg='black',fg='green').grid(row=4,column=1,sticky=W)
            Label(show,text=' Website : ',bg='black',fg='green').grid(row=5,column=0,sticky=W)
            Label(show,text=value[4],bg='black',fg='green').grid(row=5,column=1,sticky=W)
            Label(show,text=' DOB : ',bg='black',fg='green').grid(row=6,column=0,sticky=W)
            Label(show,text=value[5],bg='black',fg='green').grid(row=6,column=1,sticky=W)
            Label(show,text=' Street : ',bg='black',fg='green').grid(row=7,column=0,sticky=W)
            Label(show,text=value[6],bg='black',fg='green').grid(row=7,column=1,sticky=W)
            Label(show,text=' Landmark : ',bg='black',fg='green').grid(row=8,column=0,sticky=W)
            Label(show,text=value[7],bg='black',fg='green').grid(row=8,column=1,sticky=W)
            Label(show,text=' City : ',bg='black',fg='green').grid(row=9,column=0,sticky=W)
            Label(show,text=value[8],bg='black',fg='green').grid(row=9,column=1,sticky=W)
        data2=cur.execute('SELECT * FROM PHONE WHERE ID =(?)',(I_D,))
        for value1 in data2:
            Label(show,text=' Phone_No : ',bg='black',fg='green').grid(row=11,column=0,sticky=W)
            Label(show,text=value1[1],bg='black',fg='green').grid(row=11,column=1,sticky=W)
        data3=cur.execute('SELECT * FROM MAIL WHERE ID =(?)',(I_D,))
        for value2 in data3:
            Label(show,text=' Email : ',bg='black',fg='green').grid(row=10,column=0,sticky=W)
            Label(show,text=value2[1],bg='black',fg='green').grid(row=10,column=1,sticky=W)
        #Label(show,text=' ',bg='black').grid(row=11,column=0)
        def cl():
            show.destroy()
        Label(show,text= ' ',bg='black').grid(row=12,column=0)
        Button(show,text=' OK ',bg='black',fg='green',command=cl).grid(row=13,column=1)
        def edi():
            edit=Tk()
            show.destroy()
            edit.configure(bg='black')
            edit.geometry('280x320')
            edit.title('EDIT')
            Label(edit,text=' DETAILS',bg='black',fg='green').grid(row=1,column=0,sticky=W)
            Label(edit,text=' ',bg='black').grid(row=3,column=0)
            Label(edit,text='  First Name              ',fg='green',bg='black').grid(row=5,column=0,sticky=W)
            s2=Entry(edit)
            s2.grid(row=5,column=1)
            fn=cur.execute('SELECT FNAME FROM PBOOK WHERE ID=(?)',(I_D,))
            for i in fn:
                x1=i[0]
            s2.insert(0,x1)
            Label(edit,text='  Last Name ',fg='green',bg='black').grid(row=6,column=0,sticky=W)
            s3=Entry(edit)
            s3.grid(row=6,column=1)
            fn=cur.execute('SELECT LNAME FROM PBOOK WHERE ID=(?)',(I_D,))
            for i in fn:
                x2=i[0]
            s3.insert(0,x2)
            Label(edit,text='  Company  ',fg='green',bg='black').grid(row=7,column=0,sticky=W)
            s4=Entry(edit)
            s4.grid(row=7,column=1)
            fn=cur.execute('SELECT COMPANY FROM PBOOK WHERE ID=(?)',(I_D,))
            for i in fn:
                x3=i[0]
            s4.insert(0,x3)
            Label(edit,text='  Website    ',fg='green',bg='black').grid(row=8,column=0,sticky=W)
            s5=Entry(edit)
            s5.grid(row=8,column=1)
            fn=cur.execute('SELECT WEB FROM PBOOK WHERE ID=(?)',(I_D,))
            for i in fn:
                x4=i[0]
            s5.insert(0,x4)
            Label(edit,text='  Phone       ',fg='green',bg='black').grid(row=9,column=0,sticky=W)
            s6=Entry(edit)
            s6.grid(row=9,column=1)
            fn=cur.execute('SELECT PNO FROM PHONE WHERE ID=(?)',(I_D,))
            for i in fn:
                x5=i[0]
            s6.insert(0,x5)
            Label(edit,text='  DOB          ',fg='green',bg='black').grid(row=10,column=0,sticky=W)
            s7=Entry(edit)
            s7.grid(row=10,column=1)
            fn=cur.execute('SELECT DOB FROM PBOOK WHERE ID=(?)',(I_D,))
            for i in fn:
                x6=i[0]
            s7.insert(0,x6)
            Label(edit,text='  Email         ',fg='green',bg='black').grid(row=11,column=0,sticky=W)
            s8=Entry(edit)
            s8.grid(row=11,column=1)
            fn=cur.execute('SELECT EMAIL FROM MAIL WHERE ID=(?)',(I_D,))
            for i in fn:
                x7=i[0]
            s8.insert(0,x7)
            Label(edit,text='  Street       ',fg='green',bg='black').grid(row=12,column=0,sticky=W)
            s9=Entry(edit)
            s9.grid(row=12,column=1)
            fn=cur.execute('SELECT STREET FROM PBOOK WHERE ID=(?)',(I_D,))
            for i in fn:
                x8=i[0]
            s9.insert(0,x8)
            Label(edit,text='  Landmark ',fg='green',bg='black').grid(row=13,column=0,sticky=W)
            s10=Entry(edit)
            s10.grid(row=13,column=1)
            fn=cur.execute('SELECT LANDMARK FROM PBOOK WHERE ID=(?)',(I_D,))
            for i in fn:
                x9=i[0]
            s10.insert(0,x9)
            Label(edit,text='  City          ',fg='green',bg='black').grid(row=14,column=0,sticky=W)
            s11=Entry(edit)
            s11.grid(row=14,column=1)
            fn=cur.execute('SELECT CITY FROM PBOOK WHERE ID=(?)',(I_D,))
            for i in fn:
                x10=i[0]
            s11.insert(0,x10)
            Label(edit,text=' ',bg='black').grid(row=15,column=0)
            def saveas():
                if x1==s2.get() and x2==s3.get():
                    cur.execute('UPDATE  PBOOK SET FNAME=(?),LNAME=(?),COMPANY=(?),WEB=(?),DOB=(?),STREET=(?),LANDMARK=(?),CITY=(?) WHERE ID=(?)',(s2.get(),s3.get(),s4.get(),s5.get(),s7.get(),s9.get(),s10.get(),s11.get(),I_D))
                    con.commit()
                    cur.execute('UPDATE PHONE SET PNO=(?) WHERE ID=(?)',(s6.get(),I_D))
                    con.commit()
                    cur.execute('UPDATE MAIL SET EMAIL=(?) WHERE ID=(?)',(s8.get(),I_D))
                    con.commit()
                    edit.destroy()
                    ns=Tk()
                    ns.configure(bg='black')
                    ns.geometry('250x150')
                    Label(ns,text=' ',bg='black').grid(row=0,column=0)
                    Label(ns,text=' ',bg='black').grid(row=1,column=0)
                    Label(ns,text='         Contact updated successfully      ',bg='black',fg='green').grid(row=2,column=0)
                    def ok1():
                        ns.destroy()
                        #main.destroy()
                    
                    Button(ns,text='   OK   ',bg='black',fg='green',command=ok1).grid(row=3,column=0)
                else:
                    cur.execute('UPDATE  PBOOK SET FNAME=(?),LNAME=(?),COMPANY=(?),WEB=(?),DOB=(?),STREET=(?),LANDMARK=(?),CITY=(?) WHERE ID=(?)',(s2.get(),s3.get(),s4.get(),s5.get(),s7.get(),s9.get(),s10.get(),s11.get(),I_D))
                    con.commit()
                    cur.execute('UPDATE PHONE SET PNO=(?) WHERE ID=(?)',(s6.get(),I_D))
                    con.commit()
                    cur.execute('UPDATE MAIL SET EMAIL=(?) WHERE ID=(?)',(s8.get(),I_D))
                    con.commit()
                    edit.destroy()
                    ns=Tk()
                    ns.configure(bg='black')
                    ns.geometry('300x150')
                    Label(ns,text=' ',bg='black').grid(row=0,column=0)
                    Label(ns,text=' ',bg='black').grid(row=1,column=0)
                    Label(ns,text=' Contact updated successfully,restart it to view changes ',bg='black',fg='green').grid(row=2,column=0)
                    def ok1():
                        ns.destroy()
                        main.destroy()
                    
                    Button(ns,text='   OK   ',bg='black',fg='green',command=ok1).grid(row=3,column=0)
                
            Button(edit,text=' Save Changes ',bg='black',fg='green',command=saveas).grid(row=16,column=1)
            
        Button(show,text='Edit',bg='black',fg='green',command=edi).grid(row=13,column=0)
        def delete():
            cur.execute('DELETE FROM PBOOK WHERE ID=(?)',(I_D,))
            con.commit()
            show.destroy()
            ns1=Tk()
            ns1.configure(bg='black')
            ns1.geometry('300x150')
            Label(ns1,text=' ',bg='black').grid(row=0,column=0)
            Label(ns1,text=' ',bg='black').grid(row=1,column=0) 
            Label(ns1,text=' Contact deleted successfully,restart it to view changes ',bg='black',fg='green').grid(row=2,column=0)
            def ok2():
                  ns1.destroy()
                  main.destroy()
                  
                    
            Button(ns1,text='   OK   ',bg='black',fg='green',command=ok2).grid(row=3,column=0)
            
            
            
        Button(show,text='Delete contact',bg='black',fg='green',command=delete).grid(row=13,column=2)
    lb.bind("<<ListboxSelect>>",lambda x:fn() )
    
     
    def add():                                                                                          ### Add a contact
        new=Tk()
        new.configure(bg='black')
        new.geometry('350x330')                                                                                                            
        new.title('Saving')
##        x=cur.execute('SELECT COUNT(*) FROM PBOOK')
##        for z in x:
##            count=z[0]
        Label(new,text=' __New Contact__ ',fg='green',bg='black',font='times 15 bold').grid(row=0,column=0,sticky=W)
        Label(new,text='      ',bg='black').grid(row=1,column=0)
        
        Label(new,text='  First Name ',fg='green',bg='black').grid(row=2,column=0,sticky=W)
        e1=Entry(new)
        e1.grid(row=2,column=1)
        Label(new,text='  Last Name ',fg='green',bg='black').grid(row=3,column=0,sticky=W)
        e2=Entry(new)
        e2.grid(row=3,column=1)
        Label(new,text='  Company  ',fg='green',bg='black').grid(row=4,column=0,sticky=W)
        e3=Entry(new)
        e3.grid(row=4,column=1)
        Label(new,text='  Website    ',fg='green',bg='black').grid(row=5,column=0,sticky=W)
        e4=Entry(new)
        e4.grid(row=5,column=1)
        Label(new,text='  Phone       ',fg='green',bg='black').grid(row=6,column=0,sticky=W)
        e5=Entry(new)
        e5.grid(row=6,column=1)
        Label(new,text=' Insert a number (req) ',bg='black',fg='green').grid(row=7,column=1)
        Label(new,text='  DOB          ',fg='green',bg='black').grid(row=8,column=0,sticky=W)
        e6=Entry(new)
        e6.grid(row=8,column=1)
        Label(new,text='  Email         ',fg='green',bg='black').grid(row=9,column=0,sticky=W)
        e7=Entry(new)
        e7.grid(row=9,column=1)
        Label(new,text='  Street       ',fg='green',bg='black').grid(row=11,column=0,sticky=W)
        e8=Entry(new)
        e8.grid(row=11,column=1)
        Label(new,text=' Landmark ',fg='green',bg='black').grid(row=12,column=0,sticky=W)
        e9=Entry(new)
        e9.grid(row=12,column=1)
        Label(new,text='  City          ',fg='green',bg='black').grid(row=13,column=0,sticky=W)
        e10=Entry(new)
        e10.grid(row=13,column=1)
        Label(new,text=' ',bg='black').grid(row=14,column=0)
        def save():
            a=e1.get()
            if len(a)==0:
                a='_'
            b=e2.get()
            if len(b)==0:
                b='_'
            c=e3.get()
            d=e4.get()
            e=e5.get()
            f=e6.get()
            g=e7.get()
            h=e8.get()
            i=e9.get()
            j=e10.get()
            if len(e)==0:
                new.destroy()
                add()
            else: 
                cur.execute('INSERT INTO PBOOK(FNAME,LNAME,COMPANY,WEB,DOB,STREET,LANDMARK,CITY) VALUES(?,?,?,?,?,?,?,?)',(a,b,c,d,f,h,i,j))
                cur.execute('INSERT INTO PHONE(ID,PNO) VALUES((SELECT MAX(ID) FROM PBOOK),?)',(e,))
                cur.execute('INSERT INTO MAIL(ID,EMAIL) VALUES((SELECT MAX(ID) FROM PBOOK),?)',(g,))
                con.commit()
                new.destroy()
                nf=Tk()
                nf.configure(bg='black')
                nf.geometry('250x150')
                Label(nf,text=' ',bg='black').grid(row=0,column=0)
                Label(nf,text=' ',bg='black').grid(row=1,column=0)
                Label(nf,text='               Contact saved successfully              ',bg='black',fg='green').grid(row=2,column=0)
                def ok():
                    x=cur.execute('SELECT FNAME,LNAME FROM PBOOK WHERE ID=(SELECT MAX(ID) FROM PBOOK)')
                    for p in x:
                        lb.insert(END,p)
                    nf.destroy()
                    
                Button(nf,text='   OK   ',bg='black',fg='green',command=ok).grid(row=3,column=0)
                Label(nf,text=' ',bg='black').grid(row=4,column=0)
                Label(nf,text=' ',bg='black').grid(row=5,column=0)
                Label(nf,text=' ',bg='black').grid(row=6,column=0)
                
                
        Button(new,text=' save ',bg='black',fg='green',command=save).grid(row=15,column=1)
    Button(main,text=' Add Contact ',bg='black',fg='green',command=add).grid(row=5,column=0,sticky=E)
Button(front,text='             GO            ',bg='black',fg='green',command=go).grid(row=8 ,column=0)
front.mainloop()
