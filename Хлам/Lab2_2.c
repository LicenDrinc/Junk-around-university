#include <stdio.h>
#include <math.h>

double F(double x)
{
	return (x - 2) * cos(x) - 1;
}
double F1(double x)
{
	return cos(x) - (x-2) * sin(x);
}
double meABS(double x)
{
	if (x < 0) return -x;
	else return x;
}
// gcc -Wall -g -o "Lab2_2.exe" "Lab2_2.c" -lm -fopenmp & Lab2_2.exe > result.txt
int main(int argc, char **argv)
{
	double xa = -5, xb = -1;
	double xLeft, xRight;
	double x = xa;
	while (x < xb)
	{
		if (F(x) * F(x + 0.1) < 0)
		{
			xLeft = x; xRight = x + 0.1;
			printf("%lf %lf ++++++++\n",xLeft,xRight);
			break;
		}
		else
			printf("%lf %lf\n",x,x + 0.1);
		x = x + 0.1;
	}



	printf("\npol deleniy\n");
	double x0 = xLeft, x1 = xRight,
		x2 = (x0 + x1) / 2,
		f0 = F(x0), f2 = F(x2),
		x01 = meABS(x0 - x1);
	int i = 1;
	while (!(meABS(f2) <= 0.000001 || x01 <= 0.000001))
	{
		printf("%d | x0 = %lf, x1 = %lf, x2 = %lf, f(x0) = %lf, f(x2) = %lf, |f(x2)| = %lf, |x0 - x1| = %lf\n",i,x0,x1,x2,f0,f2,meABS(f2),x01);
		x0 = f0 * f2 < 0 ? x0 : x2;
		x1 = f0 * f2 < 0 ? x2 : x1;
		x2 = (x0 + x1) / 2;
		f0 = F(x0); f2 = F(x2);
		x01 = meABS(x0 - x1);
		i++;
	}
	printf("%d | x0 = %lf, x1 = %lf, x2 = %lf, f(x0) = %lf, f(x2) = %lf, |f(x2)| = %lf, |x0 - x1| = %lf | koren |\n",i,x0,x1,x2,f0,f2,meABS(f2),x01);
	


	printf("\nhorda\n");
	x0 = xLeft; x1 = xRight;
	x2 = x0 - F(x0) * (x1 - x0) / (F(x1) - F(x0));
	x01 = meABS(x0 - x1);
	i = 1;
	while (!(meABS(F(x2)) <= 0.000001 || x01 <= 0.000001))
	{
		printf("%d | x0 = %lf, x1 = %lf, f(x0) = %lf, f(x1) = %lf, x2 = %lf, f(x2) = %lf, |f(x2)| = %lf, |x0 - x1| = %lf\n",i,x0,x1,F(x0),F(x1),x2,F(x2),meABS(F(x2)),x01);
		x0 = F(x0) * F(x2) < 0 ? x0 : x2;
		x1 = F(x0) * F(x2) < 0 ? x2 : x1;
		x2 = x0 - F(x0) * (x1 - x0) / (F(x1) - F(x0));
		x01 = meABS(x0 - x1);
		i++;
	}
	printf("%d | x0 = %lf, x1 = %lf, f(x0) = %lf, f(x1) = %lf, x2 = %lf, f(x2) = %lf, |f(x2)| = %lf, |x0 - x1| = %lf | koren |\n",i,x0,x1,F(x0),F(x1),x2,F(x2),meABS(F(x2)),x01);
	



	printf("\nsekush'ih\n");
	x0 = xLeft; x1 = xRight;
	x2 = x1 - F(x1) * (x1 - x0) / (F(x1) - F(x0));
	x01 = meABS(x0 - x1);
	i = 1;
	while (!(meABS(F(x2)) <= 0.000001 || x01 <= 0.000001))
	{
		printf("%d | x0 = %lf, x1 = %lf, f(x0) = %lf, f(x1) = %lf, x2 = %lf, f(x2) = %lf, |f(x2)| = %lf, |x0 - x1| = %lf\n",i,x0,x1,F(x0),F(x1),x2,F(x2),meABS(F(x2)),x01);
		x0 = F(x0) * F(x2) < 0 ? x0 : x2;
		x1 = F(x0) * F(x2) < 0 ? x2 : x1;
		x2 = x1 - F(x1) * (x1 - x0) / (F(x1) - F(x0));
		x01 = meABS(x0 - x1);
		i++;
	}
	printf("%d | x0 = %lf, x1 = %lf, f(x0) = %lf, f(x1) = %lf, x2 = %lf, f(x2) = %lf, |f(x2)| = %lf, |x0 - x1| = %lf | koren |\n",i,x0,x1,F(x0),F(x1),x2,F(x2),meABS(F(x2)),x01);
	
	
	
	
	printf("\nNewton\n1 sposob\n");
	x0 = -5;
	x1 = x0 - F(x0)/F1(x0);
	x01 = meABS(x0 - x1);
	i = 1;
	while (!(meABS(F(x1)) <= 0.000001 || x01 <= 0.000001))
	{
		printf("%d | x0 = %lf, x1 = %lf, f(x0) = %lf, f'(x0) = %lf, |f(x1)| = %lf, |x0 - x1| = %lf\n",i,x0,x1,F(x0),F1(x0),meABS(F(x1)),x01);
		x0 = x1;
		x1 = x0 - F(x0)/F1(x0);
		x01 = meABS(x0 - x1);
		i++;
	}
	printf("%d | x0 = %lf, x1 = %lf, f(x0) = %lf, f'(x0) = %lf, |f(x1)| = %lf, |x0 - x1| = %lf | koren |\n",i,x0,x1,F(x0),F1(x0),meABS(F(x1)),x01);
	
	printf("\n2 sposob\n");
	x0 = -1;
	x1 = x0 - F(x0)/F1(x0);
	x01 = meABS(x0 - x1);
	i = 1;
	while (!(meABS(F(x1)) <= 0.000001 || x01 <= 0.000001))
	{
		printf("%d | x0 = %lf, x1 = %lf, f(x0) = %lf, f'(x0) = %lf, |f(x1)| = %lf, |x0 - x1| = %lf\n",i,x0,x1,F(x0),F1(x0),meABS(F(x1)),x01);
		x0 = x1;
		x1 = x0 - F(x0)/F1(x0);
		x01 = meABS(x0 - x1);
		i++;
	}
	printf("%d | x0 = %lf, x1 = %lf, f(x0) = %lf, f'(x0) = %lf, |f(x1)| = %lf, |x0 - x1| = %lf | koren |\n",i,x0,x1,F(x0),F1(x0),meABS(F(x1)),x01);
	
	
	
	printf("\nMPI\n");
	x = xLeft;
	double max = meABS(F1(x));
	double m = 1 / max;
	for (x = x + 0.01; x <= xRight; x += 0.01)
	{
		if (meABS(F1(x)) > max)
			max = meABS(F1(x));
		m = 1 / max;
	}
	x = xLeft;
	double maxf = 1 - m * meABS(F1(x));
	while (x <= xRight)
	{
		printf("x = %lf, F'(x) = %lf, |F'(x)| = %lf, m = %lf, f'(x) = %lf\n",x,F1(x),meABS(F1(x)), m, 1 - m * meABS(F1(x)));
		if (1 - m * meABS(F1(x)) > maxf)
			maxf = 1 - m * meABS(F1(x));
		x += 0.01;
	}
	
	printf("\n");
	x0 = xLeft;
	x1 = x0 - m * F(x0);
	x01 = meABS(x0 - x1);
	i = 1;
	while (!(x01 <= 0.000001 * (1 - maxf) / maxf))
	{
		printf("%d | x0 = %lf, x1 = %lf, F(x0) = %lf, f(x0) = %lf, |x0 - x1| = %lf\n",i,x0,x1,F(x0),x0 - m * F(x0),x01);
		x0 = x1;
		x1 = x0 - m * F(x0);
		x01 = meABS(x0 - x1);
		i++;
	}
	printf("%d | x0 = %lf, x1 = %lf, F(x0) = %lf, f(x0) = %lf, |x0 - x1| = %lf | koren |\n",i,x0,x1,F(x0),x0 - m * F(x0),x01);
}
