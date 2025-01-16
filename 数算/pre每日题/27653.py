a=list(map(int,input().split()))
mom=a[1]*a[3]
son=a[0]*a[3]+a[1]*a[2]

#约分，找分子分母的最大公因数
#欧几里得算法：两个数a和b的最大公因数等于b和a%b（a除以b的余数）的最大公因数。
def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

gcd_ms=gcd(mom,son)
mom//=gcd_ms
son//=gcd_ms
print(f'{son}/{mom}')