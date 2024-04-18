# Copyright 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
# Copyright (C) 2024 <hasansezertasan@gmail.com>
from opinionated_mixins.contrib.pydantic import Person as PydanticPerson


class Person(PydanticPerson):
    """Beanie `Person` document that represents a person.

    Inherits from `opinionated_mixins.contrib.pydantic.person.Person`.
    """
