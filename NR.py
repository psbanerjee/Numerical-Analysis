def fx(x):
    return pow(x,3)-12.0

def dfx(x):
    return 3.0*pow(x,2)

def NR_iter(xn):
    return (xn - (fx(xn)/dfx(xn)))

x0=2.5
x1 = NR_iter(x0)
while abs(x1-x0)>1e-100:
    x0 = x1
    x1 = NR_iter(x1)
print("The root is : {x1:2.3f}".format(x1=x1))
