#!/usr/bin/env python
import pytest
import unittest

from binary_search import binary_search


def test_binary_search():
    assert binary_search([], 3) is -1
    assert binary_search([1, 2], 3) is -1
    assert binary_search([1, 2, 3, 4], 3) is 2
    assert binary_search([1, 2, 3, 4, 5], 3) is 2
    assert binary_search([1, 2, 3, 4], 3) is 2
    assert binary_search([1, 2, 3, 4], 1) is 0
    assert binary_search([1, 2, 3, 4], 4) is 3


class TestBinarySearch(unittest.TestCase):

    def test_binary_search(self):
        self.assertEqual(binary_search([], 3), -1)
        self.assertEqual(binary_search([1, 2], 3), -1)
        self.assertEqual(binary_search([1, 2, 3, 4], 3), 2)
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(binary_search([1, 2, 3, 4], 3), 2)
        self.assertEqual(binary_search([1, 2, 3, 4], 1), 0)
        self.assertEqual(binary_search([1, 2, 3, 4], 4), 3)
