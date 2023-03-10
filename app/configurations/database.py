from typing import Optional, Dict, Any

from sqlalchemy.engine import Engine, Result
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine
from os import getenv


class Database:

    __engine = None

    def get_engine(self) -> Engine:
        if self.__engine is None:
            database_url = getenv("DATABASE_URL")
            self.__engine = create_engine(database_url, pool_pre_ping=True, pool_size=20, echo=False)
        return self.__engine

    def get_session(self) -> Session:
        session = sessionmaker(bind=self.get_engine())
        return session()

    def execute(
            self,
            query: str,
            params: Optional[Dict[str, Any]] = None
    ) -> Result:
        session = self.get_session()

        if params is not None:
            result = session.execute(query, params=params)
        else:
            result = session.execute(query)
        session.commit()

        return result


database = Database()
