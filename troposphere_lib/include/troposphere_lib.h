#ifndef TROPOSHPERE_API_H
#define TROPOSHPERE_API_H

typedef struct{


  void (*setFanSpeed)(int pwm);


} Troposphere_API;

extern const Troposphere_API troposphere_api;



#endif
