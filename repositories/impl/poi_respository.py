from levels.pois.poi import Poi
from repositories.repository import ImmutableRepository


class PoiRepository(ImmutableRepository[int, Poi]):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PoiRepository, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        super(PoiRepository, self).__init__()
        pass