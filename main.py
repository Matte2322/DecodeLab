# Kendon Beltran & Matthew Chen

print("Case0, Case1")

choiceDecode = input("Which text file would you like to decode? Type the words above to choose: ")
  
countOriginal = 1
countOriginal1 = 1
countDecode = 1
countDecode1 = 1

def case0(decide):
  global countOriginal
  if decide == "Case0":
    with open('/home/runner/Doing-Stuff/test/testCase0.txt','r') as case0:
      for charCount in case0.read():
        countOriginal += 1
      case0.close()
    with open('/home/runner/Doing-Stuff/test/testCase0.txt', 'r') as case0f:
      print()
      print(case0f.read())
      print()
      print("Characters in total: "+ str(countOriginal))
      case0.close()

def case1(decode):
  global countOriginal1
  if decode == "Case1":
    with open('/home/runner/Doing-Stuff/test/testCase1.txt', 'r') as case1:
      for charCount1 in case1.read():
        countOriginal1 += 1
      case1.close()
    with open('/home/runner/Doing-Stuff/test/testCase1.txt', 'r') as case1f:
      print()
      print(case1f.read())
      print()
      print("Characters in total: "+ str(countOriginal1))
      case1.close()

case0(choiceDecode)
case1(choiceDecode)

