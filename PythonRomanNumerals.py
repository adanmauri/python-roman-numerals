#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @license
# Copyright 2017 Adán Mauri Ungaro <adan.mauri@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

def deromanize(number):
    number = number.upper().replace(" ", "")
    numerals = { 1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I" }
    result = 0
    for value in sorted(numerals, reverse=True):
        key = numerals[value]
        while (number.find(key) == 0):
            result += value
            number = number[len(key):]   
    return result
    
def romanize(number):
    numerals = { 1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I" }
    result = ""
    for value in sorted(numerals, reverse=True):
        key = numerals[value]
        result += key*(number / value)
        number %= value;
        
    return result
