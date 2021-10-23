#include<iostream>
using namespace std;
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int cache[10001] = { 0 };
	int n,i;
	cin >> n;
	for (i = 0; i < n; i++)
	{
		int tmp;
		cin >> tmp;
		cache[tmp]++;
	}
	long long max = -1;
	int total = n;
	for (i = 1; i <= 10000; i++)
	{
		if (cache[i] > 0)
		{
			if (max < i*total)
			{
				max = i * total;
			}
			total -= cache[i];
		}
	}
	cout << max;
}