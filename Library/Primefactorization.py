def factorization(n):
  """
  引数の値を素因数分解したリストを返す

  Parameters
  ----------
  n : int
      素因数分解したい自然数

  Returns
  -------
  retlist : list
      2以上の整数n => [[素因数, 指数], ...]の2次元リスト
  """
  retlist = []
  tmp = n
  for i in range(2, int(-(-n**0.5//1))+1):
    if tmp%i==0:
      cnt=0
      while tmp%i==0:
        cnt+=1
        tmp //= i
      retlist.append([i, cnt])

  if tmp!=1:
    retlist.append([tmp, 1])

  if retlist==[]:
    retlist.append([n, 1])

  return retlist