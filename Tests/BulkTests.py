# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import unittest

# Custom data

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class BulkTests(unittest.TestCase):
    def Subtest_Equality(self,cases):
        for left, right in cases:
            with self.subTest(left=left, right=right):
                self.assertEqual(left, right)

    def Subtest_Fail(self, ObjectType:type, cases):
        for value, error in cases:
            with self.subTest(ObjectType=ObjectType,value=value, error=error):
               with self.assertRaises(error):
                    ObjectType(value)

    def Subtest_ObjectOperation(self, ObjectType:type, args:tuple, kwargs:dict, cases):
        for operation, oArgs, oKwargs,result in cases:
            with self.subTest(ObjectType=ObjectType, args=args, kwargs=kwargs, oArgs=oArgs, oKwargs=oKwargs,result=result, ):
                test_object = ObjectType(*args, **kwargs)
                self.assertEqual(operation(test_object, *oArgs, *oKwargs), result)