#include "colors.inc"
#include "shapes.inc"
#include "textures.inc"
light_source {
<5,30,-30>
White 
}
light_source {
<-5,30,-30>
White 
}
sphere {
<1,0,-6>
0.5
finish {
ambient
0.1
diffuse
0.6 
}
pigment {
NeonPink 
} 
}
box {
<-1,-1,-1>
<1,1,1>
finish {
ambient
0.1
diffuse
0.6 
}
pigment {
Green 
}
rotate
<0,-20,0> 
}
cylinder {
<-6,6,30>
<-6,-1,30>
3
finish {
ambient
0.1
diffuse
0.6 
}
pigment {
NeonBlue 
} 
}
plane {
<0,1,0>
( -1.0 )
texture {
pigment {
checker
color
Gray65
color
Gray30 
} 
} 
}
camera {
location
<0,1,-10>
look_at
<0,1,0>
focal_point
<1,1,-6>
aperture
0.4
blur_samples
50
right
<1.3333333333333333,0,0> 
}
global_settings{

}