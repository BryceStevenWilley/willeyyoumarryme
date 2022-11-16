from app import login
from flask_login import UserMixin

class SessionUser(UserMixin):
  def __init__(self):
    self.id = 0

@login.user_loader
def load_user(id):
  return SessionUser()