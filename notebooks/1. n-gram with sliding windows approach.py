# Please refers to this notebook for time complexity analysis
https://github.com/SaPhyoThuHtet/data-structure-and-algos/blob/main/useful
a = ['▁', 'al', 'p', '▁ဗိုလ်', 'ချူပ်', 'တေ', '▁လမ်း', 'စဉ်', 'သည်', '▁ရခိုင်ပြည်', '▁', 'လွတ်လပ်ရေး', '▁', 'အတွက်', 'ဦး', 'တည်', 'သည်။']
k = 3
prev = a[0:k]
#print(''.join([str(elem) for elem in prev]))

for i in range(k-1,len(a)):
  print(prev)
  print(''.join([str(elem) for elem in prev]))
  if (i+1 < len(a)):
      prev = prev[1:]+[a[i+1]]
