#include <stdio.h>


#ifndef X265_APPROX_H
#define X265_APPROX_H

class approx
{
public:
    approx();
unsigned long long __attribute__((optimize("O0"))) add_approx(unsigned long long start_address, unsigned long long end_address) ;

unsigned long long __attribute__((optimize("O0"))) remove_approx(unsigned long long start_address, unsigned long long end_address) ;

double __attribute__((optimize("O0"))) set_read_ber(double read_ber) ;

double __attribute__((optimize("O0"))) set_write_ber(double write_ber) ;

double __attribute__((optimize("O0"))) get_read_ber(double *read_ber) ;

double __attribute__((optimize("O0"))) get_write_ber(double *write_ber) ;



#define APPROX_on

#define heap_array_in
#define heap_array_tmp_image
#define heap_array_bp
#define heap_array_dp
#define heap_array_cgx
#define heap_array_cgy
#define heap_array_mid
#define heap_array_r_edges
#define heap_array_r_corners
};

#endif
