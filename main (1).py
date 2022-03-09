'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

print("Hello World")
def dt(arr,q):
    l1=[]
    x=len(arr)
    #pre=[0,0,0,0]
    pre=arr.copy()
    pre[0]=arr[0]
    for i in range(1,x):
        pre[i]=arr[i]^pre[i-1]
    print(pre)    
    for j in range(len(q)):
        l=q[j][0]
        r=q[j][1]
        print(l,r)
        if l==0:
            l1.append(pre[r])
        else:
            l1.append(pre[r]^pre[l-1])
    print(l1) 
    
dt([1,3,4,8],[[0,1],[1,2],[0,3],[3,3]])  
dt([4,8,2,10],[[2,3],[1,3],[0,0],[0,3]])