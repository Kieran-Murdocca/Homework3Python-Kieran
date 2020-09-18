# Author: Kieran Murdocca kkm5754@psu.edu
# Collaborator: Peter Schulman pks5481@psu.edu

def digit_sum(n): 
  if n==0: 
    return 0
  elif n<0: 
    return "out of domain."
  return (n % 10 + digit_sum(int(n/10)))

def run(): 
  n=int(input("Enter an int: "))
  print(f"sum of digits of {n} is {digit_sum(n)}")

  

if __name__ == "__main__": 
  run()