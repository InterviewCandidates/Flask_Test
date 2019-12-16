from datetime import datetime

from .model import Interviewee, Interview
from . import db


def do_setup():
    interviewees = [{"name": "Arnold Palmer"},
                    {"name": "George Washington"},
                    {"name": "Thomas Jefferson"},
                    {"name": "Abraham Lincoln"},
                    {"name": "James Madison"}]

    interviews = [{"room_name": "Room 1",
                   "time": datetime.strptime("2019-01-01 16:30", '%Y-%m-%d %H:%M'),
                   "interviewer1_id": 2,
                   "interviewer2_id": 3,
                   "interviewee_id": 1},
                  {"room_name": "Room 2",
                   "time": datetime.strptime("2019-01-02 13:30", '%Y-%m-%d %H:%M'),
                   "interviewer1_id": 3,
                   "interviewer2_id": 1,
                   "interviewee_id": 2},
                  {"room_name": "Room 1",
                   "time": datetime.strptime("2019-01-02 14:00", '%Y-%m-%d %H:%M'),
                   "interviewer1_id": 4,
                   "interviewer2_id": 1,
                   "interviewee_id": 3},
                  {"room_name": "Room 3",
                   "time": datetime.strptime("2019-01-02 16:00", '%Y-%m-%d %H:%M'),
                   "interviewer1_id": 2,
                   "interviewer2_id": 5,
                   "interviewee_id": 4},
                  {"room_name": "Room 1",
                   "time": datetime.strptime("2019-01-03 14:30", '%Y-%m-%d %H:%M'),
                   "interviewer1_id": 4,
                   "interviewer2_id": 5,
                   "interviewee_id": 5}
                  ]

    db.create_all()

    for interviewee in interviewees:
        new_interviewee = Interviewee(**interviewee)
        db.session.add(new_interviewee)
        db.session.commit()

    for interview in interviews:
        new_interview = Interview(**interview)
        db.session.add(new_interview)
        db.session.commit()
