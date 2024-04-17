from odmantic import Field, Model
from opinionated_mixins.contrib.odmantic.person import Person as ODMPerson
from typing_extensions import Optional


class Person(Model, ODMPerson):
    first_name: Optional[str] = Field(min_length=1, max_length=64)
    last_name: Optional[str] = Field(min_length=1, max_length=64)
