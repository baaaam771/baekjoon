#include <stdio.h>
#include <algorithm>
using namespace std;
 
int arr[100005];
int n, s;
int m;
 
int main(void) {
    scanf("%d %d", &n, &s);
    scanf("%d", &m);
    for (int i = 0; i < m; i++) {
        scanf("%d", &arr[i]);
    }
 
    int sum = 0;
    for (int t = 0; t < 1000000; t++) {
        for (int i = 0; i < m; i++) {
            if (t % arr[i] == 0) {
                sum++;
                if (sum >= n - s) {
                    printf("%d", i+1);
                    return 0;
                }
            }
        }
    }
}