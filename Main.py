from typing import List

def selectionSort(array, size) -> List[int]:
  # Write your code here
  for i in range(len(data)):
    mim = data[i]
    for j in range(i+1, len(data)):
      mim = j
      data[mim] = data[i]
      data[i] = data[mim]

# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))
