#!/usr/bin/python3

import functions
from functions.functions import keyVerification

class Tests:
    def testKeyVerification():
        id = "A123456789"
        res = functions.keyVerification(id)
        print(res)

    testKeyVerification()