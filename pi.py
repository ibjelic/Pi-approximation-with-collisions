import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#1 left body
#2 right body
#y coordinate doesnt change and its 0

dt = 0.0001; #time step
m = [1,100] #masses left body, right body 
v1=0 #velocity 
v2=-1 
x1=1 #position 
x2=1.15 
S=[x1,x2,v1,v2] #state matrix
Sn=deepcopy(S) #next state matrix
brs=0; #number of collisions
bb = [] #array of collisions for animation
x1,x2 = [],[] #array of coordinates for animation

while(1): #simulation
	bb.append(brs) 
	Sn[0]=deepcopy(S[0])+deepcopy(S[2])*dt; #change of coordinates Xnew=Xold+V*dt
	Sn[1]=deepcopy(S[1])+deepcopy(S[3])*dt;
	if(Sn[0]<0): #collision with wall
		brs=brs+1; #collisions+1
		Sn[2]=-deepcopy(Sn[2]); #speed changes sign because its elastic collision

	if(Sn[0]>Sn[1]): #collision of bodies
		brs=brs+1; #c+1
		Sn[2]=2*m[1]*deepcopy(S[3])/(m[0]+m[1])+(m[0]-m[1])*deepcopy(S[2])/(m[0]+m[1]); #calculate new speed after collision 
		Sn[3]=2*m[0]*deepcopy(S[2])/(m[0]+m[1])-(m[0]-m[1])*deepcopy(S[3])/(m[0]+m[1]); #Sn/S[2] body 1, Sn/S[3] body 2
	x1.append(S[0]) 
	x2.append(S[1])
	S=deepcopy(Sn); #setting new state to be current state
	if(brs>0 and np.abs(Sn[2])<np.abs(Sn[3]) and Sn[2]>=0): #stop simulation when there is no possibility for next collision
		break;						#that means 2nd body is moving to right and 1st body is following it with lower speed
	
print(brs)

mult = 100 #how much faster do you want to see your simulation in animation

def update_plot(i, fig, scat):
	bonus=0
	if(i>int(len(x1)/mult)-2): #added this because animation will stop and legend wont update for last collision
		bonus=1		
	k=mult*i #row index multiplied by mult so you dont watch every index as frame (because its slow)
	lx1= [x1[k],x2[k]+0.03] #plotting more dots /x coordinates
	lx2= [0,0] # /y coordinates
	scat.set_data(lx1,lx2) 
	txt.set_text('x1= %.3f   m1=%.0f\nx2= %.3f   m1=%.0f\nCollisions=%.0f\n t=%.3fs' %(x1[k],m[0], x2[k],m[1],bb[k]+bonus,(k*dt))) #update of legend
	return scat,

fig =  plt.figure() 
ax = fig.add_subplot(111)
ax.set_xlim([-0.1, 3]) #animation scale
ax.set_ylim([-0.1,3])
txt = ax.text(0.05, 0.8, '', transform=ax.transAxes) #legend position
scat, = ax.plot([], [], 's', c='b') #plot type (s=square)

anim = animation.FuncAnimation(fig, update_plot, fargs = (fig, scat),
                               frames = int(len(x1)/mult), interval = 1, repeat=False)
anim.save('sudar.mp4', fps=25) #save animation
plt.show() #show animation
