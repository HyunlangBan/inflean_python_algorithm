## 깊이 우선 탐색

![image](https://user-images.githubusercontent.com/45524783/139700071-7d4c2847-f698-4b31-a8d9-d94db236dbf3.png)


### 전위순회
- 자기 자신을 호출 하고 왼쪽으로 탐색을 마치면 오른쪽 탐색
```python
def DFS(v):
  if v>7:
    return
    
  else:
    print(v)
    DFS(v*2)      ## 왼쪽으로 이동
    DFS(v*2+1)    ## 오른쪽으로 이동
```
- 부모 - 왼쪽 - 오른쪽 순 탐색
### 중위순회
```python
def DFS(v):
  if v>7:
    return
    
  else:
    DFS(v*2)      ## 왼쪽으로 이동
    print(v)
    DFS(v*2+1)    ## 오른쪽으로 이동
```
- 왼쪽 - 부모 - 오른쪽 순 탐색
### 후위순회
```python
def DFS(v):
  if v>7:
    return
    
  else:
    DFS(v*2)      ## 왼쪽으로 이동
    DFS(v*2+1)    ## 오른쪽으로 이동
    print(v)
```
- 왼쪽 - 오른쪽 - 부모 순 탐색
- 병합정렬에 사용


