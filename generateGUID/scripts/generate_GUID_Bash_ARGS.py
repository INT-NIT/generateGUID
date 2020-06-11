#!/usr/bin/python
import sys
from generateGUID import generate_GUID


if len(sys.argv) > 1:

    if len(sys.argv) == 5:
        key = sys.argv[1]+sys.argv[2]+sys.argv[3]+sys.argv[4]
        guid=generate_GUID(key)
        print(guid))
    elif len(sys.argv) == 2:
        key = sys.argv[1]
        guid=generate_GUID(key)
        print(guid)

    else:
        print("mauvais nombre d'arguments: {}".format(len(sys.argv)))
