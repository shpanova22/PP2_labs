#Bitwise operators
#1
print(6 & 3)#Output:2
#Operator  & compares each bit and set it to 1 if both are 1, otherwise it is set to 0

#2
print(6 | 3)#Output:7
#The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0

#3
print(6 ^ 3) #Output:5
#The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0

#4
print(~3) #Output:-4
#The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0)

#5
print(3 << 2)#output:12

'''
The << operator inserts the specified number of 0's (in this case 2) from the right and let the same amount of leftmost bits fall off:

If you push 00 in from the left:
 3 = 0000000000000011
becomes
12 = 0000000000001100 '''

#6
print(8 >> 2)#Output:2

'''
The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.

If you move each bit 2 times to the right, 8 becomes 2:
 8 = 0000000000001000
becomes
 2 = 0000000000000010'''
 
'''
 
()	                                            Parentheses	
**	                                            Exponentiation	
+x  -x  ~x	                                    Unary plus, unary minus, and bitwise NOT	
*  /  //  %	                                    Multiplication, division, floor division, and modulus	
+  -	                                        Addition and subtraction	
<<  >>	                                        Bitwise left and right shifts	
&	                                            Bitwise AND	
^	                                            Bitwise XOR	
|	                                            Bitwise OR	
==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
not	                                            Logical NOT	
and	                                            AND	
or	                                            OR
'''