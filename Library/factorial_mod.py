def factorial_mod(n, mod):
  """
  ���R��n!��mod�Ŋ����ė]�����l��Ԃ��B

  Parameters
  ----------
  n : int
    ���R��
  mod:int
    ���R��
  Returns
  -------
  res�Fint

  """
  res=1
  for i in range(1,n+1):
    res*=i
    res%=mod
  return res

