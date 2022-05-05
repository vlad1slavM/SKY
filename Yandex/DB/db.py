import sqlite3
import os
from colorama import Fore
from collections import namedtuple
from typing import NamedTuple
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

DATABASE_NAME = 'fileDB'
DATABASE_TABLE_NAME = 'file'


class DataBase():
    def __init__(self):
        self.db_engine = create_engine(f"sqlite:///{DATABASE_NAME}.sqlite")

    def create(self) -> None:
        metadata = MetaData()
        file = Table(DATABASE_TABLE_NAME, metadata,
                     Column('id', Integer, primary_key=True),
                     Column('name', String),
                     Column('path', String),
                     Column('preview_link', String),
                     Column('md5', String),
                     Column('media_type', String), )
        try:
            metadata.create_all(self.db_engine)
        except Exception as e:
            print(e)

    def insert(self, name: str, path: str, preview_link: str, md5: str, media_type: str) -> None:
        # Insert Data
        query = f"INSERT INTO {DATABASE_TABLE_NAME} (name, path, preview_link, md5, media_type) " \
                f"VALUES ('{name}', '{path}', '{preview_link}', '{md5}', '{media_type}');"
        with self.db_engine.connect() as connection:
            try:
                connection.execute(query)
            except Exception as e:
                print(e)
