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

	double aug[3][2 * 3];
	for (i = 0; i < 3; i++) 
	{
		for (j = 0; j < 3; j++)
			aug[i][j] = matr[i][j];
		for (j = 3; j < 2 * 3; j++)
			aug[i][j] = (i == (j - 3)) ? 1 : 0;
	}

	for (i = 0; i < 3; i++) 
	{
		double diag = aug[i][i];
		for (j = 0; j < 2 * 3; j++)
			aug[i][j] /= diag;

		for (k = 0; k < 3; k++) 
		{
			if (k != i)
			{
				ratio = aug[k][i];
				for (j = 0; j < 2 * 3; j++)
					aug[k][j] -= ratio * aug[i][j];
			}
		}
	}

	for (i = 0; i < 3; i++)
		for (j = 0; j < 3; j++)
			matr1[i][j] = aug[i][j + 3];
}

void copyMatr(double** A, double** B, double** C)
{
	for (int j = 0; j < 3; j++)
	{
		C[j][0] = 0;
		for (int k = 0; k < 3; k++)
			C[j][0] += A[k][3] * B[j][k];
	}
}

double af(double** matr)
{
	return (matr[0][2]-matr[0][1]*matr[0][3])/(matr[0][0]-matr[0][1]*matr[0][1]);
}
double bf(double** matr, double a)
{
	return matr[0][3]-matr[0][1] * a;
}

void M4(double** matr, double** matrM, double n)
{
	double x2=0, x=0, xy=0, y=0;
	for (int i = 0; i < 4; i++)
	{
		x2 += matr[0][i] * matr[0][i];
		x += matr[0][i]; y += matr[1][i];
		xy += matr[0][i] * matr[1][i];
	}
	matrM[0][0] = x2/n; matrM[0][1] = x/n;
	matrM[0][2] = xy/n; matrM[0][3] = y/n;
}

void M7(double** matr, double** matrM, double n)
{
	double x2=0, x=0, xy=0, y=0, x4=0, x3=0, x2y=0;
	for (int i = 0; i < 4; i++)
	{
		x4 += powf(matr[0][i], 4); x3 += powf(matr[0][i], 3);
		x2 += powf(matr[0][i], 2);
		x2y += powf(matr[0][i], 2) * matr[1][i];
		x += matr[0][i]; y += matr[1][i];
		xy += matr[0][i] * matr[1][i];
	}
	matrM[0][0] = x4/n; matrM[0][1] = x3/n;
	matrM[0][2] = x2/n; matrM[0][3] = x/n;
	matrM[0][4] = x2y/n; matrM[0][5] = xy/n;
	matrM[0][6] = y/n;
}


// gcc -Wall -g -o "Lab5_2_2.exe" "Lab5_2_2.c" -lm -fopenmp & Lab5_2_2.exe > result.txt
int main(int argc, char **argv)
{
	double** matr = memoryAllocationDouble(4, 2); double x = 5.23; double n = 4;
	matr[0][0] = 4;		matr[0][1] = 6;		matr[0][2] = 7;		matr[0][3] = 9;
	matr[1][0] = 1.04;	matr[1][1] = 1.34;	matr[1][2] = 1.46;	matr[1][3] = 2.3;
	double** matrM = memoryAllocationDouble(4, 1); M4(matr, matrM, n);
	double** matrab = memoryAllocationDouble(1, 2); double summKvRazn = 0;
	matrab[0][0] = af(matrM); matrab[1][0] = bf(matrM, matrab[0][0]);
	double** matrf = memoryAllocationDouble(4, 1); double f, pog;

	for (int i = 0; i < 4; i++) matrf[0][i] = matrab[0][0] * matr[0][i] + matrab[1][0];
	f = matrab[0][0] * x + matrab[1][0];
	for (int i = 0; i < 4; i++) summKvRazn += powf((matr[1][i]-matrf[0][i]),2);
	pog = sqrtf(summKvRazn);

	printf("Lineynaya");
	for (int i = 0; i < 2; i++)
	{
		printf("\n%c | ",i==0?'x':'y');
		for (int j = 0; j < 4; j++) printf("%lf%c",matr[i][j],9);
	}
	printf("\n\nMx2%c%cMx%c%cMxy%c%cMy\n",9,9,9,9,9,9);
	for (int i = 0; i < 4; i++) printf("%lf%c",matrM[0][i],9);
	printf("\n\na = %lf | b = %lf\n\nf | ",matrab[0][0],matrab[1][0]);
	for (int i = 0; i < 4; i++) printf("%lf%c",matrf[0][i],9);
	printf("\n\npog = %lf | x = %lf | f = %lf\n\n\n\n",pog,x,f);

	freeMatr(matrM, 1); freeMatr(matrab, 2);
	freeMatr(matrf, 1);



	matrM = memoryAllocationDouble(7, 1); M7(matr, matrM, n);
	matrab = memoryAllocationDouble(1, 3); summKvRazn = 0;
	matrf = memoryAllocationDouble(4, 1);
	double** matr1 = memoryAllocationDouble(4, 3);
	double** matr2 = memoryAllocationDouble(3, 3);
	
	for (int i = 0; i < 3; i++)
	{
		for (int j = 0; j < 3; j++)
			matr1[i][j] = i==j && i==2 ? 1 : matrM[0][j + i];
	}
	for (int i = 0; i < 3; i++)
		matr1[i][3] = matrM[0][4+i];

	mobr(matr1, matr2);
	copyMatr(matr1, matr2, matrab);
	
	for (int i = 0; i < 4; i++) matrf[0][i] = matrab[0][0] * powf(matr[0][i], 2) + matrab[1][0] * matr[0][i] + matrab[2][0];
	f = matrab[0][0] * powf(x, 2) + matrab[1][0] * x + matrab[2][0];
	for (int i = 0; i < 4; i++) summKvRazn += powf((matr[1][i]-matrf[0][i]),2);
	pog = sqrtf(summKvRazn);

	printf("Kvadratichnaya");
	for (int i = 0; i < 2; i++)
	{
		printf("\n%c | ",i==0?'x':'y');
		for (int j = 0; j < 4; j++) printf("%lf%c",matr[i][j],9);
	}
	printf("\n\nMx4%c%cMx3%c%cMx2%c%cMx%c%cMx2y%c%cMxy%c%cMy\n",9,9,9,9,9,9,9,9,9,9,9,9);
	for (int i = 0; i < 7; i++) printf("%lf%c",matrM[0][i],9);
	printf("\n\na%c%cb%c%cc%c%cprov",9,9,9,9,9,9);
	for (int i = 0; i < 3; i++)
	{
		printf("\n");
		for (int j = 0; j < 4; j++) printf("%lf%c",matr1[i][j],9);
	}
	printf("\n");
	for (int i = 0; i < 3; i++)
	{
		printf("\n");
		for (int j = 0; j < 3; j++) printf("%lf%c",matr2[i][j],9);
	}
	printf("\n\na = %lf | b = %lf | c = %lf\n\nf | ",matrab[0][0],matrab[1][0],matrab[2][0]);
	for (int i = 0; i < 4; i++) printf("%lf%c",matrf[0][i],9);
	printf("\n\npog = %lf | x = %lf | f = %lf\n\n\n\n",pog,x,f);

	freeMatr(matrM, 1); freeMatr(matrab, 3);
	freeMatr(matrf, 1);	freeMatr(matr1, 3);
	freeMatr(matr2, 3);



	matr1 = memoryAllocationDouble(4, 2);
	for (int i = 0; i < 2; i++)
	{
		for (int j = 0; j < 4; j++)
			matr1[i][j] = log(matr[i][j]);
	}
	matrM = memoryAllocationDouble(4, 1); M4(matr1, matrM, n);
	matrab = memoryAllocationDouble(1, 2); summKvRazn = 0;
	matrf = memoryAllocationDouble(4, 1);
	double** matrAB = memoryAllocationDouble(1, 2);
	matrAB[0][0] = af(matrM); matrAB[1][0] = bf(matrM, matrAB[0][0]);
	matrab[0][0] = exp(matrAB[1][0]); matrab[1][0] = matrAB[0][0];

	for (int i = 0; i < 4; i++) matrf[0][i] = matrab[0][0] * powf(matr[0][i], matrab[1][0]);
	f = matrab[0][0] * powf(x, matrab[1][0]);
	for (int i = 0; i < 4; i++) summKvRazn += powf((matr[1][i]-matrf[0][i]),2);
	pog = sqrtf(summKvRazn);

	printf("Stepennaya");
	for (int i = 0; i < 2; i++)
	{
		printf("\n%c | ",i==0?'x':'y');
		for (int j = 0; j < 4; j++) printf("%lf%c",matr[i][j],9);
	}
	printf("\n\nln(x), ln(y)");
	for (int i = 0; i < 2; i++)
	{
		printf("\n%s | ",i==0?"x":"y");
		for (int j = 0; j < 4; j++) printf("%lf%c",matr1[i][j],9);
	}
	printf("\n\nMx2%c%cMx%c%cMxy%c%cMy\n",9,9,9,9,9,9);
	for (int i = 0; i < 4; i++) printf("%lf%c",matrM[0][i],9);
	printf("\n\nA = %lf | B = %lf",matrAB[0][0],matrAB[1][0]);
	printf(" |=| a = %lf | b = %lf\n\nf | ",matrab[0][0],matrab[1][0]);
	for (int i = 0; i < 4; i++) printf("%lf%c",matrf[0][i],9);
	printf("\n\npog = %lf | x = %lf | f = %lf\n\n\n\n",pog,x,f);



	for (int i = 0; i < 2; i++)
	{
		for (int j = 0; j < 4; j++)
			matr1[i][j] = i == 0 ? matr[i][j] : log(matr[i][j]);
	} M4(matr1, matrM, n); summKvRazn = 0;
	matrAB[0][0] = af(matrM); matrAB[1][0] = bf(matrM, matrAB[0][0]);
	matrab[0][0] = exp(matrAB[1][0]); matrab[1][0] = matrAB[0][0];

	for (int i = 0; i < 4; i++) matrf[0][i] = matrab[0][0] * exp(matr[0][i] * matrab[1][0]);
	f = matrab[0][0] * exp(x * matrab[1][0]);
	for (int i = 0; i < 4; i++) summKvRazn += powf((matr[1][i]-matrf[0][i]),2);
	pog = sqrtf(summKvRazn);

	printf("Pokazatel'naya");
	for (int i = 0; i < 2; i++)
	{
		printf("\n%c | ",i==0?'x':'y');
		for (int j = 0; j < 4; j++) printf("%lf%c",matr[i][j],9);
	}
	printf("\n\nx, ln(y)");
	for (int i = 0; i < 2; i++)
	{
		printf("\n%s | ",i==0?"x":"y");
		for (int j = 0; j < 4; j++) printf("%lf%c",matr1[i][j],9);
	}
	printf("\n\nMx2%c%cMx%c%cMxy%c%cMy\n",9,9,9,9,9,9);
	for (int i = 0; i < 4; i++) printf("%lf%c",matrM[0][i],9);
	printf("\n\nA = %lf | B = %lf",matrAB[0][0],matrAB[1][0]);
	printf(" |=| a = %lf | b = %lf\n\nf | ",matrab[0][0],matrab[1][0]);
	for (int i = 0; i < 4; i++) printf("%lf%c",matrf[0][i],9);
	printf("\n\npog = %lf | x = %lf | f = %lf\n\n\n\n",pog,x,f);




	for (int i = 0; i < 2; i++)
	{
		for (int j = 0; j < 4; j++)
			matr1[i][j] = i == 0 ? matr[i][j] : 1/matr[i][j];
	} M4(matr1, matrM, n); summKvRazn = 0;
	matrAB[0][0] = af(matrM); matrAB[1][0] = bf(matrM, matrAB[0][0]);
	matrab[0][0] = matrAB[0][0]; matrab[1][0] = matrAB[1][0];

	for (int i = 0; i < 4; i++) matrf[0][i] = 1/(matrab[0][0] * matr[0][i] + matrab[1][0]);
	f = 1/(matrab[0][0] * x + matrab[1][0]);
	for (int i = 0; i < 4; i++) summKvRazn += powf((matr[1][i]-matrf[0][i]),2);
	pog = sqrtf(summKvRazn);

	printf("Drobno-lineynaya");
	for (int i = 0; i < 2; i++)
	{
		printf("\n%c | ",i==0?'x':'y');
		for (int j = 0; j < 4; j++) printf("%lf%c",matr[i][j],9);
	}
	printf("\n\nx, 1/y");
	for (int i = 0; i < 2; i++)
	{
		printf("\n%s | ",i==0?"x":"y");
		for (int j = 0; j < 4; j++) printf("%lf%c",matr1[i][j],9);
	}
	printf("\n\nMx2%c%cMx%c%cMxy%c%cMy\n",9,9,9,9,9,9);
	for (int i = 0; i < 4; i++) printf("%lf%c",matrM[0][i],9);
	printf("\n\nA = %lf | B = %lf",matrAB[0][0],matrAB[1][0]);
	printf(" |=| a = %lf | b = %lf\n\nf | ",matrab[0][0],matrab[1][0]);
	for (int i = 0; i < 4; i++) printf("%lf%c",matrf[0][i],9);
	printf("\n\npog = %lf | x = %lf | f = %lf\n\n\n\n",pog,x,f);




	for (int i = 0; i < 2; i++)
	{
		for (int j = 0; j < 4; j++)
			matr1[i][j] = i == 1 ? matr[i][j] : log(matr[i][j]);
	} M4(matr1, matrM, n); summKvRazn = 0;
	matrAB[0][0] = af(matrM); matrAB[1][0] = bf(matrM, matrAB[0][0]);
	matrab[0][0] = matrAB[0][0]; matrab[1][0] = matrAB[1][0];

	for (int i = 0; i < 4; i++) matrf[0][i] = matrab[0][0] * log(matr[0][i]) + matrab[1][0];
	f = matrab[0][0] * log(x) + matrab[1][0];
	for (int i = 0; i < 4; i++) summKvRazn += powf((matr[1][i]-matrf[0][i]),2);
	pog = sqrtf(summKvRazn);

	printf("Logarifmicheskaya");
	for (int i = 0; i < 2; i++)
	{
		printf("\n%c | ",i==0?'x':'y');
		for (int j = 0; j < 4; j++) printf("%lf%c",matr[i][j],9);
	}
	printf("\n\nln(x), y");
	for (int i = 0; i < 2; i++)
	{
		printf("\n%s | ",i==0?"x":"y");
		for (int j = 0; j < 4; j++) printf("%lf%c",matr1[i][j],9);
	}
	printf("\n\nMx2%c%cMx%c%cMxy%c%cMy\n",9,9,9,9,9,9);
	for (int i = 0; i < 4; i++) printf("%lf%c",matrM[0][i],9);
	printf("\n\nA = %lf | B = %lf",matrAB[0][0],matrAB[1][0]);
	printf(" |=| a = %lf | b = %lf\n\nf | ",matrab[0][0],matrab[1][0]);
	for (int i = 0; i < 4; i++) printf("%lf%c",matrf[0][i],9);
	printf("\n\npog = %lf | x = %lf | f = %lf\n\n\n\n",pog,x,f);




	for (int i = 0; i < 2; i++)
	{
		for (int j = 0; j < 4; j++)
			matr1[i][j] = i == 1 ? matr[i][j] : 1/matr[i][j];
	} M4(matr1, matrM, n); summKvRazn = 0;
	matrAB[0][0] = af(matrM); matrAB[1][0] = bf(matrM, matrAB[0][0]);
	matrab[0][0] = matrAB[0][0]; matrab[1][0] = matrAB[1][0];

	for (int i = 0; i < 4; i++) matrf[0][i] = matrab[0][0] / matr[0][i] + matrab[1][0];
	f = matrab[0][0] / x + matrab[1][0];
	for (int i = 0; i < 4; i++) summKvRazn += powf((matr[1][i]-matrf[0][i]),2);
	pog = sqrtf(summKvRazn);

	printf("Giperbola");
	for (int i = 0; i < 2; i++)
	{
		printf("\n%c | ",i==0?'x':'y');
		for (int j = 0; j < 4; j++) printf("%lf%c",matr[i][j],9);
	}
	printf("\n\n1/x, y");
	for (int i = 0; i < 2; i++)
	{
		printf("\n%s | ",i==0?"x":"y");
		for (int j = 0; j < 4; j++) printf("%lf%c",matr1[i][j],9);
	}
	printf("\n\nMx2%c%cMx%c%cMxy%c%cMy\n",9,9,9,9,9,9);
	for (int i = 0; i < 4; i++) printf("%lf%c",matrM[0][i],9);
	printf("\n\nA = %lf | B = %lf",matrAB[0][0],matrAB[1][0]);
	printf(" |=| a = %lf | b = %lf\n\nf | ",matrab[0][0],matrab[1][0]);
	for (int i = 0; i < 4; i++) printf("%lf%c",matrf[0][i],9);
	printf("\n\npog = %lf | x = %lf | f = %lf\n\n\n\n",pog,x,f);




	for (int i = 0; i < 2; i++)
	{
		for (int j = 0; j < 4; j++)
			matr1[i][j] = 1/matr[i][j];
	} M4(matr1, matrM, n); summKvRazn = 0;
	matrAB[0][0] = af(matrM); matrAB[1][0] = bf(matrM, matrAB[0][0]);
	matrab[0][0] = matrAB[1][0]; matrab[1][0] = matrAB[0][0];

	for (int i = 0; i < 4; i++) matrf[0][i] = matr[0][i]/(matrab[0][0] * matr[0][i] + matrab[1][0]);
	f = x/(matrab[0][0] * x + matrab[1][0]);
	for (int i = 0; i < 4; i++) summKvRazn += powf((matr[1][i]-matrf[0][i]),2);
	pog = sqrtf(summKvRazn);

	printf("Drobno-ratsional'naya");
	for (int i = 0; i < 2; i++)
	{
		printf("\n%c | ",i==0?'x':'y');
		for (int j = 0; j < 4; j++) printf("%lf%c",matr[i][j],9);
	}
	printf("\n\n1/x, 1/y");
	for (int i = 0; i < 2; i++)
	{
		printf("\n%s | ",i==0?"x":"y");
		for (int j = 0; j < 4; j++) printf("%lf%c",matr1[i][j],9);
	}
	printf("\n\nMx2%c%cMx%c%cMxy%c%cMy\n",9,9,9,9,9,9);
	for (int i = 0; i < 4; i++) printf("%lf%c",matrM[0][i],9);
	printf("\n\nA = %lf | B = %lf",matrAB[0][0],matrAB[1][0]);
	printf(" |=| a = %lf | b = %lf\n\nf | ",matrab[0][0],matrab[1][0]);
	for (int i = 0; i < 4; i++) printf("%lf%c",matrf[0][i],9);
	printf("\n\npog = %lf | x = %lf | f = %lf\n",pog,x,f);

	freeMatr(matr, 2); freeMatr(matrM, 1); freeMatr(matrAB, 2);
	freeMatr(matrab, 2); freeMatr(matrf, 1); freeMatr(matr1, 2);
}
