#include <stdio.h>

int main()
{
	int N = 0, X = 0, i = 0, tmp = 0;
	scanf("%d %d", &N, &X);
	for (i = 0; i < N; i++)
	{
		scanf("%d", &tmp);
		if (tmp < X)
			printf("%d ", tmp);
	}
	return 0;
}