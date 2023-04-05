"""
author = MoYeRanQianZhi
version = 1.0.0
Python = 3.10.10
license = MIT
"""
# MIT License
#
# Copyright (c) 2023 MoYeRanQianZhi
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys

from .term import *


def draw(data, version=1, box=1, border=1):
    sys.stdout.write(
        simpleQR(data=data, version=version, box=box, border=border)
    )
    sys.stdout.flush()


def printQR(data, version=1, box=1, border=1):
    print(
        simpleQR(data=data, version=version, box=box, border=border)
    )


initialize()

if __name__ == '__main__':
    draw('https://www.google.com')
    print('\n' + '-' * 64 + '\n')
    printQR(data='GoodLuck', version=3, border=0)
