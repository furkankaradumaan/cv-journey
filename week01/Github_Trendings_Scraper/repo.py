"""
This file defines an article class to represent
a Github article.
"""

from dataclasses import dataclass, field
from functools import wraps
import types

class InvalidAttributeError(Exception):
    """
    This expection raised when a GithubRepo object
    is tried to instantiate with invalid parameters.
    """
    pass

@dataclass(slots=True)
class GithubRepo:
    """
    This class represents information about a Github repository.
    """
    owner: str = field(default=None) # Username of the owner
    repo_name: str = field(default=None) # Repository name
    description: str = field(default=None) # The description line of Repo
    language: str = field(default=None) # Mostly used programming language
    stars: int = field(default=None) # Number of stars the repository have.
    forks: int = field(default=None)
    
    def __post_init__(self):
        """
        Checks the instance variables of the objet and validates them.
        """
        # Firstly, we need to loop over the instance variables
        for attribute_name in self.__slots__:
            attribute_value = self.__getattribute__(attribute_name) # Get the value of the attribute
            attribute_type = type(attribute_value) # Find the attribute type
            expected_type = self.__annotations__.get(attribute_name, None) # Get the expected type for attribute.
                                                                          # None if expected type is not specified.

            if isinstance(expected_type, types.UnionType): # If the type is UnionType, it means there is
                                                           # more than one possible types for the attribute.
                if attribute_type not in expected_type.__args__: # Search the expected types in all possible types.
                    raise InvalidAttributeError(f"{attribute_name} is type of {attribute_type.__name__}."
                                                 f"Expected type is one of {expected_type}.")
            elif isinstance(expected_type, type): # If the expected_type object is just a single type
                                                  # compare the type with the type of attribute.
                if attribute_type != expected_type:
                    raise InvalidAttributeError(f"{attribute_name} is type of {attribute_type.__name__}."
                                                f"Expected type is {expected_type}.")

        # Now we will check the lengths of the inputs.
        # The string type objects have to be at least 1 character except blanks.
        if len(self.owner.strip()) == 0:
            raise InvalidAttributeError("Owner name must be at least one character long.")
        if len(self.repo_name.strip()) == 0:
            raise InvalidAttributeError("Repository name must be at least one character long.")
        
        #  Validate stars and forks.
        if self.stars < 0:
            raise InvalidAttributeError("Stars cannot be negative.")
        if self.forks < 0:
            raise InvalidAttributeError("Shares cannot be negative.")

    def to_dict(self):
        """
        Writes the object into a dictionary and returns it.
        """
        dict_ = dict()
        
        # Loop through the instance attributes in specified in __slots__ variable.
        for attribute_name in self.__slots__:
            attribute_value = self.__getattribute__(attribute_name)
            assert attribute_value is not None, "Attribute {attribute_name} is None" # Attribute value cannot be None.
            dict_[attribute_name] = attribute_value # Put the key-value pair into dict.

        return dict_
