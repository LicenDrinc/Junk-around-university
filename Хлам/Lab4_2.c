#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>

double meABS(double x)
{
	if (x < 0) return -x;
	else return x;
}

int same(double one, double two) { return meABS(one - two) < 0.000001; }
int same1(double one, double two) { return meABS(one - two) < 0.05; }
int same2(double one) { return one < 1 && one > -1; }

double rand1() { return (rand() % 2000) / 1000.0 - 1; }

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

double FX(double y) { return 0.7 - cos(y - 1); }
double FY(double x) { return (2 - sin(x)) / 2; }
double F1(double x, double y) { return sin(x) + 2 * y; }
double F2(double x, double y) { return cos(y - 1) + x; }
double F1r(double x, double y) { return F1(x, y) - 2; }
double F2r(double x, double y) { return F2(x, y) - 0.7; }
double F1d1(double x) { return cos(x); }
double F1d2(double y) { return 2; }
double F2d1(double x) { return 1; }
double F2d2(double y) { return -sin(y - 1); }
double F1d(double x, double y) { return F1d1(x) + F1d2(y); }
double F2d(double x, double y) { return F2d1(x) + F2d2(y); }

void mobr(double** matr, double** matr1)
{
	int i, j, k;
	double ratio;

	double aug[2][2 * 2];
	for (i = 0; i < 2; i++)
	{
		for (j = 0; j < 2; j++) aug[i][j] = matr[i][j];
		for (j = 2; j < 2 * 2; j++) aug[i][j] = (i == (j - 2)) ? 1 : 0;
	}

	for (i = 0; i < 2; i++)
	{
		double diag = aug[i][i];
		for (j = 0; j < 2 * 2; j++) aug[i][j] /= diag;

		for (k = 0; k < 2; k++)
		{
			if (k != i)
			{
				ratio = aug[k][i];
				for (j = 0; j < 2 * 2; j++) aug[k][j] -= ratio * aug[i][j];
			}
		}
	}

	for (i = 0; i < 2; i++)
		for (j = 0; j < 2; j++)
			matr1[i][j] = aug[i][j + 2];
}

void copyMatr(double** A, double** B, double** C)
{
	for (int j = 0; j < 2; j++)
	{
		C[j][0] = 0;
		for (int k = 0; k < 2; k++)
			C[j][0] += A[j][k] * B[k][0];
	}
}

// gcc -Wall -g -o "Lab4_2.exe" "Lab4_2.c" -lm -fopenmp & Lab4_2.exe > result.txt
int main(int argc, char **argv)
{
	srand(time(NULL));
	double** matrX = memoryAllocationDouble(3, 11);
	double** matrY = memoryAllocationDouble(3, 6);
	double startX = -0.6, startY = 0.8, h = 0.1, x, y, x0, y0, x1, y1, a = -0.352, b = -0.405, f1, f2, j;
	matrX[0][0] = startX; matrY[0][1] = startY;
	for (int i = 0; i < 11; i++) matrX[i][2] = FX(matrX[i][1] = FY(matrX[i][0] = matrX[0][0] + i * h));
	for (int i = 0; i < 6; i++) matrY[i][2] = FY(matrY[i][0] = FX(matrY[i][1] = matrY[0][1] + i * h));

	for (int i = 0; i < 11; i++) { if (same1(matrX[i][0], matrX[i][2])) { x = matrX[i][0]; x1 = matrX[i][2]; y1 = matrX[i][1]; break; } }
	for (int i = 0; i < 6; i++) { if (same1(matrY[i][1], matrY[i][2])) { y = matrY[i][1]; break; } }

	while (!(same2(F2d1(x1) * b + 1) && same2(F2d2(y1) * b))) { printf("b %lf %lf %lf\n", F2d1(x1) * b + 1, F2d2(y1) * b, b); b = rand1(); }
	while (!(same2(F1d1(x1) * a) && same2(F1d2(y1) * a + 1))) { printf("a %lf %lf %lf\n", F1d1(x1) * a, F1d2(y1) * a + 1, a); a = rand1(); }

	printf("Metod prostoy iteratsii\n");
	printf("x1%c%cy%c%cx2%c%c%cx%c%cy1%c%cy2\n",9,9,9,9,9,9,9,9,9,9,9);
	for (int i = 0; i < 11; i++)
	{
		printf("%lf%c%lf%c%lf",matrX[i][0],9,matrX[i][1],9,matrX[i][2]);
		if (i < 6) printf("%c%c%lf%c%lf%c%lf",9,9,matrY[i][0],9,matrY[i][1],9,matrY[i][2]);
		printf("\n");
	}
	printf("df1/dx%c%cdf1/dy%c%cdf2/dx%c%cdf2/dy%c%ca%c%cb\n",9,9,9,9,9,9,9,9,9,9);
	printf("%lf%c%lf%c%lf%c%lf%c%lf%c%lf\n", F1d1(x1) * a, 9, F1d2(y1) * a + 1, 9, F2d1(x1) * b + 1, 9, F2d2(y1) * b, 9, a, 9, b);
	printf("i%c%cx%c%cy%c%cf1%c%cf2\n",9,9,9,9,9,9,9,9); j = 0;
	x0 = x; y0 = y;
	while (!(meABS(F1r(x, y))<0.0001 && meABS(F2r(x, y))<0.0001))
	{
		f1 = F1r(x, y); f2 = F2r(x, y);
		printf("%lf%c%lf%c%lf%c%lf%c%lf\n",j,9,x,9,y,9,f1,9,f2);
		x = x + b * f2; y = y + a * f1; j++;
	}
	printf("%lf%c%lf%c%lf%c%lf%c%lf%cOK\n\n\n",j,9,x,9,y,9,f1,9,f2,9);
	freeMatr(matrX, 11); freeMatr(matrY, 6);



	double** u = memoryAllocationDouble(1, 2); u[0][0] = x0; u[1][0] = y0;
	double** f = memoryAllocationDouble(1, 2); f[0][0] = F1r(u[0][0], u[1][0]); f[1][0] = F2r(u[0][0], u[1][0]);
	double** w = memoryAllocationDouble(2, 2); w[0][0] = F1d1(u[0][0]); w[0][1] = F1d2(u[1][0]); w[1][0] = F2d1(u[0][0]); w[1][1] = F2d2(u[1][0]);
	double** w1 = memoryAllocationDouble(2, 2); mobr(w, w1);
	double** du = memoryAllocationDouble(1, 2); copyMatr(w1, f, du);

	printf("Metod N'yutona\n");
	printf("u%c%cf%c%cw%c%c%c%cw-1%c%c%c%cdu\n", 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9);
	for (int i = 0; i < 6; i++)
	{
		printf("%lf%c%lf%c%lf%c%lf%c%lf%c%lf%c%lf%c%d\n", u[0][0], 9, f[0][0], 9, w[0][0], 9, w[0][1], 9, w1[0][0], 9, w1[0][1], 9, du[0][0], 9, meABS(du[0][0]) < 0.0001);
		printf("%lf%c%lf%c%lf%c%lf%c%lf%c%lf%c%lf%c%d\n\n", u[1][0], 9, f[1][0], 9, w[1][0], 9, w[1][1], 9, w1[1][0], 9, w1[1][1], 9, du[1][0], 9, meABS(du[1][0]) < 0.0001);
		u[0][0] = u[0][0] - du[0][0]; u[1][0] = u[1][0] - du[1][0];
		f[0][0] = F1r(u[0][0], u[1][0]); f[1][0] = F2r(u[0][0], u[1][0]);
		w[0][0] = F1d1(u[0][0]); w[0][1] = F1d2(u[1][0]); w[1][0] = F2d1(u[0][0]); w[1][1] = F2d2(u[1][0]);
		mobr(w, w1); copyMatr(w1, f, du);
	}
	printf("proverrf %lf %lf",F1(u[0][0],u[1][0]),F2(u[0][0],u[1][0]));
	freeMatr(u, 2); freeMatr(f, 2); freeMatr(w, 2); freeMatr(w1, 2); freeMatr(du, 2);
}
