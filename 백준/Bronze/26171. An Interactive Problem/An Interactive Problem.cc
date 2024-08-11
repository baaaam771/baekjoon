#include <iostream>
#include <string>
using namespace std;

int N;
string ret = "0";
int val;

int ans;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	while (1) {
		cout << '?' << ' ' << 1 << ' ' << N + 1 << endl;
		cin >> ret;
		if (ret.length() < 16) {
			ans = max(ans, stoi(ret));
			N++;
		}
		else break;
	}

	for (int r = 2; r <= N; r++) {
		for (int c = 1; c <= N; c++) {
			cout << '?' << ' ' << r << ' ' << c << endl;
			cin >> val;
			ans = max(ans, val);
		}
	}

	cout << '!' << ' ' << ans << endl;
}