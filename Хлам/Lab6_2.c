#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>

double meABS(double x)
{
	if (x < 0) return -x;
	else return x;
}

int same(double one, double two)
{
	return meABS(one - two) < 0.000001;
}

double** memoryAllocationDouble(int x, int y)
{
	double** c1 = (double**)malloc(y * sizeof(double*));
	for (int i = 0; i < y; i++) c1[i] = (double*)malloc(x * sizeof(double));
	return c1;
}

void freeMatr(double** matr, int y)
{
	for (int i = 0; i < y; i++) free(matr[i]);
	free(matr);
}

double F(double x)
{
	return 5 / pow((4 * x - 3), 3);
}
double F1(double x)
{
	return -60 / pow((4 * x - 3), 4);
}
double Ln(double h1, double** matr, double i)
{
	return (1 / h1) * (-(matr[0][1] / 6) * (3 * i * i - 12 * i + 11) + (matr[1][1] / 2) * (3 * i * i - 10 * i + 6) - (matr[2][1] / 2) * (3 * i * i - 8 * i + 3) + (matr[3][1] / 6) * (3 * i * i - 6 * i + 2));
}
double Pn(double h1, double** matrE, double i)
{
	return (1 / h1) * (matrE[0][0] + ((2 * i - 1) / 2) * matrE[0][1] + ((3 * i * i - 6 * i + 2) / (2 * 3)) * matrE[0][2]);
}

double summ(double** matr, int x, int y, int maxX, int maxY)
{
	double g = 0;
	for (int i = x == -1 ? 0 : x, j = y == -1 ? 0 : y; i < maxX && j < maxY; i += (x == -1 ? 1 : 0), j += (y == -1 ? 1 : 0))
		g += matr[j][i];
	return g;
}

// gcc -Wall -g -o "Lab6_2.exe" "Lab6_2.c" -lm -fopenmp & Lab6_2.exe > result.txt
int main(int argc, char **argv)
{
	srand(time(NULL));
	double** matr = memoryAllocationDouble(2, 11);
	double** matr2 = memoryAllocationDouble(2, 5);
	double** matrE = memoryAllocationDouble(2, 10);
	double h1 = 0.1, h2 = 0.2, a = 4.23, t;
	matr[0][0] = 4;
	for (int i = 0; i < 11; i++) matr[i][1] = F(matr[i][0] = matr[0][0] + h1 * i);
	for (int i = 0; i < 5; i++) matr2[i][1] = F(matr2[i][0] = matr[i * 2 + 1][0]);
 	for (int i = 0; i < 10; i++) matrE[i][1] = F(matrE[i][0] = ((rand() % 10000) / 100000.0) + matr[i][0]);
	double Sl = (summ(matr, 1, -1, 2, 11) - matr[10][1]) * h1, 
		Sp = (summ(matr, 1, -1, 2, 11) - matr[0][1]) * h1, 
		Ss = summ(matr2, 1, -1, 2, 5) * h2, 
		Sr = summ(matrE, 1, -1, 2, 10) * h1, 
		St = h1 * (summ(matr, 1, -1, 2, 11) - (matr[0][1] + matr[10][1]) / 2), 
		Sc = (2 * h1 / 3) * (summ(matr, 1, -1, 2, 11) - (matr[0][1] + matr[10][1]) / 2 + matr[1][1] + matr[3][1] + matr[5][1] + matr[7][1] + matr[9][1]);

	printf("Metody integrirovaniya\n");
	printf("x%c%cf(x)%c%ch%c%cEi%c%cf(Ei)\n",9,9,9,9,9,9,9,9);
	for (int i = 0; i < 11; i++)
	{
		for (int j = 0; j < 2; j++)
			printf("%lf%c",matr[i][j],9);

		if (i == 0) printf("%lf%c",h1,9);
		else printf("%c%c",9,9);

		for (int j = 0; j < 2 && i != 0; j++)
			printf("%lf%c",matrE[i-1][j],9);

		printf("\n");
	}
	printf("\nSleft = %lf, Sright = %lf\nSmid = %lf, Srandom = %lf\nStr = %lf, Ssim = %lf\n\n", Sl, Sp, Ss, Sr, St, Sc);

	freeMatr(matr, 11); freeMatr(matr2, 5); freeMatr(matrE, 10);

	matr = memoryAllocationDouble(5, 4);
	matrE = memoryAllocationDouble(3, 3);
	matr[0][0] = 4;
	for (int i = 0; i < 4; i++) matr[i][1] = F(matr[i][0] = matr[0][0] + h1 * i);
	for (int i = 0; i < 4; i++) matr[i][2] = F1(matr[i][0]);
	for (int i = 0; i < 4; i++) matr[i][3] = Ln(h1, matr, i);
	matrE[0][0] = matr[1][1] - matr[0][1];
	matrE[1][0] = matr[2][1] - matr[1][1];
	matrE[2][0] = matr[3][1] - matr[2][1];
	matrE[1][1] = matrE[2][0] - matrE[1][0];
	matrE[0][1] = matrE[1][0] - matrE[0][0];
	matrE[0][2] = matrE[1][1] - matrE[0][1];
	for (int i = 0; i < 4; i++) matr[i][4] = Pn(h1, matrE, i);
	t = (a - matr[0][0]) / h1;

	printf("Metody Lagranzha i N'yutona\n");
	printf("x%c%cf(x)%c%cf`(x)%c%cLn`(x)%c%cPn`(x)\n",9,9,9,9,9,9,9,9);
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 5; j++)
			printf("%lf%c", matr[i][j], 9);
		printf("\n");
	}
	printf("\n^iy0%c%c^iy1%c%c^iy2\n",9,9,9,9);
	for (int i = 0; i < 3; i++)
	{
		for (int j = 0; j < 3 - i; j++)
			printf("%lf%c", matrE[i][j], 9);
		printf("\n");
	}

	printf("\na = %lf, f`(a) = %lf\nt = %lf\nLn`(x) = %lf, Pn`(x) = %lf\n",a,F1(a),t,Ln(h1, matr, t),Pn(h1, matrE, t));
}
