import sys
args = sys.argv

aa,bb=int(args[1][:-1]),int(args[2])
print(aa,type(aa),bb,type(bb))
def gugu(a,b):
    for i in range(a,a+b):
        print(f"====={a}단=====")
        for j in range(1,10):
            print(f'{i} x {j} = {i*j}')
gugu(aa,bb)