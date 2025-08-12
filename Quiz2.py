import tkinter as tk
from tkinter import messagebox
import random
import json
import os
import sys


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def questions(subject_name):
    with open(resource_path("english_data.json"), "r") as file:
        question_data = json.load(file)
        question = question_data.get(subject_name)
    questions_list = []
    for i in question:
        questions_list.append(i)
    return questions_list


def show_middle_score(name):
    middle_score_label = tk.Label(root, text='', font=(
        'utf-8', 14), bg="#1A1A1A", fg="#23c429")
    middle_score_label.place(x=430, y=430,)

    def del_label(label):
        label.destroy()

    with open(resource_path("users.json"), "r") as file:
        data = json.load(file)

    for i in range(len(data)):
        for j in data[i]:
            if name == data[i][j]["name"]:
                if data[i][j]["number of play"] > 0:
                    middle_score_label.config(
                        text=f'Middle score: {data[i][j]["sum score"]/data[i][j]["number of play"]}')
                    break
                else:
                    middle_score_label.config(
                        text='Middle score: 0')
    root.after(5000, del_label, middle_score_label)


def user_in_page(name):
    user_btn = tk.Button(root, text=str(name), width=10, font=(
        'utf-8', 10), bg='gray', fg='white', command=lambda: show_middle_score(name, ))
    user_btn.place(x=1000, y=10)


class QuizApp:  # page 4
    def __init__(self, root, value, name):

        self.root = root
        self.value = value
        self.name = name
        self.number_of_play = 0  # new

        self.root.title('Quiz')

        self.score = 0
        self.question_count = -1
        self.time = 30
        self.timer_id = None
        self.questions = random.sample(questions(value), 5)

        self.question_label = tk.Label(text='', font=(
            "utf-8", 16), bg="#1A1A1A", fg="yellow")
        self.question_label.place(x=10, y=10)

        self.var = tk.IntVar()
        self.option_btn = []

        for i in range(4):
            btn = tk.Radiobutton(root, text='', variable=self.var, value=i, bg="#1A1A1A", fg="yellow", font=(
                "utf-8", 14), command=lambda i=i: self.selected(i))
            btn.place(x=i*250, y=100)
            self.option_btn.append(btn)

        self.submit_btn = tk.Button(root, font=(
            "utf-8", 16), text="Submit Answer", bg="#1A1A1A", fg="white", command=self.submit_answer)
        self.submit_btn.place(x=690, y=200)

        self.timer_label = tk.Label(root, text='', font=(
            "utf-8", 14), bg="#1A1A1A", fg="red")
        self.timer_label.place(x=700, y=10)

        self.final_score_label = tk.Label(root, text='', bg="#1A1A1A")
        self.final_score_label.place(x=480, y=200)

        self.update_timer()
        self.next_question()  # 1

    def selected(self, option_index):
        for i, btn in enumerate(self.option_btn):
            if i == option_index:
                btn.config(bg="#4567f4")
        self.root.after(4500, self.reset_btn_selected)

    def reset_btn_selected(self):
        for btn in self.option_btn:
            btn.configure(bg="#1A1A1A")

    def next_question(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)

        self.question_count += 1
        self.reset_btn_selected()

        if self.question_count < len(self.questions):
            self.var.set(-1)
            self.time = 30

            self.question = self.questions[self.question_count]
            self.question_label.config(text=self.question["question"])

            for i, j in enumerate(self.questions[self.question_count]["choices"]):
                self.option_btn[i].config(text=j)

            self.update_timer()

        else:
            self.show_final_score()

    def update_timer(self):
        if self.time >= 0:
            self.timer_label.config(text=f"Time: {self.time}s")
            self.time -= 1
            self.timer_id = root.after(1000, self.update_timer)
        else:
            self.submit_answer()

    def submit_answer(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)

        if self.var.get() == self.questions[self.question_count]["answer"]:
            self.score += 1
        self.next_question()

    def show_final_score(self):
        self.add_score()

        self.final_score_label.config(
            text=f'Final score: {self.score}/{len(self.questions)} ', font=("utf-8", 16), fg="yellow")
        self.timer_label.place_forget()
        self.submit_btn.place_forget()
        self.question_label.place_forget()
        for btn in self.option_btn:
            btn.place_forget()
        self.end_button()

    def add_score(self):
        with open(resource_path("users.json"), "r") as file:
            data = json.load(file)

        for i in range(len(data)):
            for j in data[i]:
                if self.name == data[i][j]["name"]:
                    data[i][j]["sum score"] = data[i][j]["sum score"] + \
                        (self.score)
                    data[i][j]["number of play"] += 1
                    break
        with open(resource_path("users.json"), "w") as file:
            json.dump(data, file, indent=4)

    def end_button(self):
        self.restart = tk.Button(root, text='Restart', width=15, font=(
            "utf-8", 16), fg='white', bg='blue', command=self.restart)
        self.restart.place(x=370, y=300)

        self.end = tk.Button(root, text="Exit", width=15, fg='white', font=(
            "utf-8", 16), bg='blue', command=self.end)
        self.end.place(x=570, y=300)

    def restart(self):
        self.final_score_label.destroy()
        self.restart.place_forget()
        self.end.place_forget()
        self.score = 0
        Choosen_topic(root, self.name)

    def end(self):
        root.destroy()


class Creat_account:  # page two_1
    def __init__(self, root):
        self.root = root
        self.root.title("Create Account")

        self.show = tk.Label(root, text="", bg="#1A1A1A")
        self.show.place(x=380, y=270)

        self.back_btn = tk.Button(root, font=(
            "utf-8", 16), text="Back", fg='white', bg='blue', width=7)
        self.back_btn.place(x=540, y=190)
        self.back_btn.bind("<ButtonPress>", lambda even: self.back(root))

        self.status = True
        self.buttons()

    def on_enter1(self, event):
        self.user_name_input.delete(0, tk.END)

    def out_enter1(self, event):
        if self.user_name_input.get() == '':
            self.user_name_input.insert(0, "username:")

    def on_enter2(self, event):
        self.password_input.delete(0, tk.END)

    def out_enter2(self, event):
        if self.password_input.get() == '':
            self.password_input.insert(0, "password:")

    def buttons(self):

        self.label = tk.Label(root, text="Create an Account", font=(
            "utf-8", 22), fg="yellow", bg="#1A1A1A")
        self.label.place(x=420, y=15)

        self.user_name_input = tk.Entry(
            root, width=35, font=('utf-8', 16), fg="#293062")
        self.user_name_input.place(x=340, y=100)

        self.user_name_input.insert(0, "username:")

        self.user_name_input.bind('<FocusIn>', self.on_enter1)
        self.user_name_input.bind('<FocusOut>', self.out_enter1)

        self.password_input = tk.Entry(
            root, width=35, font=('utf-8', 16), fg="#293062")
        self.password_input.place(x=340, y=135)

        self.password_input.insert(0, "password:")
        self.password_input.bind('<FocusIn>', self.on_enter2)
        self.password_input.bind('<FocusOut>', self.out_enter2)

        self.build = tk.Button(root, font=("utf-8", 16), text="Next",
                               bg='blue', fg='white', width=7, command=self.username_save)
        self.build.place(x=440, y=190)

    def username_save(self):
        if (self.user_name_input.get()) and (self.password_input.get()) != '':
            if (self.user_name_input.get() != "username:") and (self.password_input.get() != "password:"):

                self.user_specifications = {str(self.user_name_input.get()): {
                    'name': self.user_name_input.get(),
                    'password': self.password_input.get(),
                    'sum score': 0,
                    "number of play": 0
                }}

                self.save_in_file()
        else:
            messagebox.showerror(
                "Error", "Enter your username and password please.")

    def save_in_file(self):
        data = []
        with open(resource_path("users.json"), "r") as file1:
            data = list(json.load(file1))

        self.names = []
        self.passwords = []

        for item in data:
            for key, value in item.items():
                self.names.append(value["name"])
                self.passwords.append(value["password"])

        self.status = True
        for i in range(len(self.names)):
            if (self.user_name_input.get() == self.names[i]) and (self.password_input.get() == str(self.passwords[i])):
                self.a = False
                self.show.config(
                    text='Change your username or password.', fg='red', font=("utf-8", 14))
                break

        if self.status == True:
            data.append(self.user_specifications)
            with open(resource_path("users.json"), "w") as file2:
                json.dump(data, file2, indent=4)
            self.continu(root)

    def back(self, root):
        self.show.place_forget()
        self.back_btn.place_forget()
        self.user_name_input.place_forget()
        self.password_input.place_forget()
        self.label.place_forget()
        self.build.place_forget()

        Page_one(root)

    def continu(self, root):
        if self.status == True:
            self.show.place_forget()
            self.back_btn.place_forget()
            self.user_name_input.place_forget()
            self.password_input.place_forget()
            self.label.place_forget()
            self.build.place_forget()

            user_in_page(self.user_name_input.get())
            Choosen_topic(root, self.user_name_input.get())


class Login:  # page two_2
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.show = tk.Label(root, text="", bg="#1A1A1A")
        self.show.place(x=380, y=270)

        self.back_btn = tk.Button(root, text="Back", font=(
            'utf-8', 16), fg='white', bg='blue', width=7)
        self.back_btn.place(x=560, y=190)
        self.back_btn.bind("<ButtonPress>", lambda even: self.back(root))

        self.continu_btn = tk.Button(root, font=(
            'utf-8', 16), text="Next", fg='white', bg='blue', width=7)
        self.continu_btn.place(x=460, y=190)
        self.continu_btn.bind(
            "<ButtonPress>", lambda even: self.search_in_file())

        self.buttons()

    def on_enter1(self, event):
        self.user_name_input.delete(0, tk.END)

    def out_enter1(self, event):
        if self.user_name_input.get() == '':
            self.user_name_input.insert(0, "username")

    def on_enter2(self, event):
        self.password_input.delete(0, tk.END)

    def out_enter2(self, event):
        if self.password_input.get() == '':
            self.password_input.insert(0, "password")

    def buttons(self):

        self.label = tk.Label(root, text="Login", font=(
            "", 22), bg="#1A1A1A", fg="yellow")
        self.label.place(x=480, y=15)

        self.user_name_input = tk.Entry(
            root, width=35, font=('utf-8', 16), fg="#293062")
        self.user_name_input.place(x=340, y=100)

        self.user_name_input.insert(0, "username:")

        self.user_name_input.bind('<FocusIn>', self.on_enter1)
        self.user_name_input.bind('<FocusOut>', self.out_enter1)

        self.password_input = tk.Entry(
            root, width=35, font=('utf-8', 16), fg="#293062")
        self.password_input.place(x=340, y=135)

        self.password_input.insert(0, "password:")
        self.password_input.bind('<FocusIn>', self.on_enter2)
        self.password_input.bind('<FocusOut>', self.out_enter2)

    def search_in_file(self):
        data = []
        with open(resource_path(R"Quiz_game/users.json"), "r") as file1:
            data = list(json.load(file1))

        self.names = []
        self.passwords = []

        for item in data:
            for key, value in item.items():
                self.names.append(value["name"])
                self.passwords.append(value["password"])

        user_found_and_matched = False
        for i in range(len(self.names)):
            if ((self.user_name_input.get()) and (self.password_input.get())) != '':
                if (self.user_name_input.get() != "username:") and (self.password_input.get() != "password:"):
                    if (self.user_name_input.get() == self.names[i]) and (str(self.password_input.get()) == str(self.passwords[i])):
                        self.continu()
                        user_found_and_matched = True
                        break

        if not user_found_and_matched:
            self.show.config(
                text="There is no user with such specifications.", fg='red', font=("utf-8", 14))

    def back(self, root):
        self.show.place_forget()
        self.back_btn.place_forget()
        self.user_name_input.place_forget()
        self.password_input.place_forget()
        self.label.place_forget()
        self.continu_btn.place_forget()

        Page_one(root)

    def continu(self):

        self.show.place_forget()
        self.back_btn.place_forget()
        self.user_name_input.place_forget()
        self.password_input.place_forget()
        self.label.place_forget()
        self.continu_btn.place_forget()

        user_in_page(self.user_name_input.get())

        Choosen_topic(root, self.user_name_input.get())


class Choosen_topic:  # page 3
    def __init__(self, root, name):

        self.root = root
        self.root.title('Choose Topic')
        self.name = name
        self.value = ''

        self.subject_label = tk.Label(root, text="Choose your regarding topic.", font=(
            "utf-8", 16), bg="#1A1A1A", fg="yellow")
        self.subject_label.place(x=400, y=70)

        self.subject_1 = tk.Button(root, text="Geography", width=11, font=(
            "utf-8", 14), fg='white', bg='blue', command=self.subject_1_func)
        self.subject_1.place(x=390, y=150)

        self.subject_2 = tk.Button(root, text="Scientific", width=11, font=(
            "utf-8", 14), fg='white', bg='blue', command=self.subject_2_func)
        self.subject_2.place(x=530, y=150)

        self.subject_3 = tk.Button(root, text="Historical", width=11, font=(
            "utf-8", 14), fg='white', bg='blue', command=self.subject_3_func)
        self.subject_3.place(x=390, y=190)

        self.subject_4 = tk.Button(root, text="Political", width=11, font=(
            "utf-8", 14), fg='white', bg='blue', command=self.subject_4_func)
        self.subject_4.place(x=530, y=190)

        self.start_btn = tk.Button(
            root, text="Start", width=11, fg='white', bg='blue', font=('utf-8', 14))
        self.start_btn.place(x=390,  y=350)

        self.rahnama_btn = tk.Button(
            root, text="Guide", width=11, fg='white', bg='blue', font=('utf-8', 14))
        self.rahnama_btn.place(x=530, y=350)

        self.start_btn.bind('<ButtonPress>', lambda even: self.delet())
        self.rahnama_btn.bind(
            '<ButtonPress>', lambda even: self.show_description())

    def subject_1_func(self):
        self.value = "Geography"

    def subject_2_func(self):
        self.value = "Scientific"

    def subject_3_func(self):
        self.value = "Historical"

    def subject_4_func(self):
        self.value = "Political"

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
            QuizApp(root, self.value, self.name)

    def show_description(self):

        messagebox.showinfo("Guide", """In this game, you can answer questions related to the chosen topic.
                             You can also save your information by creating a user account.""")


class Page_one:

    def __init__(self, root):
        self.root = root
        self.root.title('login&create account')
        self.root.geometry('1100x600')
        self.root.resizable(False, False)
        self.root.configure(bg="#1A1A1A")

        self.account1 = tk.Button(root, text='''Create an account''', font=(
            'utf-8', 16), width=15, bg='blue', fg='white')
        self.account1.place(x=440, y=180)
        self.account1.bind(
            "<ButtonPress>", lambda even: self.creating_account())

        self.account2 = tk.Button(root, text='''Login''', font=(
            'utf-8', 16), width=15, bg='blue', fg='white')
        self.account2.place(x=440, y=250)
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
if __name__ == "__main__":
    app = Page_one(root)
    root.mainloop()
