from sqlalchemy import Column, Integer, String
from DB.sample import Base

class User(Base):
    __tablename__= 'users'

    id= Column(Integer, primary_key= True)
    name= Column(String)
    fullname= Column(String)
    nickname= Column(String)
    def __repr__(self):
        return "<User (name='%s', fullname='%s', nickname='%s')>" % (
        self.name, self.fullname, self.nickname
        )

# which file will get this thing in use
# how this stuff will be gained by another file
