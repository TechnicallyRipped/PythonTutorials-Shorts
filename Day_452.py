

def compound_int_cal(p,r,n,t):
    r = r/100
    final_amount = p*(1+(r/n))**(n*t)
    return round(final_amount,2)

x = compound_int_cal(1000,5,12,3)
print(x)















