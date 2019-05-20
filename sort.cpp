#include "string.h"
#include "stdlib.h"
#include "stdio.h"
#include "time.h"
#define random(x) (rand()%x)
int a[100000];

void load(char filename[]) //写文件
{
	int i;
	FILE *fp;
	fp=fopen(filename,"w");
	if(fp==NULL)
	{
		printf("cannot open file/n");
		return;
	}
	for(i=0;i<1000000;i++) 
		fprintf(fp,"%d ",a[i]);  
}

int partitions(int a[],int low,int high)   
{
	int pivotkey=a[low];   //基准
	while(low<high)
	{
		while(low<high && a[high]>=pivotkey)
			--high;
		a[low]=a[high];
		while(low<high && a[low]<=pivotkey)
			++low;
    	a[high]=a[low];
	}
	a[low]=pivotkey;
	return low;
} 
  
void qsort(int a[],int low,int high)   //快速排序
{
	int pivotkey;
	if(low<high)
	{
		//递归调用
		pivotkey=partitions(a,low,high);
		qsort(a,low,pivotkey-1);
		qsort(a,pivotkey+1,high);
	}
}

int main(void)
{
	int i;
	char filename[20];
	srand( (unsigned)time( NULL ) );     //初始化随机数
	for(i=0;i<1000000;i++)                //打印出10W个随机数
		a[i]=rand();
	strcpy(filename,"generate.txt");
	load(filename);
	qsort(a,0,1000000);  //快速排序
	strcpy(filename,"sort.txt");
	load(filename);
	system("pause");
	return 0;
}
