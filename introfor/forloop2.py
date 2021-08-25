#!/usr/bin/env python3
"""RZFeeser | Alta3 Research
   nesting an if-statement inside of a for loop"""

# create a list of strings
vendorsList = ["cisco", "juniper", "big_ip", "f5", "arista", "alta3", "zach", "stuart"]
# create a second list of strings
approved_vendorsList = ["cisco", "juniper", "big_ip"]
# loop across the list called vendors
for vendor in vendorsList:
    print("\nThe vendor is " + vendor, end="")   # newline, print current vendor, and end without newline
    if vendor not in approved_vendorsList:   # if x does not appear within the list approved_vendors
        print(" - NOT AN APPROVED VENDOR!", end="")
print("\nOur loop has ended.") # print when loop has finished

