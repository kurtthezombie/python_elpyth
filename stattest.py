from os import system

num:list = []

def mymedian()->int:
  num.sort()
  no:int = len(num)
  if no%2==0:
    median1 = num[no//2]
    median2 = num[no//2-1]
    return (median1+median2)//2
  else:
    return num[no//2]

def mymode()->int:
  mode:int = -1
  count:int = 0
  for item in num:
    c:int = num.count(item)
    if c>count:
      mode = item
      count = c
    return mode

def mymean()->int:
  return mysum()/len(num)

def mysum()->int:
  sum:int = 0
  for item in num:sum += item
  return sum

def mydisplay()->None:
  [print(num[index], end=" ")for index in range(len(num)-1,-1,-1)]
  print()

def main()->None:
  system("cls")
  for i in range(0,5):
    val:int = int(input("Enter value(1..100): "))
    num.append(val)
  mydisplay()
  print(f"The total sum = {mysum()}")
  print(f"The mean = {mymean():.4}")
  print(f"The median = {mymedian()}")
  print(f"The mode = {mymode()}")

if __name__ == "__main__":
  main()