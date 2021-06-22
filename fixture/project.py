from model.project import Project

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def manage_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()

    def manage_project_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage Projects").click()

    def create_project(self, new_project_data):
        wd = self.app.wd
        self.manage_page()
        self.manage_project_page()
        # Click new project
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        # Fill project form
        self.fill_project_form(new_project_data)
        # submit create
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.project_cache = None

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)
        #self.change_field_value("status", project.status)
        #wd.find_element_by_name("status").click()
        #Select(wd.find_element_by_name("status")).select_by_visible_text("release")
        #self.change_field_value("inherit_global", project.inherit_global)
        #wd.find_element_by_xpath("//option[@value='30']").click()
        #wd.find_element_by_name("inherit_global").click()
        #self.change_field_value("view_state", project.view_state)
        #wd.find_element_by_name("view_state").click()
        #Select(wd.find_element_by_name("view_state")).select_by_visible_text("private")
        #wd.find_element_by_xpath(
        #    "(.//*[normalize-space(text()) and normalize-space(.)='View Status'])[1]/following::option[2]").click()
        self.change_field_value("description", project.description)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_project_by_id(self, name):
        wd = self.app.wd
        # open manage project page
        self.manage_page()
        self.manage_project_page()
        # Select project
        self.select_project_by_id(name)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        self.project_cache = None

    def select_project_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath(f"//*[@href='manage_proj_edit_page.php?project_id={id}']").click()

    project_cache = None

    def is_project_with_name_present(self, old_projects, project):
        k = 0
        for i in range(len(old_projects)):
            if old_projects[i].name == project.name:
                k = k + 1
        if k != 1:
            return True
