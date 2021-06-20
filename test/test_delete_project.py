def test_delete_project(app):
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")