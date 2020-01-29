# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testEquilateral(self): # test equilateral triangle
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 is an Equilateral triangle')
        self.assertNotEqual(classifyTriangle(2,2,3),'Equilateral','2,2,3 is not an Equilateral triangle')
        self.assertNotEqual(classifyTriangle(-1,-1,-1),'Equilateral','-1,-1,-1 is not an Equilateral triangle')
        self.assertNotEqual(classifyTriangle(0,0,0),'Equilateral','0,0,0 is not an Equilateral triangle')
        self.assertNotEqual(classifyTriangle(2.5,2.5,2.5),'Equilateral','2.5,2.5,2.5 is not an Equilateral triangle')
        self.assertNotEqual(classifyTriangle('a','a','a'),'Equilateral','a,a,a is not an Equilateral triangle')

    def testIsosceles(self): # test Isosceles triangle
        self.assertEqual(classifyTriangle(2,2,3),'Isosceles','2,2,3 is an Isosceles triangle')
        self.assertEqual(classifyTriangle(6,7,6),'Isosceles','6,7,6 is an Isosceles triangle')
        self.assertEqual(classifyTriangle(4,3,3),'Isosceles','4,3,3 is an Isosceles triangle')
        self.assertNotEqual(classifyTriangle(2,2,-3),'Isosceles','2,2,-3 is not an Isosceles triangle')
        self.assertNotEqual(classifyTriangle(-2,-2,-3),'Isosceles','-2,-2,-3 is not an Isosceles triangle')
        self.assertNotEqual(classifyTriangle(0,0,1),'Isosceles','0,0,1 is not an Isosceles triangle')
        self.assertNotEqual(classifyTriangle('a','a','b'),'Isosceles','a,a,b is not an Isosceles triangle')

    def testRight(self): # test right triangle
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
        self.assertEqual(classifyTriangle(6,8,10),'Right','6,8,10 is a Right triangle')
        self.assertNotEqual(classifyTriangle(3,4,-5),'Right','3,4,-5 is not a Right triangle')
        self.assertNotEqual(classifyTriangle(-6,-8,-10),'Right','-6,-8,-10 is not a Right triangle')
        self.assertNotEqual(classifyTriangle(0,1,1),'Right','0,1,1 is not a Right triangle')

    def testScalene(self): # test scalene triangle
        self.assertEqual(classifyTriangle(2,3,4),'Scalene','2,3,4 is a Scalene triangle')
        self.assertEqual(classifyTriangle(7,6,5),'Scalene','7,6,5 is a Scalene triangle')
        self.assertEqual(classifyTriangle(8,9,10),'Scalene','8,9,10 is a Scalene triangle')
        self.assertEqual(classifyTriangle(2,3,4),'Scalene','2,3,4 is a Scalene triangle')
        self.assertNotEqual(classifyTriangle(6,7,-8),'Scalene','6,7,-8 is not a Scalene triangle')
        self.assertNotEqual(classifyTriangle(-9,-10,-11),'Scalene','-9,-10,-11 is not a Scalene triangle')

    def testNotATriangle(self): # test invalid triangle and bad input
        self.assertEqual(classifyTriangle(1,1,10),'NotATriangle','1,1,10 is NotATriangle')        
        self.assertEqual(classifyTriangle(1,3,5),'NotATriangle','1,3,5 is NotATriangle')
        
    def testInvalidInput(self):
        self.assertEqual(classifyTriangle(1,3,0),'InvalidInput','1,3,0 is InvalidInput')
        self.assertEqual(classifyTriangle(0,0,0),'InvalidInput','0,0,0 is InvalidInput')
        self.assertEqual(classifyTriangle(-2,3,-4),'InvalidInput','-2,3,-4 is InvalidInput')        
        self.assertEqual(classifyTriangle(-1,3,5),'InvalidInput','-1,3,5 is InvalidInput')
        self.assertEqual(classifyTriangle('a','b','c'),'InvalidInput','a,b,c is InvalidInput')
        self.assertEqual(classifyTriangle('','',''),'InvalidInput','<no input> is InvalidInput')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

