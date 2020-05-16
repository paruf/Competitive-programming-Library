def create_divisors(n):
  """
  ���R��n�̑S�Ă̖񐔂�񋓂������X�g���쐬����B

  Parameters
  ----------
  n : int
    ���R��

  Returns
  -------
    divisors�Flist

  """
  divisors=[]
  for i in range(1,int(n**0.5)+1):
    if n%i==0:
      divisors.append(i)
      if i!=n//i:
        divisors.append(n//i)
  divisors.sort()
  return divisors


