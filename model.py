from . import db


class Interviewee(db.Model):
    """
    This class contains the interviewee information
    """
    __tablename__ = 'Interviewee'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))

    def __repr__(self):
        return f'<Interviewer_Name: {self.name}>'


class Interview(db.Model):
    """
    This class contains the interview schedule information
    """
    __tablename__ = 'Interview'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    room_name = db.Column(db.String(255))
    time = db.Column(db.DateTime)
    interviewer1_id = db.Column(db.Integer)
    interviewer2_id = db.Column(db.Integer)
    interviewee_id = db.Column(db.Integer, db.ForeignKey('Interviewee.id'))
    interviewee = db.relationship('Interviewee')

    def __repr__(self):
        return f'<Interview_id: {self.id}>'
