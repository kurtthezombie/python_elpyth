from os import system

def inputnum():
  while True:
    try:
      n:int = int(input("Input(1..10): "))
      if n in range(1,11):
        break
    except:
      print("Invalid input!")
      continue
    print("Invalid input!")
  return n


def table(n):
  x = 0
  while x < n:
    y = 0
    while y<n:
      r = (x+y)%n
      print(r+1, end = " ")
      y += 1
    print()
    x += 1

def main():
  table(inputnum())

if __name__ == "__main__":
    main()