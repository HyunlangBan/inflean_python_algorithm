## Quick Sort
- 후위순회
- pivot을 구하는 기준은 여러개가 있지만 여기서는 rt로 하기로 함
- 분할 -> 중심값(pivot)보다 작으면 왼쪽, 크면 오른쪽
  - idx 0부터 pos를 기준으로 idx를 증가시키는데, 현재 idx가 pivot보다 작으면 pos와 현재 idx를 swap하고 pos+1을 해준다.
- 탐색이 끝나면 최종 pos와 rt를 swap한다. -> 이동한 pivot(rt)를 기준으로 리스트가 나뉜다.(partiton)

![image](https://user-images.githubusercontent.com/45524783/146782444-e51ffcc2-4f31-4951-b16c-abfd9ed50774.png)

## Code
```python
def Qsort(lt, rt):
  if lt<rt:
    ## partiton
    pos=lt     ## 분할된 영역의 시작지점
    pivot=arr[rt]
    for i in range(lt, rt):
      if arr[i]<=pivot:
        arr[i], arr[pos] = arr[pos], arr[i]
        post+=1
    arr[rt], arr[pos] = arr[pos], arr[rt]
    
    Qsort(lt, pos-1)
    Qsort(pos+1, rt)
    
arr=[45, 21, 23, 36, 15, 67, 11, 60, 20, 33]
print("Before sort: ", end='')
print(arr)
Qsort(0, 9)
print("After sort: ", end='')
print(arr)
```
