#include <stdio.h>
#include "include/troposphere_lib.h"


int main(int argc, char *argv[])
{
  int pwm;
  printf("Jibo fan speed set example\n");
  
  scanf("%d", &pwm);
  printf("Setting jibos fan speed to pwm: %d\n", pwm );

    troposphere_api.setFanSpeed(pwm);


  return 0;
}
