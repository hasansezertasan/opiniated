from sqlalchemy import Column
from sqlalchemy.orm import declarative_mixin
from sqlalchemy.sql.sqltypes import Date, String


@declarative_mixin
class Person:
    """
    SQLAlchemy `Person` model that represents a person.

    !!! note
        This class does not inherit from any base class and is not meant to be used directly.
    """

    first_name = Column(String(64), nullable=False)
    last_name = Column(String(64), nullable=False)
    middle_name = Column(String(64))
    phone = Column(String(64))
    email = Column(String(64))
    address = Column(String(64))
    postal_code = Column(String(64))
    city = Column(String(64))
    country = Column(String(64))
    date_birth = Column(Date)
    description = Column(String(64))
