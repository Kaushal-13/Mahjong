from sqlalchemy import Integer, String, Column

import sys
sys.path.append("..")
from db.database import Base

class RoomDB(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)