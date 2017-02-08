#!/usr/bin/python

# storecredit.py

test_case = int(input())  # read a line with a single integer

for i in range(test_case):
    credit = int(input())
    numprod = int(input())
    pricelist = input().split()
    intpriceL = [int(j) for j in pricelist]
    count = 1

    for i in range(len(intpriceL)):
        count += 1
        if (credit - intpriceL[i]) in intpriceL:
            print(i + 1, end=',')
            if (credit - intpriceL[i]) in intpriceL[i+1:]:
                print(intpriceL[i+1:].index(credit - intpriceL[i]) + count)
                break

