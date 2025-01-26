import tkinter as tk
from tkinter import messagebox
import random 
import json



def questions(subject_name):
    with open("data.json", "r", encoding = "utf-8") as file:
        question = json.load(file)
        question = question[subject_name]
    questions = []
    for i in question:
        questions.append(i)
    return questions

def show_middle_score(name):
    middle_score_label = tk.Label(root, text = '', font = ('uft-8', 12), fg = "#23c429")
    middle_score_label.place(x = 400,y = 400,)
    with open("users.json", "r") as file:
        data = json.load(file)

    for i in range(len(data)):
        for j in data[i]:
            if name == data[i][j]["name"]:
                middle_score_label.config(text = f'مجموع امتیاز شما: {data[i][j]["sum score"]}')
                break

def user_in_page(name):
    user_btn = tk.Button(root, text= str(name), width = 10, font = ('uft-8', 10), bg = 'gray', fg = 'white',command = lambda : show_middle_score(name)) 
    user_btn.place(x = 600, y = 2)
    
class QuizApp:  #page four
    
    def __init__(self, root,value, name):

        self.root = root
        self.value = value
        self.name = name

        self.root.title('Testy')
        self.root.geometry('1000x500')

        self.score = 0
        self.question_count = -1
        self.time = 20
        self.questions = random.sample(questions(value), 3)

        self.question_label = tk.Label(text='')
        self.question_label.place(x = 0, y = 0)

        self.var = tk.IntVar()
        self.option_btn = []

        for i in range(4):
            btn = tk.Radiobutton(root, text='', variable = self.var, value = i)
            btn.place(x = i*110 , y = 100)
            self.option_btn.append(btn)

        self.submit_btn = tk.Button(root, text = 'ارسال جواب', command = self.submit_answer)
        self.submit_btn.place(x = 400,y = 150)

        self.timer_label = tk.Label(root, text='')
        self.timer_label.place(x= 700,y=0)

        self.final_score_label = tk.Label(root, text ='' )
        self.final_score_label.place(x = 380,y = 200)

        self.update_timer()
        self.next_question() #1

    def next_question(self):

        self.question_count += 1
 
        if self.question_count < len(self.questions):
            self.var.set(-1)
            self.time = 20
            
            self.question = self.questions[self.question_count] 
            self.question_label.config(text = self.question["question"])

            for i,j in enumerate(self.questions[self.question_count]["choices"]):
                self.option_btn[i].config(text = j)

        else:
            self.show_final_score()

    def update_timer(self):
        if self.time >= 0:
            self.timer_label.config(text = f"زمان باقی مانده {self.time} ثانیه")
            self.time -= 1  
            root.after(1000, self.update_timer)

        else:
            self.next_question()
            if self.question_count < len(self.questions):
                self.update_timer() 
             
            
    def submit_answer(self):
        
        if self.var.get() == self.questions[self.question_count]["answer"]: 
            self.score += 1
        self.next_question()
        
    def show_final_score(self):
        self.add_score()

        self.final_score_label.config(text=f'امتیاز نهایی شما: {len(self.questions)} / {self.score}')
        self.timer_label.place_forget()
        self.submit_btn.place_forget()
        self.question_label.place_forget()
        for btn in self.option_btn:
            btn.place_forget()                
        self.end_button()

    def add_score(self):
        with open("users.json", "r") as file:
            data = json.load(file)

        for i in range(len(data)):
            for j in data[i]:
                if self.name == data[i][j]["name"]:
                    data[i][j]["sum score"] = data[i][j]["sum score"] + (self.score)

                    with open("users.json", "w") as file:
                        json.dump(data, file, indent = 4)
                    break

    def end_button(self):
        self.restart = tk.Button(root, text = 'شروع دوباره', width = 20,fg = 'white', bg = 'blue',command = self.restart) 
        self.restart.place(x = 300,y=300)

        self.end = tk.Button(root, text = 'خروج', width = 20, fg = 'white', bg = 'blue',command = self.end)
        self.end.place(x = 500,y = 300) 

    def restart(self):
        self.final_score_label.destroy()
        self.restart.place_forget()
        self.end.place_forget()
        self.score = 0
        btn(root, self.name)

    def end(self):
        root.destroy()



class Creat_account: #page two_1
    def __init__(self, root):
        self.root = root
        self.root.title('حساب کاربری')

        self.show = tk.Label(root, text="")
        self.show.place(x = 200,y = 250)

        self.back_btn = tk.Button(root, text = 'بازگشت', fg = 'white', bg = 'blue', width = 7)
        self.back_btn.place(x = 338,y = 190)
        self.back_btn.bind("<ButtonPress>", lambda even : self.back(root))

        # self.name= ''
        self.a = True
        
      
        self.buttons()
    
    def on_enter1(self, event):
        self.user_name_input.delete(0, tk.END)

    def out_enter1(self, event):
        if self.user_name_input.get() == '':
            self.user_name_input.insert(0, 'نام حساب کاربری')

    def on_enter2(self, event):
        self.password_input.delete(0, tk.END)

    def out_enter2(self, event):
        if self.password_input.get() == '':
            self.password_input.insert(0, 'رمز')
       

    def buttons(self):

        self.label = tk.Label(root, text = "ساخت حساب کاربری", font = 22)
        self.label.place(x = 220, y = 10)

        self.user_name_input = tk.Entry(root,width = 35, font=('utf-8', 9))
        self.user_name_input.place(x = 150,y = 50)

        self.user_name_input.insert(0, 'نام حساب کاربری')

        self.user_name_input.bind('<FocusIn>', self.on_enter1)
        self.user_name_input.bind('<FocusOut>', self.out_enter1)

        self.fram1 = tk.Frame(root, bg = 'black', width=250, height=3)
        self.fram1.place(x = 150,y = 70)


        self.password_input = tk.Entry(root, width = 35, font=('utf-8', 9))
        self.password_input.place(x = 150,y=110)

        self.password_input.insert(0, 'رمز')
        self.password_input.bind('<FocusIn>', self.on_enter2)
        self.password_input.bind('<FocusOut>', self.out_enter2)
        


        self.fram2 = tk.Frame(root, bg = 'black', width=247, height=3)
        self.fram2.place(x = 150,y = 130)

        self.build = tk.Button(root, text = 'ساخت حساب', bg = 'blue', pady=3,padx=3, width = 33,fg = 'white', command = self.username_save)
        self.build.place(x = 150,y = 150)


    def username_save(self):
        if (self.user_name_input.get()) and (self.password_input.get()) != '':
            if (self.user_name_input.get() != 'نام حساب کاربری') and (self.password_input.get() != 'رمز'):

                self.user_specifications = {str(self.user_name_input.get()):{
                    'name' : self.user_name_input.get(),
                    'password': self.password_input.get(),
                    'sum score' :0
                }}

                self.save_in_file()
        else:
            pass

    def save_in_file(self):
        with open("users.json", "r") as file1:
            data = list(json.load(file1))

        self.names = []
        self.passwords = []

        for i in range(len(data)): 
            for j in data[i]:
                self.names.append(data[i][j]["name"])
                self.passwords.append(data[i][j]["password"])
                # self.name = self.user_name_input.get()

        for i in range(len(self.names)):
            if (self.user_name_input.get() == self.names[i]) and (self.password_input.get() == str(self.passwords[i])):
                self.a = False
                self.show.config(text='نام کاربری یا رمز خود را تغییر دهید.', fg = 'red')
                break

        if self.a == True:
            data.append(self.user_specifications)
            with open("users.json", "w") as file2:
                json.dump(data, file2,indent = 4)
            self.continu(root)

    def back(self, root):
        self.show.place_forget()
        self.back_btn.place_forget()
        self.user_name_input.place_forget()
        self.password_input.place_forget()
        self.fram1.place_forget()
        self.fram2.place_forget()
        self.label.place_forget()
        self.build.place_forget()

        
        Page_one(root)
    
    def continu(self, root):
        if self.a == True:
            self.show.place_forget() 
            self.back_btn.place_forget()
            self.user_name_input.place_forget()
            self.password_input.place_forget()
            self.fram1.place_forget()
            self.fram2.place_forget()
            self.label.place_forget()
            self.build.place_forget()

            user_in_page(self.user_name_input.get())
            
            btn(root,self.user_name_input.get())
        else:
            pass


class Login:  #page two_2
    def __init__(self, root):
        self.root = root
        self.root.title('ورود به حساب کاربری')

        self.show = tk.Label(root, text="")
        self.show.place(x = 200,y = 250)

        self.back_btn = tk.Button(root, text = 'بازگشت', fg = 'white', bg = 'blue', width = 7)
        self.back_btn.place(x = 338,y = 190)
        self.back_btn.bind("<ButtonPress>", lambda even : self.back(root))

        self.continu_btn = tk.Button(root, text = 'ادامه', fg = 'white', bg = 'blue', width = 7)
        self.continu_btn.place(x = 270,y = 190)
        self.continu_btn.bind("<ButtonPress>", lambda even : self.search_in_file())
      
        self.buttons()
    
    def on_enter1(self, event):
        self.user_name_input.delete(0, tk.END)

    def out_enter1(self, event):
        if self.user_name_input.get() == '':
            self.user_name_input.insert(0, 'نام حساب کاربری')

    def on_enter2(self, event):
        self.password_input.delete(0, tk.END)

    def out_enter2(self, event):
        if self.password_input.get() == '':
            self.password_input.insert(0, 'رمز')
       

    def buttons(self):

        self.label = tk.Label(root, text = 'ورود به حساب کاربری', font = 22)
        self.label.place(x = 220, y = 10)

        self.user_name_input = tk.Entry(root,width = 35, font=('utf-8', 9))
        self.user_name_input.place(x = 150,y = 50)

        self.user_name_input.insert(0, 'نام حساب کاربری')

        self.user_name_input.bind('<FocusIn>', self.on_enter1)
        self.user_name_input.bind('<FocusOut>', self.out_enter1)

        self.fram1 = tk.Frame(root, bg = 'black', width=250, height=3)
        self.fram1.place(x = 150,y = 70)


        self.password_input = tk.Entry(root, width = 35, font=('utf-8', 9))
        self.password_input.place(x = 150,y=110)

        self.password_input.insert(0, 'رمز')
        self.password_input.bind('<FocusIn>', self.on_enter2)
        self.password_input.bind('<FocusOut>', self.out_enter2)
        
        self.fram2 = tk.Frame(root, bg = 'black', width=247, height=3)
        self.fram2.place(x = 150,y = 130)

    def search_in_file(self):
        with open("users.json", "r") as file1:
            data = list(json.load(file1))

        self.names = []
        self.passwords = []

        for i in range(len(data)): 
            for j in data[i]:
                self.names.append(data[i][j]["name"])
                self.passwords.append(data[i][j]["password"])

        for i in range(len(self.names)):
            if ((self.user_name_input.get()) and (self.password_input.get())) != '':
                if (self.user_name_input.get() != 'نام حساب کاربری') and (self.password_input.get() != 'رمز'):
                    if (self.user_name_input.get() == self.names[i]) and (str(self.password_input.get()) == str(self.passwords[i])):
                        self.continu()
                        break

                    else:
                        self.show.config(text = 'کاربری با چنین مشخصات وجود ندارد', fg = 'red')
                else:
                    pass
            else:
                pass

    def back(self, root):
        self.show.place_forget()
        self.back_btn.place_forget()
        self.user_name_input.place_forget()
        self.password_input.place_forget()
        self.fram1.place_forget()
        self.fram2.place_forget()
        self.label.place_forget()
        self.continu_btn.place_forget()
        
        Page_one(root)
    
    def continu(self):
        
        self.show.place_forget() 
        self.back_btn.place_forget()
        self.user_name_input.place_forget()
        self.password_input.place_forget()
        self.fram1.place_forget()
        self.fram2.place_forget()
        self.label.place_forget()
        self.continu_btn.place_forget()

        user_in_page(self.user_name_input.get())
            
        btn(root, self.user_name_input.get())

class btn:  #page three
    def __init__(self, root, name):

        self.root = root
        self.root.title('Testy')
        self.root.geometry('1000x500')  
        self.name = name
        self.value = ''

        self.subject_label = tk.Label(root, text = "موضوع مورد نظر خود را انتخاب کنید")
        self.subject_label.place(x = 280 ,y = 100)

        self.subject_1 = tk.Button(root, text = "جغرافی", width = 11,fg = 'white', bg = 'blue', command = self.subject_1_func)
        self.subject_1.place(x = 270,y = 150)

        self.subject_2 = tk.Button(root, text = "علمی", width = 11,fg = 'white', bg = 'blue',command = self.subject_2_func)
        self.subject_2.place(x = 380,y = 150)

        self.subject_3 = tk.Button(root, text = "تاریخی", width = 11,fg = 'white', bg = 'blue',command = self.subject_3_func)
        self.subject_3.place(x = 270,y = 180)

        self.subject_4 = tk.Button(root, text = "سیاسی", width = 11,fg = 'white', bg = 'blue',command = self.subject_4_func)
        self.subject_4.place(x = 380,y = 180)

        self.start_btn = tk.Button(root, text = "شروع", width = 10, fg = 'white', bg = 'blue', font = 'utf-8')
        self.start_btn.place(x= 250,y=350)

        self.rahnama_btn = tk.Button(root, text = "راهنما", width=10,fg = 'white', bg = 'blue', font = 'utf-8')
        self.rahnama_btn.place(x= 370,y=350)

        self.start_btn.bind('<ButtonPress>', lambda even : self.delet())
        self.rahnama_btn.bind('<ButtonPress>', lambda even : self.show_description())

    def subject_1_func(self):
        self.value = "goghraphy" 

    def subject_2_func(self):
        self.value = "scientific" 

    def subject_3_func(self):
        self.value = "historical"

    def subject_4_func(self):
        self.value = "political" 


    def delet(self):
        if self.value == '':
            pass
        else:
            self.start_btn.place_forget()
            self.rahnama_btn.place_forget()

            self.subject_label.place_forget()
            self.subject_1.place_forget()
            self.subject_2.place_forget()
            self.subject_3.place_forget()
            self.subject_4.place_forget()       
            QuizApp(root, self.value,self.name)

    def show_description(self):

        messagebox.showinfo("راهنما", 'در این بازی شما می توانید با انتخاب موضوع مورد نظر،سوالات مربوط به همان بخش را پاسخ دهید.\nهمچنین شما می توانید با ساخت حساب کاربری،اطلاعات خود را ذخیره کنید.')




class Page_one:

    def __init__(self, root):
        self.root = root
        self.root.title('Testy')
        self.root.geometry('1000x500') 
        
        self.account1 = tk.Button(root, text = '''ساخت حساب کاربری''' , font = ('utf=8', 11), width = 15, bg = 'blue', fg = 'white')
        self.account1.place(x = 350, y = 180)
        self.account1.bind("<ButtonPress>", lambda even: self.creating_account())

        self.account2 = tk.Button(root, text = '''ورود به حساب کاربری''' , font = ('utf=8', 11), width = 15, bg = 'blue', fg = 'white')
        self.account2.place(x = 350, y = 220)
        self.account2.bind("<ButtonPress>", lambda even: self.login())


    def creating_account(self):
       
        self.account1.place_forget()
        self.account2.place_forget()

        Creat_account(root)  
    
    def login(self):
        self.account1.place_forget()
        self.account2.place_forget()

        Login(root)



root = tk.Tk()
if __name__== "__main__":
    app = Page_one(root)
    root.mainloop()
