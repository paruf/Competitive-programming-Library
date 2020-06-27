def factorial_mod(n, mod):
  """
  自然数n!のmodで割って余った値を返す。

  Parameters
  ----------
  n : int
    自然数
  mod:int
    自然数
  Returns
  -------
  res：int

  """
  res=1
  for i in range(1,n+1):
    res*=i
    res%=mod
  return res

