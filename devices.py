#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

import os
import time

while True:
    os.system("adb devices -l")
    time.sleep(5)