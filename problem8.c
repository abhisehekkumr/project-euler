#include<stdio.h>

int main(){
	int a = 20, b = 50;
	int arr[a*b];

	for(int j = 0; j < a*b; j++)
		scanf("%d",&arr[j]);

	double max = 0;

		int count = 0;
		double product = 1;
		for(int j = 0; j < a*b;){
			count++;
			product = product*arr[j];
			//printf("%d ",arr[j]);
			if(count == 13){
				//printf("\n");
				count = 0;
				j = j - 11;
				max = max > product ? max:product;
				product = 1;
			}else
				j++;
		}

	printf("\n%lf\n",max);
}