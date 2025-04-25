from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from contextlib import contextmanager

from repositories.savable import Storable

class ConnectionManager:
    _instance = None
    _engine = None
    _initialized = False
    _SessionFactory: sessionmaker = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConnectionManager, cls).__new__(cls)
        return cls._instance

    def initialize(self):
        if not self._initialized:
            self._engine = create_engine("sqlite:///data.db", pool_size=5, pool_recycle=3600)
            self._SessionFactory = sessionmaker(self._engine)
            self._initialized = True
            Storable.metadata.create_all(self._engine)

    @contextmanager
    def session(self) -> Generator[Session]:
        """context manager to simplify session lifecycle"""
        if not self._initialized:
            raise Exception("Connection Manager is not initialized. Please call 'initialize' first.")

        with self._SessionFactory() as session:
            try:
                yield session
                session.commit()
            except Exception as e:
                print(f"Exception during commit: {e}")
                session.rollback()
            finally:
                session.close()

    def shutdown(self):
        """clean up resources and shut down the connection manager"""
        if not self._initialized:
            raise Exception("Connection Manager is not initialized.")

        self._SessionFactory.close_all()
        self._engine.dispose()
        self._initialized = False
