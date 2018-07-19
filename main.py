q=['hi']
a=['hello']
num=()
say='hi'
turn=2
print('hi')
a.append(input('a: '))
while True:
  if turn % 2 == 0:
    response=input('q: ')
    if response in q:
      print(a[q.index(response)])
    else:
      q.append(response)
      print('?')
  else:
    num=random.randint(0, len(q)-1)
    print(q[num])
    try:
      tst=input('a: ')
      a[num]=tst
    except:
      a.append(tst)
  turn=turn+1




