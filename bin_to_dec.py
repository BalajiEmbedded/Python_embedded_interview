def bin_to_dec(num):
    decimal,i=0,0
    while(num>0):
        dec=num%10
        decimal=decimal+dec*(2**i)
        num=num//10
        i+=1
    return decimal

res=bin_to_dec(10101)
print(res)
