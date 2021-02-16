# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 13:21:38 2020

@author: ychen
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# open the mcnp output meshtal file as the input file to python
input_file=open("knife_edge_brpoly.txtmsht","r")

# make a blank memory space 2033 lists of 2034 pixel groups in a list-of-lists
spectra0 = []
spectra0_uncertainties = []
spectra2 = []
spectra2_uncertainties = []
spectra5 = []
spectra5_uncertainties = []
spectra10 = []
spectra10_uncertainties = []
energylist=np.zeros(2034)
p_list=np.linspace(-10.16,10.15,2032)

# check if a string can be converted into float
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

for i in range(0,2032):
    temporary_line = []
    for item in range(0,2033):
        temporary_line.append( 0.0 )
    spectra0.append( temporary_line.copy() )
    spectra0_uncertainties.append( temporary_line.copy() )
    spectra2.append( temporary_line.copy() )
    spectra2_uncertainties.append( temporary_line.copy() )
    spectra5.append( temporary_line.copy() )
    spectra5_uncertainties.append( temporary_line.copy() )
    spectra10.append( temporary_line.copy() )
    spectra10_uncertainties.append( temporary_line.copy() )

while 1 :
    # read a single line
    temporary_line = input_file.readline()
    # if we've gotten to the end of the file and there's nothing left,
    # even a blank line with an endline character will have length of 1
    if( len(temporary_line) < 1 ) :
        print( 'found an end of file condition and will break' )
        break
    # split that line of characters at the whitespace
    temporary_line_split = temporary_line.split()
    
    
    # #check for keywords, 0 inches.
    if(temporary_line_split[:3]==['X','bin:','575.52']):
        temporary_line = input_file.readline()
        temporary_line = input_file.readline()
        temporary_line_split = temporary_line.split()
        if (temporary_line_split[:1]==['Tally']):
            temporary_line = input_file.readline()
            for i in range (0,2032):
                temp_line=input_file.readline()
                temp_line_split=temp_line.split()
                for ii in range(0,2033):
                    spectra0[i][ii]=float(temp_line_split[ii])
            temporary_line = input_file.readline()
            temporary_line = input_file.readline()
            temporary_line = input_file.readline()
            for i in range (0,2032):
                temp_line=input_file.readline()
                temp_line_split=temp_line.split()
                for ii in range(0,2033):
                    spectra0_uncertainties[i][ii]=float(temp_line_split[ii])
    
    # #check for keywords, 2 inches.
    if(temporary_line_split[:3]==['X','bin:','580.60']):
        temporary_line = input_file.readline()
        temporary_line = input_file.readline()
        temporary_line_split = temporary_line.split()
        if (temporary_line_split[:1]==['Tally']):
            temporary_line = input_file.readline()
            for i in range (0,2032):
                temp_line=input_file.readline()
                temp_line_split=temp_line.split()
                for ii in range(0,2033):
                    spectra2[i][ii]=float(temp_line_split[ii])
            temporary_line = input_file.readline()
            temporary_line = input_file.readline()
            temporary_line = input_file.readline()
            for i in range (0,2032):
                temp_line=input_file.readline()
                temp_line_split=temp_line.split()
                for ii in range(0,2033):
                    spectra2_uncertainties[i][ii]=float(temp_line_split[ii])
                       
    # #check for keywords, 5 inches.
    if(temporary_line_split[:3]==['X','bin:','588.22']):
        temporary_line = input_file.readline()
        temporary_line = input_file.readline()
        temporary_line_split = temporary_line.split()
        if (temporary_line_split[:1]==['Tally']):
            temporary_line = input_file.readline()
            for i in range (0,2032):
                temp_line=input_file.readline()
                temp_line_split=temp_line.split()
                for ii in range(0,2033):
                    spectra5[i][ii]=float(temp_line_split[ii])
            temporary_line = input_file.readline()
            temporary_line = input_file.readline()
            temporary_line = input_file.readline()
            for i in range (0,2032):
                temp_line=input_file.readline()
                temp_line_split=temp_line.split()
                for ii in range(0,2033):
                    spectra5_uncertainties[i][ii]=float(temp_line_split[ii])

    # #check for keywords, 10 inches.
    if(temporary_line_split[:3]==['X','bin:','600.92']):
        temporary_line = input_file.readline()
        temporary_line = input_file.readline()
        temporary_line_split = temporary_line.split()
        if (temporary_line_split[:1]==['Tally']):
            temporary_line = input_file.readline()
            for i in range (0,2032):
                temp_line=input_file.readline()
                temp_line_split=temp_line.split()
                for ii in range(0,2033):
                    spectra10[i][ii]=float(temp_line_split[ii])
            temporary_line = input_file.readline()
            temporary_line = input_file.readline()
            temporary_line = input_file.readline()
            for i in range (0,2032):
                temp_line=input_file.readline()
                temp_line_split=temp_line.split()
                for ii in range(0,2033):
                    spectra10_uncertainties[i][ii]=float(temp_line_split[ii])

#Richards curve
def esf(x,a,b,c,d):
    return d+c/(1+a*np.exp(-b*x))
#Gaussian
def gaussian(x,sigma,mu,h):
    return (h/(sigma*np.sqrt(2*np.pi))*np.exp(-(x-mu)**2/(2*sigma**2)))
#exponential
def expf(b,x):
    return np.exp(b*x)

#find the gaussian curve
def findcurve(p_list,new_list):
    #fit data to a Richards curve
    popt1,pcov2=curve_fit(esf,p_list,new_list)
    
    #make 10x data point and differentiate -> line spread function(LSF)
    points=np.linspace(-0.5,0.5,1000)
    response=esf(points,popt1[0],popt1[1],popt1[2],popt1[3])

    lsf_list=np.zeros(999)
    for i in range (999):
        lsf_list[i]=(response[i+1]-response[i])/0.01
    
    #find the peak location, reduce the curve to this small portion
    max_loc=np.where(lsf_list == np.amax(lsf_list))
    max_loc=int(max_loc[0][0])
    lower=max_loc-100
    upper=max_loc+100
    new_lsf=lsf_list[lower:upper]
    
    #normalize
    total=sum(new_lsf)
    for i in range(200):
        new_lsf[i]=new_lsf[i]/total
    
    return new_lsf

#find the average of each image plane
width=np.linspace(-0.099,0.1,200)
a=np.zeros(200)
a0=np.zeros(200)
a2=np.zeros(200)
a5=np.zeros(200)
a10=np.zeros(200)

for i in range (600):
    new_list=spectra0[716+i]
    new_list=new_list[-2032:]
    
    a=findcurve(p_list,new_list)
    a0=a0+a

for i in range (600):
    new_list=spectra2[716+i]
    new_list=new_list[-2032:]
    
    a=findcurve(p_list,new_list)
    a2=a2+a

for i in range (600):
    new_list=spectra5[716+i]
    new_list=new_list[-2032:]
    
    a=findcurve(p_list,new_list)
    a5=a5+a
    
for i in range (600):
    new_list=spectra10[716+i]
    new_list=new_list[-2032:]
    
    a=findcurve(p_list,new_list)
    a10=a10+a

a0=a0/600
a2=a2/600
a5=a5/600
a10=a10/600

total0=np.sum(a0)
total2=np.sum(a2)
total5=np.sum(a5)
total10=np.sum(a10)
for i in range (200):
    a0[i]=a0[i]/total0
    a2[i]=a2[i]/total2
    a5[i]=a5[i]/total5
    a10[i]=a10[i]/total10

# max0=np.max(a0)
# max2=np.max(a2)
# max5=np.max(a5)
# max10=np.max(a10)
# for i in range (200):
#     a0[i]=a0[i]/max0
#     a2[i]=a2[i]/max2
#     a5[i]=a5[i]/max5
#     a10[i]=a10[i]/max10

plt.figure(0)
plt.plot(width,a0,'b',label='0 inches')
plt.plot(width,a2,'g',label='2 inches')
plt.plot(width,a5,'r',label='5 inches')
plt.plot(width,a10,'y',label='10 inches')
plt.xlabel('pixel (cm)')
plt.ylabel('neutron intensity fractions')
plt.legend()

#fitting
vals0, covar0=curve_fit(gaussian,width,a0)
vals2, covar2=curve_fit(gaussian,width,a2)
vals5, covar5=curve_fit(gaussian,width,a5)
vals10, covar10=curve_fit(gaussian,width,a10)

new_a0=gaussian(width,vals0[0],vals0[1],vals0[2])
new_a2=gaussian(width,vals2[0],vals2[1],vals2[2])
new_a5=gaussian(width,vals5[0],vals5[1],vals5[2])
new_a10=gaussian(width,vals10[0],vals10[1],vals10[2])

plt.figure(1)
plt.plot(width,a0,'r',label='data0')
plt.plot(width,new_a0,'g',label='fitted0')
plt.ylabel('relative flux')
plt.xlabel('pixels(cm)')
plt.legend()

plt.figure(2)
plt.plot(width,a2,'r',label='data2')
plt.plot(width,new_a2,'g',label='fitted2')
plt.ylabel('relative flux')
plt.xlabel('pixels(cm)')
plt.legend()

plt.figure(3)
plt.plot(width,a5,'r',label='data5')
plt.plot(width,new_a5,'g',label='fitted5')
plt.ylabel('relative flux')
plt.xlabel('pixels(cm)')
plt.legend()

plt.figure(4)
plt.plot(width,a10,'r',label='data10')
plt.plot(width,new_a10,'g',label='fitted10')
plt.ylabel('relative flux')
plt.xlabel('pixels(cm)')
plt.legend()

# fwhm0=2.355*np.std(a0)
# fwhm2=2.355*np.std(a2)
# fwhm5=2.355*np.std(a5)
# fwhm10=2.355*np.std(a10)

# new_fwhm0=2.355*np.std(new_a0)
# new_fwhm2=2.355*np.std(new_a2)
# new_fwhm5=2.355*np.std(new_a5)
# new_fwhm10=2.355*np.std(new_a10)

fwhm0=np.abs(vals0[0])
fwhm2=np.abs(vals2[0])
fwhm5=np.abs(vals5[0])
fwhm10=np.abs(vals10[0])

# print('original averaged data fwhm:',fwhm0,fwhm2,fwhm5,fwhm10)
# print('fitted averaged data fwhm:',new_fwhm0,new_fwhm2,new_fwhm5,new_fwhm10)
print("fwhm(cm):",fwhm0,fwhm2,fwhm5,fwhm10)

m=10000
n=10
upper=m+n
lower=m

pixel=np.linspace(-0.1,0.1,m*2+1)
#super samling the new lsf
new_a0=gaussian(pixel,vals0[0],vals0[1],vals0[2])
new_a2=gaussian(pixel,vals2[0],vals2[1],vals2[2])
new_a5=gaussian(pixel,vals5[0],vals5[1],vals5[2])
new_a10=gaussian(pixel,vals10[0],vals10[1],vals10[2])

# plt.figure(5)
# plt.plot(pixel,new_a0,'r',label='0')
# plt.plot(pixel,new_a2,'g',label='2')
# plt.plot(pixel,new_a5,'b',label='5')
# plt.plot(pixel,new_a10,'y',label='10')   

#fourier tranform
a0_fft=np.fft.fftshift(np.abs(np.fft.fft(new_a0)))/np.sqrt(len(new_a0))
a2_fft=np.fft.fftshift(np.abs(np.fft.fft(new_a2)))/np.sqrt(len(new_a2))
a5_fft=np.fft.fftshift(np.abs(np.fft.fft(new_a5)))/np.sqrt(len(new_a5))
a10_fft=np.fft.fftshift(np.abs(np.fft.fft(new_a10)))/np.sqrt(len(new_a10))

# plt.figure(5)
# plt.plot(pixel,a0_fft,'r',label='0')
# plt.plot(pixel,a2_fft,'g',label='2')
# plt.plot(pixel,a5_fft,'b',label='5')
# plt.plot(pixel,a10_fft,'y',label='10')   

max_a0_fft=np.where(a0_fft == np.amax(a0_fft))
max_a0_fft_loc=int(max_a0_fft[0][0])
max_a2_fft=np.where(a2_fft == np.amax(a2_fft))
max_a2_fft_loc=int(max_a2_fft[0][0])
max_a5_fft=np.where(a5_fft == np.amax(a5_fft))
max_a5_fft_loc=int(max_a5_fft[0][0])
max_a10_fft=np.where(a10_fft == np.amax(a10_fft))
max_a10_fft_loc=int(max_a10_fft[0][0])

pixel=pixel[lower:upper]
mtf0=a0_fft[lower:upper]
mtf2=a2_fft[lower:upper]
mtf5=a5_fft[lower:upper]
mtf10=a10_fft[lower:upper]

#normalization
for i in range (n):
    mtf0[i]=mtf0[i]/mtf0[0]
    mtf2[i]=mtf2[i]/mtf2[0]
    mtf5[i]=mtf5[i]/mtf5[0]
    mtf10[i]=mtf10[i]/mtf10[0]

val0,covar0=curve_fit(expf,pixel,mtf0)
val2,covar2=curve_fit(expf,pixel,mtf2)
val5,covar5=curve_fit(expf,pixel,mtf5)
val10,covar10=curve_fit(expf,pixel,mtf10)

fitted_mtf0=expf(pixel,val0[0])
fitted_mtf2=expf(pixel,val2[0])
fitted_mtf5=expf(pixel,val5[0])
fitted_mtf10=expf(pixel,val10[0])

plt.figure(5)
#plt.plot(pixel,mtf0,'r',label='0')
plt.plot(pixel,fitted_mtf0,'purple',label='0 inches fitted')
#plt.plot(pixel,mtf2,'g',label='2')
plt.plot(pixel,fitted_mtf2,'c',label='2 inches fitted')
#plt.plot(pixel,mtf5,'b',label='5')
plt.plot(pixel,fitted_mtf5,'m',label='5 inches fitted')
#plt.plot(pixel,mtf10,'y',label='10')
plt.plot(pixel,fitted_mtf10,'orange',label='10 inches fitted')
plt.ylabel('Normalized MTF')
plt.xlabel('Spatial frequency (cycles/cm)')
plt.legend()

res0=(np.log(0.1)/val0[0])/(2*np.pi)*10000
res2=(np.log(0.1)/val2[0])/(2*np.pi)*10000
res5=(np.log(0.1)/val5[0])/(2*np.pi)*10000
res10=(np.log(0.1)/val10[0])/(2*np.pi)*10000

spres0=1/(res0*2)
spres2=1/(res2*2)
spres5=1/(res5*2)
spres10=1/(res10*2)

print('spatial resolution(per micron):',res0,res2,res5,res10)
print('spatial resolution(micron):',spres0,spres2,spres5,spres10)

