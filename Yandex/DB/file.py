from sqlalchemy import Column, INTEGER, String
from Yandex.DB.db import Base


class File(Base):
    __tablename__ = 'file'

    id = Column(INTEGER, primary_key=True)
    name = Column(String)
    path = Column(String)
    path_preview = Column(String)
    md5 = Column(String)
    media_type = Column(String)
