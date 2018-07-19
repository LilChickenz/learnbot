import random
q=['hi', 'how are you']
a=['hello', 'good']
num=()
say='hi'
turn=2
print('q: hi')
a.append(input('a: '))
while True:
  if turn % 2 == 0:
    response=input('q: ')
    if response in q:
      print('a: ',a[q.index(response)])
    else:
      q.append(response)
      print('a: ?')
  else:
    num=random.randint(0, len(q)-1)
    print('q: ',q[num])
    try:
      tst=input('a: ')
      a[num]=tst
    except:
      a.append(tst)
  turn=turn+1




