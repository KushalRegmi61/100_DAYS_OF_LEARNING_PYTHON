list = []
cond = True
while cond:
  name = input("enter the bidder name: \n")
  bid_amount = int(input("enter the bid amount:"))

  list.append({'b_n': name, 'b': bid_amount})
  # dict.clear()
  c = input("do you want to continue(Y/N)")
  if c == "n":
    cond = False

a = 0
for i in range(0, len(list)):
  for j in range(1, len(list)):
    if list[i]["b"]>list[j]["b"]:
      a = i
    else:
      a = j
print("The winner is",list[a]["b_n"],"with the bid amount of", list[a]["b"] )          
    