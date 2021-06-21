import random
from model.project import Project


def test_delete_some_project(app, db):
    if len(db.get_project_list()) == 0:
        app.project.create_project(Project(name="test", description="test test test"))
    old_projects = db.get_project_list()
    pr = random.choice(old_projects)
    app.project.delete_project_by_id(pr.id)
    new_projects = db.get_project_list()
    old_projects.remove(pr)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)


