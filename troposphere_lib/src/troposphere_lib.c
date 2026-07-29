#include "../include/dev/fan_pwm.h"
#include "../include/troposphere_lib.h"
#include <stdlib.h>

const Troposphere_API troposphere_api = {

  .setFanSpeed = set_fanPWM,


};
