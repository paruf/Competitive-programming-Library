from heapq import heappop,heappush
def dijkstra(s,n,edge):
  """
  �n�_s����e���_�ւ̍ŒZ������Ԃ�
 
  Parameters
  ----------
  s : int
      ���_�Ƃ��钸�_�i0-indexed�j
  n : int
      �O���t�̗v�f��
  eage:list
      �O���O
 
  Returns
  -------
  dist �Flist
  �n�_s����e���_�ւ̍ŒZ����
  """
  dist=[float("inf")]*n
  dist[s]=0
  used=[-1]*n
  hq=[[dist[s],s]]
  while hq:
    d,cur=heappop(hq)
    if dist[cur]<d:continue # �������ŏ��łȂ��ꍇ�͔�΂�
    for nx,nxd in edge[cur]:
      if dist[cur]+nxd<dist[nx]:
        dist[nx]=dist[cur]+nxd
        used[nx]=cur
        heappush(hq,[dist[cur]+nxd,nx])
  return dist