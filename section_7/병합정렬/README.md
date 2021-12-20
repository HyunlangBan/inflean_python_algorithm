## Divide Sort 
- lt와 rt의 영역을 절반으로 나눈다(`(lt+rt)//2`) -> (lt, mid), (mid+1, rt)
- 나눈 두 영역(각각 정렬되어 있음)을 새로운 리스트에 오름차순으로 합친다.(tmp)
- 위에서 정렬한 부분을 원래의 리스트에 적용해준다.    


![image](https://user-images.githubusercontent.com/45524783/146779286-53bc7ae3-62f8-40e5-8e7c-64d047dbc76e.png)

## Code
```python
def Dsort(lt, rt):
  if lt<rt:
    mid = (lt+rt)//2
    Dsort(lt, mid)
    Dsort(mid+1, rt)
    
    ## 왼쪽, 오른쪽 부분끼리 정렬되고 난 후 -> 병합
    p1=lt
    p2=mid+1
    tmp=[]
    while p1<=mid and p2<=rt:
      if arr[p1]<arr[p2]:
        tmp.append(arr[p1])
        p1+=1
      else:
        tmp.append(arr[p2])
        p2+=1
    if p1<=mid:
      tmp=tmp+arr[p1:mid+1]
    if p2<=rt:
      tmp=tmp+arr[p2:rt+1]
      
    for i in range(len(tmp)):
      arr[lt+i] = tmp[i]
      
arr=[23, 11, 45, 36, 15, 67, 33, 21]
print("Before Sort: ", end=' ')
print(arr)
Dsort(0, 7)
print()
print("After Sort: ", end=' ')
print(arr)
```
