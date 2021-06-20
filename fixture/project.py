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
        #self.project_cache = None

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)
        #self.change_field_value("status", project.status)
        #self.change_field_value("inherit_global", project.inherit_global)
        #self.change_field_value("view_state", project.view_state)
        self.change_field_value("description", project.description)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def fill_project_form1(self):
        wd = self.app.wd
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys("test")

        wd.find_element_by_name("status").click()
        Select(wd.find_element_by_name("status")).select_by_visible_text("release")

        wd.find_element_by_xpath("//option[@value='30']").click()
        wd.find_element_by_name("inherit_global").click()

        wd.find_element_by_name("view_state").click()
        Select(wd.find_element_by_name("view_state")).select_by_visible_text("private")
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='View Status'])[1]/following::option[2]").click()

        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys("test test test")

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def create(self, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        # Init group creation
        wd.find_element_by_name("new").click()
        # Fill group form
        self.fill_group_form(new_group_data)
        # submit create
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()
        self.group_cache = None

    def return_to_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("group page").click()

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        self.select_group_by_index(index)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        self.select_group_by_id(id)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None



    def select_first_group(self):
        self.select_group_by_index(0)

    def select_group_by_index(self, index):
        wd = self.app.wd
        # Select first group
        wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        # Select first group
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def modify_first_group(self, new_group_data):
        self.modify_group_by_index(0, new_group_data)

    def modify_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # open modification form
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_form(new_group_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def modify_group_by_id(self, id, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        # open modification form
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_form(new_group_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)

