#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def main():
    print "Welcome to the Lottery numbers generator"
    st_stevilk = int(raw_input("Please enter how many random numbers would you like to have:"))
    loto = []

    while True:
        if len(loto) == st_stevilk:
            break
        else:
            stevilo = random.randint(1,39)
            if stevilo not in loto:
                loto.append(stevilo)


    print loto
    print "End"

if __name__ == '__main__':
    main()
