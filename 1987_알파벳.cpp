#include<iostream>
#include<algorithm>
#include<vector>
#include<limits>
#include<queue>
#include<memory.h>
#include<stack>
#include<string>
#include<deque>
#include<math.h>
#define MAX 10000

using namespace std;

int n, m;


int answer = 0;
int dx[] = { -1,1,0,0 };
int dy[] = { 0,0,1,-1 };
bool check[26];
char map[21][21];
int alpha[26];







void BFS(int a, int b, int cnt)
{
	answer = max(cnt, answer);

	for (int i = 0; i < 4; i++)
	{
		int nx = a + dx[i];
		int ny = b + dy[i];

		if (nx < 0 || nx >= n || ny < 0 || ny >= m)
			continue;
		int temp = (int)map[nx][ny] - 65;
		if (alpha[temp])
			continue;
		alpha[temp] = 1;
		BFS(nx, ny, cnt + 1);
		alpha[temp] = 0;
	}



}


int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	cin >> n >> m;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			cin >> map[i][j];
		}
	}
	int num = (int)map[0][0] - 65;
	alpha[num] = 1;

	BFS(0, 0, 1);

	cout << answer;

	return 0;
}