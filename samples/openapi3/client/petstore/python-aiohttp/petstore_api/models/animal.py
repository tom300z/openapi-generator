# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union
from pydantic import BaseModel, StrictStr
from pydantic import Field
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Animal(BaseModel):
    """
    Animal
    """
    class_name: StrictStr = Field(alias="className")
    color: Optional[StrictStr] = 'red'
    __properties: ClassVar[List[str]] = ["className", "color"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[List[str]] = 'className'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Union[Dict[str, str], None]] = None

    @classmethod
    def _get_discriminator_value_class_map(cls) -> ClassVar[Dict[str, str]]:
        if cls.__discriminator_value_class_map == None:
            # Prevent circular imports caused by mutually referencing classes
            from petstore_api.models.cat import Cat
            from petstore_api.models.dog import Dog

            cls.__discriminator_value_class_map = {
                'Cat': Cat,'Dog': Dog
            }
        return cls.__discriminator_value_class_map

    @classmethod
    def get_discriminator_value(cls, obj: dict) -> str:
        """Returns the discriminator value (object type) of the data"""

        discriminator_value = obj[cls.__discriminator_property_name]
        if discriminator_value:
            return cls._get_discriminator_value_class_map().get(discriminator_value)
        else:
            return None

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Union[Self, Self]:
        """Create an instance of Animal from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Union[Self, Self]:
        """Create an instance of Animal from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type:
            klass = globals()[object_type]
            return klass.from_dict(obj)
        else:
            raise ValueError("Animal failed to lookup discriminator value from " +
                             json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                             ", mapping: " + json.dumps(cls._get_discriminator_value_class_map()))


