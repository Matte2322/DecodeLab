from main import *

# Dictionary
replacement = {
  '^': 'as',
  '~': 'the',
  '+': 'and',
  '$': 'that',
  '&': 'must',
  '%': 'well',
  '#': 'these',
}

def decodingSymbols():
  global countOriginal
  global countOriginal1
  global choiceDecode
  global countDecode
  global countDecode1
  
  lines = []
  if choiceDecode == "Case0":
    with open('/home/runner/Doing-Stuff/test/testCase0.txt', 'r') as decodeCase0:
      for line in decodeCase0:
        for original, translate in replacement.items():
          line = line.replace(original, translate)
        lines.append(line)
    with open('/home/runner/Doing-Stuff/out/output0.txt', 'w') as output0:
      for line in lines:
        output0.write(line)
    print("Here is the decoded file: ")
    
    # increment case0
    with open('/home/runner/Doing-Stuff/out/output0.txt', 'r') as readput0:
      for charOuputCount in readput0.read():
        countDecode +=1
      readput0.close()
    with open('/home/runner/Doing-Stuff/out/output0.txt', 'r') as caseDecode0f:
      print()
      print(caseDecode0f.read())
      print()
      print(f'Character count after decode: {countDecode}')
      
  elif choiceDecode == "Case1":
    with open('/home/runner/Doing-Stuff/test/testCase1.txt', 'r') as decodeCase1:
      for line in decodeCase1:
        for original, translate in replacement.items():
          line = line.replace(original, translate)
        lines.append(line)
    with open('/home/runner/Doing-Stuff/out/output1.txt', 'w') as output1:
      for line in lines:
        output1.write(line)
    print("Here is the decoded file: ")

    # increment case1
    with open('/home/runner/Doing-Stuff/out/output1.txt', 'r') as readput1:
      for charOutputCount1 in readput1.read():
        countDecode1 +=1
      readput1.close()
    with open('/home/runner/Doing-Stuff/out/output1.txt', 'r') as caseDecode1f:
      print()
      print(caseDecode1f.read())
      print()
      print(f'Character count after decode: {countDecode1}')
    
decodingSymbols() 