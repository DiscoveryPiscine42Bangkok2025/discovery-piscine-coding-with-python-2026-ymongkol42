#!/usr/bin/env python
print("Enter the first number:");
first_num =int(input());
print("Enter the second number:");
sec_num = int(input());
sub = first_num*sec_num;
print(f"{first_num} × {sec_num} = {sub}");

if(sub>0):
    print("This result is positive.");
elif(sub<0):
    print("This result is negative.");
else:
    print("This result is both positive and negative.");