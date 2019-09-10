from app import create_app,db
from flask import Flask, session
from app.auth.templates.models import User


if __name__ == '__main__':

    flask_app = create_app('prod')
    flask_app.secret_key = 'super secret key'
    flask_app.config['SESSION_TYPE'] = 'filesystem'
    with flask_app.app_context():
        db.create_all()
        if not User.query.filter_by(user_name='harry').first():
            User.create_user(user='harry',
                             email='harry@gmail.com',
                             password='secret')
    flask_app.run()
