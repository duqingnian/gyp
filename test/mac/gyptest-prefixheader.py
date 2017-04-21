#!/usr/bin/env python

# Copyright (c) 2012 Google Inc. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""
Verifies that GCC_PREFIX_HEADER works.
"""

import TestGyp

import sys

if sys.platform == 'darwin':
  test = TestGyp.TestGyp(formats=['ninja', 'make', 'xcode'])

  if test.format == 'xcode-ninja':
    test.skip_test(bug=527)

  test.run_gyp('test.gyp', chdir='prefixheader')

  test.build('test.gyp', test.ALL, chdir='prefixheader')
  test.pass_test()
