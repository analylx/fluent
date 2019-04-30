#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def getValidateCheckout(id17):
    weight=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]   
    validate=['1','0','X','9','8','7','6','5','4','3','2']  

    sum=0
    mode=0
    for i in range(0,len(id17)):
        sum = sum + int(id17[i])*weight[i]
    mode=sum%11
    return validate[mode]