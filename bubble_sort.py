#bubble_sort.py
#make use of swapping - arranging an element in a particular location (bubbling up elemenent in a proper location)
#bubbling up - swapping

number=[66,57,54,53,64,52]
for i in range(len(number)):
  for j in range(len(number)-1-i):
    if number[j]>number[j+1]:
      number[j],number[j+1]=number[j+1],number[j]

print("Best Time : ",number[0])
