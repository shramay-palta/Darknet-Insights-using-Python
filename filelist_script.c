#include <stdio.h>


int main (){

int i=1;
	//feb
	for (i=1;i<=28;i++){
		printf("data-telescope-meta-flowtuple -d / -p datasource=ucsd-nt/year=2013/month=2/day=%d/ \n",i);
	}
	//march
	for (i=1;i<=31;i++){
		printf("data-telescope-meta-flowtuple -d / -p datasource=ucsd-nt/year=2013/month=3/day=%d/ \n",i);
	}
	//april
	for (i=1;i<=30;i++){
		printf("data-telescope-meta-flowtuple -d / -p datasource=ucsd-nt/year=2013/month=4/day=%d/ \n",i);
	}

}