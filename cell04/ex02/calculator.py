#!/usr/bin/env python
first=int(input("Give me the first number: "));
sec=int(input("Give me the second number:"));
print("Thank you!");
cal=["+","-","/","x"];
result=[first+sec,first-sec,int(first/sec),first*sec];
x=0;
for i in cal:
    print(f"{first} {i} {sec} = {result[x]}");
    x+=1;