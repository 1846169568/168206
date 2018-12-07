#斐波那契数
def fa(n):
    if n==1:
        return [1]
    if n==2:
        return [1,1]
    list=[1,1]
    for i in range(2,n):
        list.append(list[-2]+list[-1])
    return list
if __name__=="__main__":
    x=int(input("请输入需要求个数："))
    print(fa(x))