from model.project import Project

def test_add_project(app, db, json_projects):
    app.session.login("administrator", "root")
    project = json_projects
    old_projects = db.get_project_list()
    if len(old_projects) != 0:
        k = 0
        for i in range(len(old_projects)):
            if old_projects[i].name == project.name:
                k = k + 1
        if k != 1:
            app.project.create_project(project)
            new_projects = db.get_project_list()
            old_projects.append(project)
            assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
            app.session.logout()
        else:
            app.session.logout()
    else:
        app.project.create_project(project)
        new_projects = db.get_project_list()
        old_projects.append(project)
        assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
        app.session.logout()
