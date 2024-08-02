
def insertion_sort(elements):
  for i in range(1, len(elements)):
    anochor = elements[i]
    j = i -1

    while j>=0 and anochor < elements[j]:
      elements[j+1] = elements[j]
      j = j - 1
    elements[j+1] = anochor



if __name__ == '__main__':
  elements = [11,9,29,7,2,15,28]
  insertion_sort(elements)
  print(elements)