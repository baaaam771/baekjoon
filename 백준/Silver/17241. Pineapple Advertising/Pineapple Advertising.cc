#include <iostream>
#include <vector>
using namespace std;
vector<int> house[200001];
int visit[200001] = {0};
int delivery(int start){
	int cnt = 0;
	if(visit[start] == -2)	return 0;  //이미 좋아함
	if(visit[start] == 0){
		cnt++;
		visit[start] = -2; 
	}
	for(int i=0; i<house[start].size();i++){
		int a = house[start][i];
		if(visit[a]==0){
			cnt++;
			visit[a] = -1; // 피자 전달된 집이랑 연결된 집
		}
	}
	return cnt;
}
int main(){
	int n,m,q;
	scanf("%d %d %d", &n, &m, &q);
	for(int i=0; i<m; i++){
		int a, b;
		scanf("%d %d", &a, &b);
		house[a].push_back(b);
		house[b].push_back(a);
	}
	for(int i=0; i<q; i++){
		int temp;
		scanf("%d" ,&temp);
		printf("%d\n", delivery(temp));
	}
	return 0;
}