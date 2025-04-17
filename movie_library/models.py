from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Movie:
    _id: str
    title: str
    director: str
    year: int
    actors: list[str] = field(default_factory=list)
    series: list[str] = field(default_factory=list)
    last_watched: datetime = field(default_factory=datetime.today)
    rating: int = 0
    tags: list[str] = field(default_factory=list)
    description:str = None
    video_link: str = None

@dataclass
class User:
    _id: str
    email: str
    password: str
    registered_on: datetime = datetime.now()
    last_login: datetime = datetime.now()
    movies: list[Movie] = field(default_factory=list)