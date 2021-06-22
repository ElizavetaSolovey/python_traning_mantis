from suds.client import Client
from suds import WebFault
from model.project import Project

class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False


    def get_project_list(self):
        list = []
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            list1 = client.service.mc_projects_get_user_accessible("administrator", "root")
            for row in range(len(list1)):
                list.append(Project(id=str(list1[row].id), name=list1[row].name, description=list1[row].description))
            return list
        except WebFault:
            return None
