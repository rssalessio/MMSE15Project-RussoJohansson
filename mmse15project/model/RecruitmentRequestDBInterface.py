from mmse15project.model.RecruitmentRequest import *
from mmse15project.model.DBInterface import DBInterface
from mmse15project.model.GenericMethods import *


class RecruitmentRequestDBInterface(DBInterface):
    def __init__(self,database):
        self.database = database

    def add(self, request):
        values = request.getAll()
        values = tuple_without(values,0)
        self.database.executeDoQuery('INSERT INTO recruitmentRequest (type,date, department,title,status,description ) VALUES (?,?,?,?,?,?)',values)
        request.id = self.database.getLastRow()
        return request.id

    def update(self,request):
        values = request.getAll()
        values =tuple_without(values,0)
        values = values +  (request.id,)
        self.database.executeDoQuery('UPDATE recruitmentRequest SET type=?,date=?,department=?,title=?,status=?,description=? where id=?',values)

    def get(self,request):
        ans = self.database.executeKnowQuery('SELECT * FROM recruitmentRequest WHERE id = ?', (request.id,))
        if (len(ans) == 0):
            return False
        ans = ans[0]
        ret = RecruitmentRequest()
        ret.setAll(ans)
        return ret

    def getAll(self):
        ans= self.database.executeKnowQuery('SELECT * from recruitmentRequest')
        if (len(ans)==0):
            return False
        ret=[]
        for row in ans:
            temp = RecruitmentRequest()
            temp.setAll(row)
            ret.append(temp)
        return ret

    def getByID(self,r_id):
        temp = RecruitmentRequest()
        temp.id = r_id
        return self.get(temp)

    def getByStatus(self, status):
        all = self.getAll()
        if all is False:
            return []
        ret = []
        for req in all:
            if req.status == status:
                ret.append(req)
        return ret
