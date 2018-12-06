#include <stdint.h>
#include "approx.h"

int main(int argc, char **argv)
{

 uint8_t matrix [200][200];

 uint8_t *ptr[200][200];

int i =0;
int j =0;

ptr = matrix;

    unsigned long long start_approx_add, end_approx_add;

    start_approx_add = (unsigned long long)(ptr);
    end_approx_add = (unsigned long long)(&ptr +(200*200*sizeof(uint8_t)));
    
    
    add_approx(start_approx_add, end_approx_add);
    
    set_write_ber((double)(1E-1));            

    set_read_ber((double)(1E-1)); 

for ( i = 0; i < 200; i++){
	for (j = 0; j < 200; j++){
		
		matrix[i][j] = 1;
	}
}	
while (matrix[199][199] < 9){
	for ( i = 0; i < 200; i++){
		for (j = 0; j < 200; j++){
		
			matrix[i][j] += 1;
		}
	}
}

j=0;
i =0;

for (i = 0; i < 200; i++){
	
	for (j = 0; j < 200; j++){
		printf(" %i,", matrix[i][j]);
		
	}
printf("\n");

}


	printf(" \n%llu end %llu\n", start_approx_add, end_approx_add);
 remove_approx(start_approx_add, end_approx_add);

  return 0;
}
