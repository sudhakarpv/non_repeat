# non_repeat
def main():
    pass
    n=input()
    inp=input().split()
    list_1=list(inp)
    list_2=[]
    for i in list_1:
        k=list_1.count(i)
        if (k==1):
            list_2.append(i)
        else:
            pass
    print(''.join(list_2))
if __name__ == '__main__':
    main()
