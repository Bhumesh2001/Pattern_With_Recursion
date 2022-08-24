# Q .1 
#  pattern with recursion

def pattern(i):
    global a,run,a1
    if i == 0:
        return 1
    else:
        def c(i,j):
            global run,a
            if j == run:
                return 1
            else:
                print(a,end=' ')
                a+=1
                c(i+1,j+1)
        c(0,i)
        print()
        a1+=1
        pattern(i-1)     
run,a,a1=int(input('enter the num :')),1,1
pattern(run)


# Q . 2
# pattern with recirsion

def p(i):
    global s,re
    if i == re:
        return 1
    else:
        print(' '*s,end='')
        s-=1
        print(((10*i-1)//9)*2)
        p(i+1)
re= int(input('enter the num :'))
s=re*1
p(1)


# Q . 3
# pattern with recursion

def pattern(i):
    global re,s,itr,a
    if i == re:
        return 1
    else:
        a=(i,i,(i+i)**2)
        def c(y):
            global a
            if y ==len(a):
                return 1
            else :
                print(a[y],end='')
                c(y+1)
        c(0)
        print()
        pattern(i+1)
re= int(input('enter the num :'))
s,itr=re*1,0
pattern(1)

# Q .4 
# snake pattern with recursion
 
def snk(i):
    global n,k,c,run,r,run2
    if run==0:return c
    else:
        run2=1*r
        def cal(j):
            global n,k,run2
            if run2==0:return run2
            else:
                print(n,"\t",end='')
                n+=k
                run2-=1
                cal(j-1)
        cal(1)
        if s %2==1:
            if i% 2==1:
                n=n+c-1
                k=-1
            else:
                n=n+c+1
                k=1
        else:
             if i% 2 !=1:
                n=n+c-1
                k=-1
             else:
                n=n+c+1
                k=1
        print()
        run-=1
        snk(i+1)
r=int(input('enter the range: '))
k,n,c,s,run=1,1,r,1*r,1*r
snk(r)


