import tkinter.ttk as ttk


# AccountTeam view for Marketing
class Marketing(ttk.Frame):
    def __init__(self, master, model, ctrl, acc_type, user):
        ttk.Frame.__init__(self, master)
        self.model = model
        self.ctrl = ctrl
        self.acc_type = acc_type
        self.user = user
        self.create_widgets()

    def create_widgets(self):
        container = ttk.Frame(self)
        container.pack()
        user_info = "Marketing, " + self.acc_type + " - logged in as " + self.user
        ttk.Label(container, text=user_info).pack()
        n = ttk.Notebook(container)
        n.pack()
        f1 = ttk.Frame(n)
        n.add(f1, text="Empty")