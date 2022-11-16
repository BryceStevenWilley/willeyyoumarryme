from app import db

class User(db.Model):
  uid = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String(64))
  last_name = db.Column(db.String(64))
  title = db.Column(db.String(10))
  group_id = db.Column(db.Integer, db.ForeignKey('group.gid'))
  has_plus_one = db.Column(db.Boolean)
  customized_note = db.Column(db.String)

  def __repr__(self):
    return f'<User {self.uid} {self.first_name} {self.last_name}>'

class Group(db.Model):
  gid = db.Column(db.Integer, primary_key=True)
  addr_str = db.Column(db.String)
  addr_unit = db.Column(db.String(64))
  invite_to_rehearsal_dinner = db.Column(db.Boolean)

  def __repr__(self):
    return f'<Group {self.gid}>'

  def get_addr(self):
    if not self.addr_unit:
      return self.addr_str
    else:
      return f'{self.addr_str}, {self.addr_unit}'

class GroupResp(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  gid = db.Column(db.Integer, db.ForeignKey('group.gid'))
  addr_city = db.Column(db.String(64))
  addr_state = db.Column(db.String(20))
  addr_zip = db.Column(db.String(10))
  addr_country = db.Column(db.String(40))

  def __repr__(self):
    return f'<GroupResp {self.gid} {self.addr_city} {self.addr_zip}>'

class UserResp(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  date_submitted = db.Column(db.DateTime)
  uid = db.Column(db.Integer, db.ForeignKey('user.uid'))
  rsvp_wedding = db.Column(db.Boolean)
  rsvp_rehearsal = db.Column(db.Boolean) # ask for after meal stuff, so not confusing
  covid_ack = db.Column(db.Boolean)
  meal = db.String(db.String)
  dietary_restricions = db.Column(db.String)
  cell = db.Column(db.String(12))# optional
  general_note = db.Column(db.String) # optional

  def __repr__(self):
    return f'<UserResp {self.uid} {self.rsvp_wedding} {self.rsvp_rehearsal} {self.general_note}>'

