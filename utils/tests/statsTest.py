#!/usr/bin/env python
"""
    Copyright 2012 Denys Sobchyshak

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
__author__ = "Denys Sobchyshak"
__email__ = "denys.sobchyshak@gmail.com"

import stats

import random
import unittest

class StatsTestCase(unittest.TestCase):

    def setUp(self):
        self.data = [10, 20, 1, 0, 50, 4, 100, 8, 3, 60]

        self.arithmeticMean = 25
        self.population_variance = 1014
        self.sample_variance = 422.25

    def tearDown(self):
        self.data = []
        self.arithmeticMean = 0
        self.population_variance = 0
        self.sample_variance = 0

    def testAverage(self):
        self.assertEquals(self.arithmeticMean, stats.arithmeticMean(self.data))

    def testVariance(self):
        self.assertEquals(self.population_variance, stats.variance(self.data, True))
        self.assertEquals(self.sample_variance, stats.variance(self.data[:len(self.data)/2]))
