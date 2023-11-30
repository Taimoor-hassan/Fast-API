from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation


def session_acr(model, session):
    """
    This method manages the session of db write
    """
    session.add(model)
    try:
        session.commit()
    except IntegrityError as e:
        assert isinstance(e.orig, UniqueViolation)  # proves the original exception
        raise BadRequest from e
    # session.commit()
    session.refresh(model)
