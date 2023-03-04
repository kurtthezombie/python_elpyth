from os import system

num:list = []

def inputnum():
    count = 0
    for x in range(0,5):
        while True:
            try:
                count+=1
                n:int = int(input(f"Enter value {count} (1..100): "))
                if(1<=n<=100):
                    break
            except:
                print("Invalid input, 1-100 only!")
                continue
            print("Invalid input, 1-100 only!")
        num.append(n)
    return num

def mysum():
    sum:int = 0
    for x in num:
        sum += x
    return sum

def mymean(sum):
    return sum/5

def mymedian():
    num.sort()
    return num[5//2]

def mymode():
    mode = None
    maxcount = 0
    for x in num:
        count = 1
        for y in range (x+1, len(num)):
            if num[x] == num[y]:
                count+=1
            if count > maxcount:
                maxcount = count
                mode = num[x] 
    return mode

def main():
    inputnum()
    print("Sum:", mysum())
    print("Mean:", mymean(mysum()))
    print("Median:", mymedian())
    print("Mode:", mymode())

if __name__ == "__main__":
    main()