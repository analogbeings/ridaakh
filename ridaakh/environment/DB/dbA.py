from sqlalchemy import Column, Integer, String
from DB.sample import Base

class UserA(Base):
    __tablename__ == 'usersA'
    name= Column(string)
    nickname= Column(String)


    def __repr__(self):
        return "<User (name='%s', fullname='%s', nickname='%s')>" % (
        self.name, self.fullname, self.nickname
        )
