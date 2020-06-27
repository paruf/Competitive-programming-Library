def factorization(n):
  """
  �����̒l��f���������������X�g��Ԃ�

  Parameters
  ----------
  n : int
      �f�����������������R��

  Returns
  -------
  retlist : list
      2�ȏ�̐���n => [[�f����, �w��], ...]��2�������X�g
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