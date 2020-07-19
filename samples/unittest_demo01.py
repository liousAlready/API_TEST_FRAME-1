#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: unittest_demo01.py
# @time: 2020/7/19 11:03 上午

import unittest

class TestDemo(unittest.TestCase):
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass

    def test_add1(self):
        self.assertEqual(1+2,3)

    def test_add2(self):
        self.assertEqual(2+3,5)

if __name__ == "__main__":
    unittest.main()
