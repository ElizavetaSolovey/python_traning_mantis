from sys import maxsize


class Project:
    def __init__(self, projectname=None, projectstatus=None, projectinheritglobal=None,
                 projectviewstate=None, projectdescription=None, id=None):
        self.projectname = projectname
        self.projectstatus = projectstatus
        self.projectinheritglobal = projectinheritglobal
        self.projectviewstate = projectviewstate
        self.projectdescription = projectdescription
        self.id = id

    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.name, self.header, self.footer)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

