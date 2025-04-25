from sqlalchemy import select

from repositories.connection_manager import ConnectionManager
from repositories.repository import MutableRepository

class PlayerRepository(MutableRepository):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PlayerRepository, cls).__new__(cls)
        return cls._instance

    def delete(self, player):
        with ConnectionManager().session() as session:
            session.delete(player)

    def save(self, player):
        with ConnectionManager().session() as session:
            session.merge(player)
            session.merge(player.inventory)

    def get(self, identifier: str):
        from models.entity.player import Player
        with ConnectionManager().session() as session:
            return session.scalars(select(Player).filter_by(name=identifier)).first()

    def get_all(self):
        from models.entity.player import Player
        with ConnectionManager().session() as session:
            return session.scalars(select(Player)).all()