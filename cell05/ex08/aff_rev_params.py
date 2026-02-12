import sys
if(len(sys.argv)>=3):
    for i in range (len(sys.argv)-1):
        text=sys.argv[-(i+1)].lower();
        print(f"{text}",end=" ");
else:
    print("none");