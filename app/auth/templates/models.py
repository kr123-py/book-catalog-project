from datetime import datetime

#from pip._vendor.urllib3.packages.rfc3986.validators import check_password

from app import db
from flask_login import UserMixin
from app import login_manager
#from passlib.hash import sha256_crypt


class User(UserMixin, db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20))
    user_email = db.Column(db.String(60), unique=True, index=True)
    user_Password = db.Column(db.String(20))
    registration_date = db.Column(db.DateTime, default=datetime.now)

    #def check_password(self,password):
      #  return sha256_crypt.check_password(self.user_Password,password)

    @classmethod
    def create_user(cls, user, email, password):
        user = cls(user_name=user,
                   user_email=email,
                   user_Password=password)
        db.session.add(user)
        db.session.commit()

        return user


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
