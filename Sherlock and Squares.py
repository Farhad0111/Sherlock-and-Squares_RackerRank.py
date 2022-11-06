class Farhad:
    def faru(self,t):
        for i in range(0,t):
            a, b = [int(j) for j in input().strip().split()]  # taking input in a and b
            # strip() is used to remove the extra spaces
            # split() is used to split the input into two parts
            # int() is used to convert the input into integer
            root=a**(0.5)
            #print(root)
            if(root!=int(root)):
                c=int(root)+1
                #print(root)
            else:
                c=int(root)
            root2=b**(0.5)
            d=int(root2)
            print(d-c+1)
farhad =Farhad()
farhad.faru(int(input()))
