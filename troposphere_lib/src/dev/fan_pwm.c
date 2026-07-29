#include "../../include/dev/fan_pwm.h"
#include <stdio.h>

#define FAN_DEVICE "/sys/devices/platform/pwm-fan.6/hwmon/hwmon5/pwm1"


void set_fanPWM(int pwm){

  if (pwm > 255) {
    pwm = 255;
  } else if (pwm < 100) {
    pwm = 100;
  }



  FILE *fan_file = fopen(FAN_DEVICE, "w");
  if (fan_file != NULL){

    fprintf(fan_file, "%d", pwm);
    fclose(fan_file);


  }


}
