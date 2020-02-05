from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.pool import NullPool


dburl = 'sqlite:///test.db'

engine = create_engine(dburl, echo=False, poolclass=NullPool)

# Session = scoped_session(sessionmaker(bind=engine))
Session = sessionmaker(bind=engine)
