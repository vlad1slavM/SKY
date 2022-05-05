import logging

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData

DATABASE_NAME = 'fileDB'
DATABASE_TABLE_NAME = 'file'


class DataBase:
    def __init__(self):
        self.db_engine = create_engine(f"sqlite:///{DATABASE_NAME}.sqlite")
        self._metadata = MetaData()
        logging.basicConfig(filename='../Yandex/log.log', level=logging.DEBUG)
        self.file = Table(DATABASE_TABLE_NAME, self._metadata,
                          Column('id', Integer, primary_key=True),
                          Column('name', String),
                          Column('path', String, unique=True),
                          Column('preview_link', String),
                          Column('md5', String),
                          Column('media_type', String), )

    def create(self) -> None:
        try:
            self._metadata.create_all(self.db_engine)
        except Exception as e:
            logging.error(e)

    def insert(self, name: str, path: str, preview_link: str, md5: str, media_type: str) -> None:
        # Insert Data
        insert = self.file.insert().values(name=name, path=path, preview_link=preview_link,
                                           md5=md5, media_type=media_type)
        with self.db_engine.connect() as connection:
            try:
                connection.execute(insert)
            except Exception as e:
                logging.error(e)
