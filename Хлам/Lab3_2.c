#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#define F0(x,x1,x2,x3) (x*x3-x2*x1)
#define F0P(x,x1,x2,x3,x4,x5) (x*x3+x1*x4+x2*x5)
#define F1(i,j,x,x1,x2,x3) (pow(-1,i+j)*F0(x,x1,x2,x3))
#define F2(x,x1,x2,x3,x4,x5,x6,x7,x8)\
(x*F0(x4,x5,x7,x8)-x3*F0(x1,x2,x7,x8)+x6*F0(x1,x2,x4,x5))

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
	double **c1 = (double **)malloc(y * sizeof(double *));
	for (int i = 0; i < y; i++) c1[i] = (double *)malloc(x * sizeof(double));
	return c1;
}

void freeMatr(double **matr, int y)
{
	for (int i = 0; i < y; i++) free(matr[i]);
	free(matr);
}

void constMatr(double **matr)
{
	matr[0][0] = 14.38;	matr[0][1] = -2.41;	matr[0][2] = 1.39;	matr[0][3] = 5.86;
	matr[1][0] = 1.84;	matr[1][1] = 25.36;	matr[1][2] = -3.31;	matr[1][3] = -2.28;
	matr[2][0] = 2.46;	matr[2][1] = -3.49;	matr[2][2] = 16.37;	matr[2][3] = 4.47;
}

void writeMatr(double **matr, int x, int y, int z)
{
	for (int i = 0; i < y; i++)
	{
		if (z == 1) printf("x%d = ",i+1);
		for (int j = 0; j < x; j++) printf("%lf\t",matr[i][j]);
		if (z == 1) printf(" ");
		else printf("\n");
	}
	if (z == 1) printf("\n");
}

void mobr(double **matr, double **matr1)
{
	double D = F2(matr[0][0],matr[0][1],matr[0][2],matr[1][0],matr[1][1],matr[1][2],matr[2][0],matr[2][1],matr[2][2]);

	matr1[0][0] = F1(1,1,matr[1][1],matr[1][2],matr[2][1],matr[2][2]) / D;
	matr1[1][0] = F1(1,2,matr[1][0],matr[1][2],matr[2][0],matr[2][2]) / D;
	matr1[2][0] = F1(1,3,matr[1][0],matr[1][1],matr[2][0],matr[2][1]) / D;

	matr1[0][1] = F1(2,1,matr[0][1],matr[0][2],matr[2][1],matr[2][2]) / D;
	matr1[1][1] = F1(2,2,matr[0][0],matr[0][2],matr[2][0],matr[2][2]) / D;
	matr1[2][1] = F1(2,3,matr[0][0],matr[0][1],matr[2][0],matr[2][1]) / D;

	matr1[0][2] = F1(3,1,matr[0][1],matr[0][2],matr[1][1],matr[1][2]) / D;
	matr1[1][2] = F1(3,2,matr[0][0],matr[0][2],matr[1][0],matr[1][2]) / D;
	matr1[2][2] = F1(3,3,matr[0][0],matr[0][1],matr[1][0],matr[1][1]) / D;
}

void mumnozh(double **matr, double **matr1, double **matr2, int z, int x, int y, int flag)
{
	if (x >= 1 && y >= 1 && z == 3 && flag == 0) matr2[0][0] = F0P(matr[0][0],matr[0][1],matr[0][2],matr1[0][0],matr1[1][0],matr1[2][0]);
	if (x >= 2 && y >= 1 && z == 3 && flag == 0) matr2[0][1] = F0P(matr[0][0],matr[0][1],matr[0][2],matr1[0][1],matr1[1][1],matr1[2][1]);
	if (x >= 3 && y >= 1 && z == 3 && flag == 0) matr2[0][2] = F0P(matr[0][0],matr[0][1],matr[0][2],matr1[0][2],matr1[1][2],matr1[2][2]);
	if (x >= 1 && y >= 2 && z == 3 && flag == 0) matr2[1][0] = F0P(matr[1][0],matr[1][1],matr[1][2],matr1[0][0],matr1[1][0],matr1[2][0]);
	if (x >= 2 && y >= 2 && z == 3 && flag == 0) matr2[1][1] = F0P(matr[1][0],matr[1][1],matr[1][2],matr1[0][1],matr1[1][1],matr1[2][1]);
	if (x >= 3 && y >= 2 && z == 3 && flag == 0) matr2[1][2] = F0P(matr[1][0],matr[1][1],matr[1][2],matr1[0][2],matr1[1][2],matr1[2][2]);
	if (x >= 1 && y >= 3 && z == 3 && flag == 0) matr2[2][0] = F0P(matr[2][0],matr[2][1],matr[2][2],matr1[0][0],matr1[1][0],matr1[2][0]);
	if (x >= 2 && y >= 3 && z == 3 && flag == 0) matr2[2][1] = F0P(matr[2][0],matr[2][1],matr[2][2],matr1[0][1],matr1[1][1],matr1[2][1]);
	if (x >= 3 && y >= 3 && z == 3 && flag == 0) matr2[2][2] = F0P(matr[2][0],matr[2][1],matr[2][2],matr1[0][2],matr1[1][2],matr1[2][2]);

	if (x >= 1 && y >= 1 && z == 3 && flag == 1) matr2[0][0] = F0P(matr[0][0],matr[0][1],matr[0][2],matr1[0][3],matr1[1][3],matr1[2][3]);
	if (x >= 1 && y >= 2 && z == 3 && flag == 1) matr2[1][0] = F0P(matr[1][0],matr[1][1],matr[1][2],matr1[0][3],matr1[1][3],matr1[2][3]);
	if (x >= 1 && y >= 3 && z == 3 && flag == 1) matr2[2][0] = F0P(matr[2][0],matr[2][1],matr[2][2],matr1[0][3],matr1[1][3],matr1[2][3]);
	
	if (x >= 1 && y >= 1 && z == 3 && flag == 2) matr2[0][3] = F0P(matr[0][0],matr[0][1],matr[0][2],matr1[0][3],matr1[1][3],matr1[2][3]);
	if (x >= 1 && y >= 2 && z == 3 && flag == 2) matr2[1][3] = F0P(matr[1][0],matr[1][1],matr[1][2],matr1[0][3],matr1[1][3],matr1[2][3]);
	if (x >= 1 && y >= 3 && z == 3 && flag == 2) matr2[2][3] = F0P(matr[2][0],matr[2][1],matr[2][2],matr1[0][3],matr1[1][3],matr1[2][3]);
}

void copyMatr(double **matr1, double **matr, int x)
{
	if (x == 1) { matr1[0][0] = matr[0][3]; matr1[1][0] = matr[1][3]; matr1[2][0] = matr[2][3]; }
	else { matr1[0][0] = matr[0][0]; matr1[1][0] = matr[1][0]; matr1[2][0] = matr[2][0]; }
	if (x == 2) { matr1[0][1] = matr[0][3]; matr1[1][1] = matr[1][3]; matr1[2][1] = matr[2][3]; }
	else { matr1[0][1] = matr[0][1]; matr1[1][1] = matr[1][1]; matr1[2][1] = matr[2][1]; }
	if (x == 3) { matr1[0][2] = matr[0][3]; matr1[1][2] = matr[1][3]; matr1[2][2] = matr[2][3]; }
	else { matr1[0][2] = matr[0][2]; matr1[1][2] = matr[1][2]; matr1[2][2] = matr[2][2]; }
	if (x >= 4) { matr1[0][3] = matr[0][3]; matr1[1][3] = matr[1][3]; matr1[2][3] = matr[2][3]; }
	if (x >= 5) { matr1[0][4] = matr[0][4]; matr1[1][4] = matr[1][4]; matr1[2][4] = matr[2][4]; }
}

void sumMatr(double **matr1, int x)
{	
	if (x == 5)
	{
		matr1[0][5] = matr1[0][0] + matr1[0][1] + matr1[0][2] + matr1[0][3] + matr1[0][4];
		matr1[1][5] = matr1[1][0] + matr1[1][1] + matr1[1][2] + matr1[1][3] + matr1[1][4];
		matr1[2][5] = matr1[2][0] + matr1[2][1] + matr1[2][2] + matr1[2][3] + matr1[2][4];
	}
}

void trancpMatr(double **matr, double **matr1)
{
	for (int i = 0; i < 3; i++)
		for (int j = 0; j < 3; j++)
			matr1[i][j] = matr[j][i];
}

// gcc -Wall -g -o "Lab3_2.exe" "Lab3_2.c" -lm -fopenmp & Lab3_2.exe > result.txt
int main(int argc, char **argv)
{
	double **matr = memoryAllocationDouble(4, 3);
	constMatr(matr); writeMatr(matr,4,3,0);
	
	printf("\nmatrichniy metod\ndelta\t%lf\n",F2(matr[0][0],matr[0][1],matr[0][2],matr[1][0],matr[1][1],matr[1][2],matr[2][0],matr[2][1],matr[2][2]));
	double **matr1 = memoryAllocationDouble(3, 3);
	mobr(matr, matr1);
	printf("\n"); writeMatr(matr1,3,3,0);
	double **matr2 = memoryAllocationDouble(1, 3);
	mumnozh(matr1,matr,matr2,3,1,3,1);
	printf("\n"); writeMatr(matr2,1,3,1);
	double **matr3 = memoryAllocationDouble(1, 3);
	mumnozh(matr,matr2,matr3,3,1,3,0);
	printf("proverka\n"); writeMatr(matr3,1,3,0);

	copyMatr(matr1, matr, 1); 
	copyMatr(matr2, matr, 2);
	copyMatr(matr3, matr, 3);
	double D0 = F2(matr[0][0],matr[0][1],matr[0][2],matr[1][0],matr[1][1],matr[1][2],matr[2][0],matr[2][1],matr[2][2]),
		D1 = F2(matr1[0][0],matr1[0][1],matr1[0][2],matr1[1][0],matr1[1][1],matr1[1][2],matr1[2][0],matr1[2][1],matr1[2][2]),
		D2 = F2(matr2[0][0],matr2[0][1],matr2[0][2],matr2[1][0],matr2[1][1],matr2[1][2],matr2[2][0],matr2[2][1],matr2[2][2]),
		D3 = F2(matr3[0][0],matr3[0][1],matr3[0][2],matr3[1][0],matr3[1][1],matr3[1][2],matr3[2][0],matr3[2][1],matr3[2][2]);
	printf("\nmetod Kramera\ndelta\t%lf\n",D0);
	printf("delta1\t%lf\tx1 = %lf\n",D1,D1/D0);
	printf("delta1\t%lf\tx2 = %lf\n",D2,D2/D0);
	printf("delta1\t%lf\tx3 = %lf\n",D3,D3/D0);

	freeMatr(matr, 3);  freeMatr(matr1, 3);
	freeMatr(matr2, 3); freeMatr(matr3, 3);

	matr = memoryAllocationDouble(6, 3);
	matr1 = memoryAllocationDouble(6, 3);
	matr2 = memoryAllocationDouble(6, 3);
	matr3 = memoryAllocationDouble(6, 3);
	double **matr4 = memoryAllocationDouble(6, 3);
	double **matr5 = memoryAllocationDouble(6, 3);
	double **matr6 = memoryAllocationDouble(1, 3);

	constMatr(matr);
	matr[0][4] = matr[0][5] = matr[0][0] + matr[0][1] + matr[0][2] + matr[0][3];
	matr[1][4] = matr[1][5] = matr[1][0] + matr[1][1] + matr[1][2] + matr[1][3];
	matr[2][4] = matr[2][5] = matr[2][0] + matr[2][1] + matr[2][2] + matr[2][3];
	printf("\ngaussa\n\t1\n");
	writeMatr(matr,6,3,0);

	copyMatr(matr1, matr, 5);
	for (int i1 = 0; i1 < 3; i1++)
		for (int i = 0; i < 5; i++)
			matr1[i1][i] /= matr[i1][0];
	sumMatr(matr1,5); printf("\t2\n");
	writeMatr(matr1,6,3,0);

	copyMatr(matr2, matr1, 5);
	for (int i1 = 1; i1 < 3; i1++)
		for (int i = 0; i < 5; i++)
			matr2[i1][i] -= matr2[0][i];
	sumMatr(matr2,5); printf("\t3\n");
	writeMatr(matr2,6,3,0);
	
	copyMatr(matr3, matr2, 5);
	for (int i1 = 1; i1 < 3; i1++)
		for (int i = 0; i < 5; i++)
			matr3[i1][i] /= matr2[i1][1];
	sumMatr(matr3,5); printf("\t4\n");
	writeMatr(matr3,6,3,0);

	copyMatr(matr4, matr3, 5);
	for (int i = 0; i < 5; i++)
		matr4[2][i] -= matr3[1][i];
	sumMatr(matr4,5); printf("\t5\n");
	writeMatr(matr4,6,3,0);

	copyMatr(matr5, matr4, 5);
	for (int i = 0; i < 5; i++)
		matr5[2][i] /= matr4[2][2];
	sumMatr(matr5,5); printf("\t5\n");
	writeMatr(matr5,6,3,0);
	
	matr6[2][0] = matr5[2][3];
	matr6[1][0] = matr5[1][3] - matr5[1][2]*matr6[2][0];
	matr6[0][0] = matr5[0][3] - matr5[0][2]*matr6[2][0] - matr5[0][1]*matr6[1][0];
	printf("\n"); writeMatr(matr6,1,3,1);

	freeMatr(matr, 3);
	freeMatr(matr1, 3); freeMatr(matr2, 3);
	freeMatr(matr3, 3); freeMatr(matr4, 3);
	freeMatr(matr5, 3); freeMatr(matr6, 3);


	matr = memoryAllocationDouble(4, 3);
	constMatr(matr); printf("\nMPI\n");
	writeMatr(matr,4,3,0);
	
	matr1 = memoryAllocationDouble(4, 3);
	copyMatr(matr1, matr, 4);
	for (int i1 = 0; i1 < 3; i1++)
		for (int i = 0; i < 5; i++)
			matr1[i1][i] /= matr[i1][i1];
	printf("\n"); writeMatr(matr1,4,3,0);

	matr6 = memoryAllocationDouble(4, 3);
	for (int i = 0; i < 3; i++)
		matr6[0][i] = (same(matr1[i][0],1) ? 0 : meABS(matr1[i][0])) + 
		(same(matr1[i][1],1) ? 0 : meABS(matr1[i][1])) + 
		(same(matr1[i][2],1) ? 0 : meABS(matr1[i][2]));
	for (int i = 0; i < 3; i++)
		matr6[1][i] = (same(matr1[0][i],1) ? 0 : meABS(matr1[0][i])) + 
		(same(matr1[1][i],1) ? 0 : meABS(matr1[1][i])) + 
		(same(matr1[2][i],1) ? 0 : meABS(matr1[2][i]));
	matr6[0][3] = matr6[0][0] > matr6[0][1] ? 
		(matr6[0][2] > matr6[0][0] ? matr6[0][2] : matr6[0][0]) : 
		(matr6[0][1] > matr6[0][0] ? matr6[0][1] : matr6[0][0]);
	matr6[1][3] = matr6[1][0] > matr6[1][1] ? 
		(matr6[1][2] > matr6[1][0] ? matr6[1][2] : matr6[1][0]) : 
		(matr6[1][1] > matr6[1][0] ? matr6[1][1] : matr6[1][0]);
	matr6[2][0] = sqrt(
		matr1[0][1] * matr1[0][1] + matr1[0][2] * matr1[0][2] +
		matr1[1][0] * matr1[1][0] + matr1[1][2] * matr1[1][2] +
		matr1[2][0] * matr1[2][0] + matr1[2][1] * matr1[2][1]);
	matr6[2][3] = matr6[0][3] < matr6[1][3] ? 
		(matr6[2][0] < matr6[0][3] ? matr6[2][0] : matr6[0][3]) : 
		(matr6[2][0] < matr6[1][3] ? matr6[2][0] : matr6[1][3]);
	matr6[2][1] = matr6[2][2] = 0;
	printf("\n"); writeMatr(matr6,4,3,0);

	matr2 = memoryAllocationDouble(10, 100);
	matr3 = memoryAllocationDouble(1, 3); int i1 = 0;
	matr2[0][0] = matr1[0][3]; matr2[0][1] = matr1[1][3]; matr2[0][2] = matr1[2][3];
	for (int i = 0; i == 0 ? 1 : matr2[i-1][9] >= 0.0001*(1-matr6[2][3])/matr6[2][3] ; i++)
	{
		for (int j = 0; j < 3; j++)
			matr2[i][3+j] = matr1[j][3] - 
			matr1[j][j==0?1:0] * matr2[i][j==0?1:0] - 
			matr1[j][j==2?1:2] * matr2[i][j==2?1:2];
		for (int j = 0; j < 3; j++)
			matr2[i][6+j] = meABS(matr2[i][j] - matr2[i][3+j]);
		matr2[i][9] = matr2[i][6] > matr2[i][7] ? 
			(matr2[i][6] > matr2[i][8] ? matr2[i][6] : matr2[i][8]) : 
			(matr2[i][7] > matr2[i][8] ? matr2[i][7] : matr2[i][8]);
		for (int j = 0; j < 3; j++)
			matr2[i+1][j] = matr2[i][3+j];
		i1 = i;
	}
	printf("\n"); writeMatr(matr2,10,i1+1,0);
	matr3[0][0] = matr2[i1][3];
	matr3[1][0] = matr2[i1][4];
	matr3[2][0] = matr2[i1][5];
	printf("\n"); writeMatr(matr3,1,3,1);

	freeMatr(matr, 3); freeMatr(matr1, 3);
	freeMatr(matr2, 100);
	freeMatr(matr3, 3); freeMatr(matr6, 3);


	matr = memoryAllocationDouble(4,3);
	constMatr(matr); printf("\nZtidekia\n");
	writeMatr(matr,4,3,0);

	matr1 = memoryAllocationDouble(3,3);
	trancpMatr(matr, matr1);
	printf("\n"); writeMatr(matr1,3,3,0);

	matr2 = memoryAllocationDouble(4,3);
	mumnozh(matr1, matr, matr2, 3, 3, 3, 0);
	mumnozh(matr1, matr, matr2, 3, 1, 3, 2);
	printf("\n"); writeMatr(matr2,4,3,0);

	matr3 = memoryAllocationDouble(4,3);
	copyMatr(matr3, matr2, 4);
	for (int i1 = 0; i1 < 3; i1++)
		for (int i = 0; i < 5; i++)
			matr3[i1][i] /= matr2[i1][i1];
	printf("\n"); writeMatr(matr3,4,3,0);

	matr4 = memoryAllocationDouble(7, 100);
	matr5 = memoryAllocationDouble(1, 3); i1 = 0;
	matr4[0][0] = matr3[0][3]; matr4[0][1] = matr3[1][3]; matr4[0][2] = matr3[2][3];
	for (int i = 0; i < 4; i++) matr4[0][i+3] = 0;
	for (int i = 1; i == 1 ? 1 : matr4[i-1][6] >= 0.0001 ; i++)
	{
		for (int j = 0; j < 3; j++)
		{
			matr4[i][3+j] = matr3[j][3] - matr3[j][0] * matr4[i - (j < 1 ? 1 : 0)][0] - 
				matr3[j][1] * matr4[i - (j < 2 ? 1 : 0)][1] - matr3[j][2] * matr4[i-1][2];
			matr4[i][j] = matr4[i-1][j]+matr4[i][3+j];
		}
		matr4[i][6] = meABS(matr4[i][3]) > meABS(matr4[i][4]) ? 
			(meABS(matr4[i][3]) > meABS(matr4[i][5]) 
			? meABS(matr4[i][3]) : meABS(matr4[i][5])) : 
			(meABS(matr4[i][4]) > meABS(matr4[i][5]) 
			? meABS(matr4[i][4]) : meABS(matr4[i][5]));
		i1 = i;
	}
	printf("\n"); writeMatr(matr4,7,i1+1,0);
	matr5[0][0] = matr4[i1][0];
	matr5[1][0] = matr4[i1][1];
	matr5[2][0] = matr4[i1][2];
	printf("\n"); writeMatr(matr5,1,3,1);
	
	freeMatr(matr, 3); freeMatr(matr1, 3);
	freeMatr(matr2, 3); freeMatr(matr3, 3);
	freeMatr(matr4, 100); freeMatr(matr5, 3);



	
}
