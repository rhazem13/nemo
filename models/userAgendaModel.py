from models.db import db,Base



class UserAgenda (db.Model,Base):
    __tablename__ = "agenda"
    id = db.Column(db.Integer, primary_key=True)
    date= db.Column(db.DateTime(timezone=True))
    occasion = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))