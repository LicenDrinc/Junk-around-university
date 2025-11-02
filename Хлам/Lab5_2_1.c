#include <stdio.h>
#include <math.h>
#include <stdlib.h>

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

void mobr(double** matr, double** matr1)
{
	int i, j, k;
	double ratio;

	double aug[8][2 * 8];
	for (i = 0; i < 8; i++) 
	{
		for (j = 0; j < 8; j++)
			aug[i][j] = matr[i][j];
		for (j = 8; j < 2 * 8; j++)
			aug[i][j] = (i == (j - 8)) ? 1 : 0;
	}

	for (i = 0; i < 8; i++) 
	{
		double diag = aug[i][i];
		for (j = 0; j < 2 * 8; j++)
			aug[i][j] /= diag;

		for (k = 0; k < 8; k++) 
		{
			if (k != i)
			{
				ratio = aug[k][i];
				for (j = 0; j < 2 * 8; j++)
					aug[k][j] -= ratio * aug[i][j];
			}
		}
	}

	for (i = 0; i < 8; i++)
		for (j = 0; j < 8; j++)
			matr1[i][j] = aug[i][j + 8];
}

void copyMatr(double** A, double** B, double** C)
{
	for (int j = 0; j < 8; j++)
	{
		C[j][0] = 0;
		for (int k = 0; k < 8; k++)
			C[j][0] += A[k][8] * B[j][k];
	}
}

// gcc -Wall -g -o "Lab5_2_1.exe" "Lab5_2_1.c" -lm -fopenmp & Lab5_2_1.exe > result.txt
int main(int argc, char **argv)
{
	double** matr = memoryAllocationDouble(4, 2);
	matr[0][0] = 4;		matr[0][1] = 6;		matr[0][2] = 7;		matr[0][3] = 9;
	matr[1][0] = 1.04;	matr[1][1] = 1.34;	matr[1][2] = 1.46;	matr[1][3] = 2.3;

	double x = 5.23;
	double l0, l1, l2, l3, f;
	l0 = matr[1][0] * (((x - matr[0][1]) * (x - matr[0][2]) * (x - matr[0][3])) / ((matr[0][0] - matr[0][1]) * (matr[0][0] - matr[0][2]) * (matr[0][0] - matr[0][3])));
	l1 = matr[1][1] * (((x - matr[0][0]) * (x - matr[0][2]) * (x - matr[0][3])) / ((matr[0][1] - matr[0][0]) * (matr[0][1] - matr[0][2]) * (matr[0][1] - matr[0][3])));
	l2 = matr[1][2] * (((x - matr[0][0]) * (x - matr[0][1]) * (x - matr[0][3])) / ((matr[0][2] - matr[0][0]) * (matr[0][2] - matr[0][1]) * (matr[0][2] - matr[0][3])));
	l3 = matr[1][3] * (((x - matr[0][0]) * (x - matr[0][1]) * (x - matr[0][2])) / ((matr[0][3] - matr[0][0]) * (matr[0][3] - matr[0][1]) * (matr[0][3] - matr[0][2])));
	f = l0 + l1 + l2 + l3;

	double** matr1 = memoryAllocationDouble(4, 2);
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 2; j++)
			matr1[j][i] = matr[j][i];

	double t, h, a0, a1, a2, a3, f_2;
	h = (matr1[0][3] - matr1[0][0]) / 3;
	matr1[0][1] = matr1[0][0] + h;
	matr1[0][2] = matr1[0][1] + h;
	t = (x - matr1[0][0]) / h;
	a0 = matr1[1][0] / (-6) + matr1[1][1] / 2 + matr1[1][2] / (-2) + matr1[1][3] / 6;
	a1 = matr1[1][0] + matr1[1][1] * 5 / (-2) + matr1[1][2] * 2 + matr1[1][3] / (-2);
	a2 = matr1[1][0] * 11 / (-6) + matr1[1][1] * 3 + matr1[1][2] * 3 / (-2) + matr1[1][3] / 3;
	a3 = matr1[1][0];
	f_2 = a0 * powf(t, 3) + a1 * powf(t, 2) + a2 * t + a3;

	printf("metod lagranzha\n");
	for (int i = 0; i < 2; i++)
	{
		printf("%c ",i == 0 ? 'x' : 'y');
		for (int j = 0; j < 4; j++)
			printf("%lf%c",matr[i][j],9);
		printf("\n");
	}
	printf("x = %lf\nl0 = %lf l1 = %lf l2 = %lf l3 = %lf\nf(x) = %lf\n\n", x, l0, l1, l2, l3, f);
	for (int i = 0; i < 2; i++)
	{
		printf("%c ", i == 0 ? 'x' : 'y');
		for (int j = 0; j < 4; j++)
			printf("%lf%c", matr1[i][j], 9);
		printf("\n");
	}
	printf("x = %lf\nt = %lf h = %lf\nf(x) = %lf * t^3 + %lf * t^2 + %lf * t + %lf = %lf\n\n\n", x, t, h, a0, a1, a2, a3, f_2);



	freeMatr(matr1, 2);
	matr1 = memoryAllocationDouble(4, 5);
	for (int i = 0; i < 2; i++)
		for (int j = 0; j < 4; j++)
			matr1[j][i] = matr[i][j];

	matr1[1][2] = (matr1[1][1] - matr1[0][1]) / (matr1[1][0] - matr1[0][0]);
	matr1[2][2] = (matr1[2][1] - matr1[0][1]) / (matr1[2][0] - matr1[0][0]);
	matr1[3][2] = (matr1[3][1] - matr1[0][1]) / (matr1[3][0] - matr1[0][0]);

	matr1[2][3] = (matr1[2][2] - matr1[1][2]) / (matr1[2][0] - matr1[1][0]);
	matr1[3][3] = (matr1[3][2] - matr1[1][2]) / (matr1[3][0] - matr1[1][0]);
	matr1[3][4] = (matr1[3][3] - matr1[2][3]) / (matr1[3][0] - matr1[2][0]);

	a0 = matr1[0][1]; a1 = matr1[1][2]; a2 = matr1[2][3]; a3 = matr1[3][4];

	f = a0 + a1 * (x - matr1[0][0]) + a2 * (x - matr1[1][0]) * (x - matr1[0][0]) + a3 * (x - matr1[2][0]) * (x - matr1[1][0]) * (x - matr1[0][0]);

	double** matr2 = memoryAllocationDouble(4, 5);
	for (int i = 0; i < 2; i++)
		for (int j = 0; j < 4; j++)
			matr2[j][i] = matr1[3 - j][i];

	matr2[1][2] = (matr2[1][1] - matr2[0][1]) / (matr2[1][0] - matr2[0][0]);
	matr2[2][2] = (matr2[2][1] - matr2[0][1]) / (matr2[2][0] - matr2[0][0]);
	matr2[3][2] = (matr2[3][1] - matr2[0][1]) / (matr2[3][0] - matr2[0][0]);

	matr2[2][3] = (matr2[2][2] - matr2[1][2]) / (matr2[2][0] - matr2[1][0]);
	matr2[3][3] = (matr2[3][2] - matr2[1][2]) / (matr2[3][0] - matr2[1][0]);
	matr2[3][4] = (matr2[3][3] - matr2[2][3]) / (matr2[3][0] - matr2[2][0]);

	l0 = matr2[0][1]; l1 = matr2[1][2]; l2 = matr2[2][3]; l3 = matr2[3][4];

	f_2 = l0 + l1 * (x - matr2[0][0]) + l2 * (x - matr2[1][0]) * (x - matr2[0][0]) + l3 * (x - matr2[2][0]) * (x - matr2[1][0]) * (x - matr2[0][0]);

	printf("\n\nmetod n'yutona\n");
	printf("  | x    %cy        %c1        %c2        %c3    %c\n",9,9,9,9,9);
	for (int i = 0; i < 4; i++)
	{
		printf("%d | ", i);
		for (int j = 0; j < 2 + (i > 0 ? i : 0); j++)
			printf("%lf%c", matr1[i][j], 9);
		printf("\n");
	}
	printf("x = %lf\na0 = %lf a1 = %lf a2 = %lf a3 = %lf\nf(x) = %lf\n\n", x, a0, a1, a2, a3, f);
	printf("  | x    %cy        %c1        %c2        %c3    %c\n", 9, 9, 9, 9, 9);
	for (int i = 0; i < 4; i++)
	{
		printf("%d | ", i);
		for (int j = 0; j < 2 + (i > 0 ? i : 0); j++)
			printf("%lf%c", matr2[i][j], 9);
		printf("\n");
	}
	printf("x = %lf\na0 = %lf a1 = %lf a2 = %lf a3 = %lf\nf(x) = %lf\n\n\n", x, l0, l1, l2, l3, f_2);



	freeMatr(matr1, 5); freeMatr(matr2, 5);
	matr1 = memoryAllocationDouble(4, 2);
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 2; j++)
			matr1[j][i] = matr[j][i];

	matr2 = memoryAllocationDouble(4, 3);
	double** matr3 = memoryAllocationDouble(9, 8);
	double** matr4 = memoryAllocationDouble(9, 8);
	double** matrH = memoryAllocationDouble(1, 3);
	double** matr5 = memoryAllocationDouble(1, 8);

	matr2[0][0] = matr1[1][0]; matr2[1][0] = matr1[1][1]; matr2[2][0] = matr1[1][2]; matr2[0][2] = 0;

	for (int i = 0; i < 8; i++)
		for (int j = 0; j < 8; j++)
			matr3[i][j] = 0;

	matrH[0][0] = matr1[0][1] - matr1[0][0]; matrH[1][0] = matr1[0][2] - matr1[0][1]; matrH[2][0] = matr1[0][3] - matr1[0][2];

	matr3[0][0] = matrH[0][0];		matr3[0][1] = powf(matrH[0][0], 3);
	matr3[1][0] = 1;				matr3[1][1] = 3 * powf(matrH[0][0], 2); matr3[1][2] = -1;
	matr3[2][1] = 3 * matrH[0][0];	matr3[2][3] = -1;
	matr3[3][2] = matrH[1][0];		matr3[3][3] = powf(matrH[1][0], 2);		matr3[3][4] = powf(matrH[1][0], 3);
	matr3[4][2] = 1;				matr3[4][3] = 2 * matrH[1][0];			matr3[4][4] = 3 * powf(matrH[1][0], 2);		matr3[4][5] = -1;
	matr3[5][3] = 1;				matr3[5][4] = 3 * matrH[1][0];			matr3[5][6] = -1;
	matr3[6][5] = matrH[2][0];		matr3[6][6] = powf(matrH[2][0], 2);		matr3[6][7] = powf(matrH[2][0], 3);
	matr3[7][6] = 1;				matr3[7][7] = 3 * matrH[2][0];

	matr3[0][8] = matr1[1][1] - matr1[1][0]; matr3[1][8] = 0; matr3[2][8] = 0;
	matr3[3][8] = matr1[1][2] - matr1[1][1]; matr3[4][8] = 0; matr3[5][8] = 0;
	matr3[6][8] = matr1[1][3] - matr1[1][2]; matr3[7][8] = 0; 

	mobr(matr3, matr4);
	copyMatr(matr3, matr4, matr5);
	matr2[0][1] = matr5[0][0]; matr2[1][1] = matr5[2][0]; matr2[2][1] = matr5[5][0];
	matr2[1][2] = matr5[3][0]; matr2[2][2] = matr5[6][0];
	matr2[0][3] = matr5[1][0]; matr2[1][3] = matr5[4][0]; matr2[2][3] = matr5[7][0];

	f = matr2[0][0] + matr2[0][1] * (x - matr1[0][0]) + matr2[0][2] * powf((x - matr1[0][0]), 2) + matr2[0][3] * powf((x - matr1[0][0]), 3);
	printf("\n\nmetod splaynov\n");
	printf("  | a    %cb        %cc        %cd\n", 9, 9, 9);
	for (int i = 0; i < 3; i++)
	{
		printf("%d | ", i+1);
		for (int j = 0; j < 4; j++)
			printf("%lf%c", matr2[i][j], 9);
		printf("\n");
	}
	printf("\nh | ");
	for (int i = 0; i < 3; i++)
		printf("%lf%c", matrH[i][0], 9);
	printf("\n\nb1        %cd1        %cb2        %cc2        %cd2        %cb3        %cc3        %cd3        %c=\n", 9, 9, 9, 9, 9, 9, 9, 9);
	for (int i = 0; i < 8; i++)
	{
		for (int j = 0; j < 9; j++)
			printf("%lf%c", matr3[i][j], 9);
		printf("\n");
	}
	printf("\n");
	for (int i = 0; i < 8; i++)
	{
		for (int j = 0; j < 8; j++)
			printf("%lf%c", matr4[i][j], 9);
		printf("\n");
	}
	printf("\nf(x) = %lf\n", f);
	
	freeMatr(matr1, 2); freeMatr(matr, 2);
	freeMatr(matr2, 3); freeMatr(matrH, 3);
	freeMatr(matr3, 8);	freeMatr(matr4, 8);
	freeMatr(matr5, 8);
}
