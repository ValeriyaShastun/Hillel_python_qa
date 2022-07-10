from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

engine = create_engine('postgresql://vshastun:12345@localhost/store')

__session = sessionmaker(engine)

session: Session = __session()
