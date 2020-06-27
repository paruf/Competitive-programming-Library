from heapq import heappop,heappush
def dijkstra(s,n,edge):
  """
  始点sから各頂点への最短距離を返す
 
  Parameters
  ----------
  s : int
      視点とする頂点（0-indexed）
  n : int
      グラフの要素数
  eage:list
      グラフ
 
  Returns
  -------
  dist ：list
  始点sから各頂点への最短距離
  """
  dist=[float("inf")]*n
  dist[s]=0
  used=[-1]*n
  hq=[[dist[s],s]]
  while hq:
    d,cur=heappop(hq)
    if dist[cur]<d:continue # 距離が最小でない場合は飛ばす
    for nx,nxd in edge[cur]:
      if dist[cur]+nxd<dist[nx]:
        dist[nx]=dist[cur]+nxd
        used[nx]=cur
        heappush(hq,[dist[cur]+nxd,nx])
  return dist