amt=int(input('Enter Target Amount: '))
coins=list(map(int, input("Enter Coins: ").rstrip().split()))
coins.sort()

if(amt>=coins[0]):
  matrix=[]
  array=[0 for i in range(amt+1)]
  array[0]=0
  for i in range(1,amt+1):
    array[i]=amt+1

  for i in range(len(coins)):
    coin=coins[i]
    for j in range(1,amt+1):
      amount=j
      if(amount<coin):
        array[amount]=min(amount,array[amount])
      else:
        array[amount]=min(array[amount],array[amount-coin]+1)
    temp=list(array)
    matrix.append(temp)

  print("\nMinimum numbers of Coins: ",array[amt])

  row=len(matrix)-1
  column=amt

  list_coins=[]
  while(row>-1 and column>-1):

    if(row==0 and column-coins[row]==0):
      list_coins.append(coins[row])
      break
    elif(column==0):

      break
    elif(matrix[row][column]==matrix[row-1][column]):
      row=row-1
    else:
      list_coins.append(coins[row])
      column=column-coins[row]

  list_coins.sort()
  print("\nCoins required ",list_coins)
else:
  print("Not Possible as Target ",amt," we have Coins ",coins)

print('\n')
for i in matrix:
    print(*i)