def create_divisors(n):
  """
  自然数nの全ての約数を列挙したリストを作成する。

  Parameters
  ----------
  n : int
    自然数

  Returns
  -------
    divisors：list

  """
  divisors=[]
  for i in range(1,int(n**0.5)+1):
    if n%i==0:
      divisors.append(i)
      if i!=n//i:
        divisors.append(n//i)
  divisors.sort()
  return divisors


