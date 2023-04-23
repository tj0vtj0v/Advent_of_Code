import string
import os
inputfile = open(os.path.join(os.path.dirname(__file__), 'input_signal.txt'), "r")
inputsignal = str(inputfile.readlines())

signal = ""
for char in inputsignal:
  if char in string.ascii_lowercase:
    signal = signal + char

counter = 1
for char in signal:
  if counter >= 4:
    charlist = [signal[counter-1], signal[counter-2], signal[counter-3], signal[counter-4]]
    charlist = set(charlist)
    if len(charlist) ==4:
      print("start of first package marker: " + str(counter) + ", " + str(charlist))
      break
  counter+=1

counter = 1
for char in signal:
  if counter >= 4:
    charlist = [signal[counter-1], signal[counter-2], signal[counter-3], signal[counter-4], signal[counter-5], signal[counter-6], signal[counter-7], signal[counter-8], signal[counter-9], signal[counter-10], signal[counter-11], signal[counter-12], signal[counter-13], signal[counter-14]]
    charlist = set(charlist)
    if len(charlist) ==14:
      print("start of first message marker: " + str(counter) + ", " + str(charlist))
      break
  counter+=1