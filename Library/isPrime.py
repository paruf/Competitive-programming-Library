def isPrime(x):
  """
  x‚ª‘f”‚©”Û‚©”»’è‚·‚éB

  Parameters
  ----------
  x: int
      ©‘R”

  Returns
  -------
      True:‘f”
      False:‘f”‚Å‚Í‚È‚¢
  """
  if x<2:
    return False
  for i in range(2,int(x**0.5)+1):
    if x%i==0:
      return False
  return True


def sieve(x):
  """
  xˆÈ‰º‚Ì©‘R”‚ª‘f”‚ª”Û‚©‚ğ”»’è‚·‚éB

  Parameters
  ----------
  x: int
      ©‘R”

  Returns
  -------
  f:list
    True:‘f”
    False:‘f”ˆÈŠO
  """
  f=[True]*(x+1)
  f[0],f[1]=False,False

  for i in range(2,len(f)):
    if isPrime(i):
      for j in range(i*2,len(f),i):
        f[j]=False
  return f


