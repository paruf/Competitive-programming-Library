def isPrime(x):
  """
  x���f�����ۂ����肷��B

  Parameters
  ----------
  x: int
      ���R��

  Returns
  -------
      True:�f��
      False:�f���ł͂Ȃ�
  """
  if x<2:
    return False
  for i in range(2,int(x**0.5)+1):
    if x%i==0:
      return False
  return True


def sieve(x):
  """
  x�ȉ��̎��R�����f�����ۂ��𔻒肷��B

  Parameters
  ----------
  x: int
      ���R��

  Returns
  -------
  f:list
    True:�f��
    False:�f���ȊO
  """
  f=[True]*(x+1)
  f[0],f[1]=False,False

  for i in range(2,len(f)):
    if isPrime(i):
      for j in range(i*2,len(f),i):
        f[j]=False
  return f


