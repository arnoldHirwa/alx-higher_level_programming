#!/usr/bin/python3
"""A module that
Lists all State objects that contain the letter a from the database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    name = sys.argv[1]
    paswd = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine(f'mysql+mysqldb://{name}:{paswd}@localhost:3306/{db}',
                        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).filter(State.name.like('%a%')).all()

    for st in states:
        print(f'{st.id}: {st.name}')
