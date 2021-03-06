위상정렬은 어떤 일을 하는 순서를 찾는 알고리즘입니다.    
각각의 일의 선후관계가 복잡하게 얽혀있을 때 각각 일의 선후관계를 유지하면서 전체 일의 순서를 짜는 알고리즘입니다.    
만약 아래와 같은 일의 순서를 각각 지키면서 전체 일의 순서를 정한다면      

1 4 //1번일을 하고 난 후 4번일을 해야한다.     
5 4    
4 3    
2 5   
2 3   
6 2     

![image](https://user-images.githubusercontent.com/45524783/150991905-4d3031ab-1934-42ce-8707-b0ab4314a37e.png)

전체 일의 순서는 1, 6, 2, 5, 4, 3과 같이 정할 수 있다. 전체 일의 순서는 여러 가지가 있습 니다 그 중에 하나입니다.

▣ 입력설명       
첫 번째 줄에 전체 일의 개수 N과 일의 순서 정보의 개수 M이 주어집니다. 두 번째 줄부터 M개의 정보가 주어집니다.


▣ 출력설명      
전체 일의 순서를 출력합니다.


▣ 입력예제 1    
6 6     
1 4     
5 4      
4 3      
2 5     
2 3      
6 2    
 
 
▣ 출력예제 1     
1 6 2 5 4 3

## 풀이참고
![image](https://user-images.githubusercontent.com/45524783/150992715-5e285d62-54b8-49ba-9f8f-27752302d959.png)

- 진입차수로 연결된 노드들이 먼저 끝나야 현재 노드가 수행될 수 있다.
- 입력한 일의 순서에 따라 진입 차수를 더한다.
- degree가 0인(먼저 해야할 일이 없는)곳부터 큐에 쌓는다. 
- 큐에서 하나씩 수행하며 수행한 후에는 degree에서 연결된 진입차수를 빼준다.
