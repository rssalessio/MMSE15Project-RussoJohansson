import tkinter.ttk as ttk
from mmse15project.views.Config import Config
from mmse15project.views.GenericMethods import get_header
from mmse15project.views.subviews.PendingRecruitmentRequest import PendingRecruitmentRequest
from mmse15project.views.subviews.SearchRequest import SearchRequest
from mmse15project.views.subviews.SearchRequestDetails import SearchRequestDetails
from mmse15project.views.subviews.SearchRecruitmentRequest import SearchRecruitmentRequest
from mmse15project.views.subviews.NewRecruitmentRequest import NewRecruitmentRequest

# AccountTeam view for HR
class HR(ttk.Frame):
    def __init__(self, master, model, ctrl, acc_team, acc_type, user):
        ttk.Frame.__init__(self, master)
        self.model = model
        self.ctrl = ctrl
        self.acc_team = acc_team
        self.acc_type = acc_type
        self.user = user
        self.create_widgets()

    def create_widgets(self):
        self.ctrl.clear_frame(self)
        get_header(self, "Config", lambda: self.config())
        n = ttk.Notebook(self)
        n.grid(row=1, columnspan=2)
        f1 = PendingRecruitmentRequest(n, self.model, self.ctrl)
        f2 = SearchRecruitmentRequest(n, self.model, self.ctrl)
        f3 = SearchRequest(n, self.model, self.ctrl)
        f4 = SearchRequestDetails(n, self.model, self.ctrl)
        f5 = NewRecruitmentRequest(n, self.model, self.ctrl)
        n.add(f1, text="Pending recruitments", sticky="NS")
        n.add(f2, text="View recruitment", sticky="NS")
        n.add(f3, text="View request", sticky="NS")
        n.add(f4, text="View request details", sticky="NS")
        n.add(f5, text='New recruitment request')

    def config(self):
        self.ctrl.clear_frame(self)
        get_header(self, "General", lambda: self.create_widgets())
        c = Config(self, self.model, self. ctrl)
        c.grid(row=1, columnspan=2)
