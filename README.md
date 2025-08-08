I created an English language Quiz game, and I also created its exe file.
The new game has improvements in terms of program usability compared to the previous version.
I also expanded the question bank with the help of artificial intelligence.

This is first page of game, you can create your account and use it.
<img width="1375" height="780" alt="Screenshot (8)" src="https://github.com/user-attachments/assets/6cca5461-28a8-4c2c-b47c-f84efef15d8b" />
`class Page_one:

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
        Login(root)`
.
.
.
