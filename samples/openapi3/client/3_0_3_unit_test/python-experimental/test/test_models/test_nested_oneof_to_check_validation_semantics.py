# coding: utf-8

"""
    openapi 3.0.3 sample spec

    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""

import unittest

import unit_test_api
from unit_test_api.model.nested_oneof_to_check_validation_semantics import NestedOneofToCheckValidationSemantics
from unit_test_api import configuration


class TestNestedOneofToCheckValidationSemantics(unittest.TestCase):
    """NestedOneofToCheckValidationSemantics unit test stubs"""
    _configuration = configuration.Configuration()

    def test_anything_non_null_is_invalid_fails(self):
        # anything non-null is invalid
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            NestedOneofToCheckValidationSemantics._from_openapi_data(
                123,
                _configuration=self._configuration
            )

    def test_null_is_valid_passes(self):
        # null is valid
        NestedOneofToCheckValidationSemantics._from_openapi_data(
            None,
            _configuration=self._configuration
        )


if __name__ == '__main__':
    unittest.main()
