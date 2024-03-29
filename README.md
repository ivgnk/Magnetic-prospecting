# Magnetic-prospecting
Various calculations for magnetic prospecting

### MB
The program <font color="#0000ff"><b>MB.py</b></font> outputs the following images

**1 Image**: Magnetic field (Magnetic field induction) in nT:       
vertical component (blue)             
horizontal component (orange)          
full vector (green) of  ball            
![Figure_2](https://user-images.githubusercontent.com/20105840/204506631-070fe34d-b102-4df6-a40b-66634ec02ab7.png)


#### Data
Ball parameters:           
The ball is vertically magnetized
h - the depth of the center of the ball in meters         
R - the radius of the ball in meters        
J - magnetization in A/m             
The magnetic field is calculated on a straight line (profile or axis x) with coordinates from -250 m to 250 m with step 5 m.    
The origin of the coordinates is above the center of the ball       

#### Formulas: 
In [International System of Units, SI](https://en.wikipedia.org/wiki/International_System_of_Units)             
Magnetic moment of the ball               
$$M = \frac{4}{3} \cdot \pi \cdot J \cdot R^3                        $$

Vertical component         
$$Z_a = \frac{\mu_0}{4\pi} \cdot \frac{M(2h^2 - x^2)}{(h^2 + x^2)^{5/2}}$$           

Horizontal component
$$H_a = - \frac{\mu_0}{4\pi} \cdot \frac{3Mhx}{(h^2 + x^2)^{5/2}}$$       

Full vector        

$$T_a=\sqrt{(Z_a^2 + Н_a^2)}$$
&nbsp;
&nbsp;
&nbsp;&nbsp;              


**2 Image**:
![Figure_3](https://user-images.githubusercontent.com/20105840/204506664-fa6fcdf7-5ee6-4b8f-998e-433f183b442d.png)

Several variants of the magnetic field (vertical component, horizontal component, full vector) at different parameters of the ball occurrence are presented         
Four windows show the magnetic field for different variations of the depths of the center of the ball: 50 m, 100 m, 150 m, 200 m          
In each window there are four possible sub-variants with different values of the radius and magnetization of the ball:            
R = 10 m, J = 0.25 A/m,         
R = 10 m, J = 0.50 A/m,             
R = 20 m, J = 0.25 A/m,         
R = 20 m, J = 0.50 A/m.            

