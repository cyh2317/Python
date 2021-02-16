# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 13:59:53 2020

@author: ychen
"""

import numpy as np

input_file=open("beamdivergence.txt","r")

angle= np.zeros(601)
box = []
box_error = []
boxf = []
boxf_error = []
text_string=""
# check if a string can be converted into float
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

for ii in range(0,6):
    temporary_line = []
    for item in range(0,601):
        temporary_line.append( 0.0 )
    box.append( temporary_line.copy() )
    box_error.append( temporary_line.copy() )
    boxf.append( temporary_line.copy() )
    boxf_error.append( temporary_line.copy() )

i=0
while 1:
    input_file.readline()
    temporary_line = input_file.readline()
    temporary_line_split = temporary_line.split()
    if( len(temporary_line) < 1 ) :
        print( 'found an end of file condition and will break' )
        break

    if(temporary_line_split[:2]==['surface','6.2']):
        temporary_line = input_file.readline()
        temporary_line_split = temporary_line.split()
        if (temporary_line_split[:1]==['angle']):
            temp_line = input_file.readline()
            temp_line_split = temporary_line.split()
            angle[i]=temp_line_split[4]
            i=i+1

for j in range (0,600):
    angle[j]=round(np.arccos(angle[j])*180/np.pi)
input_file.close()

for k in range (6):
    surf=str(6.2+k)
    input_file=open("beamdivergence.txt","r")
    i=0
    j=0
    while 1:
        input_file.readline()
        temporary_line = input_file.readline()
        temporary_line_split = temporary_line.split()
        if( len(temporary_line) < 1 ) :
            print( 'found an end of file condition and will break' )
            break
    
        if(temporary_line_split[:2]==['surface',surf]):
            temporary_line = input_file.readline()
            temporary_line_split = temporary_line.split()
            if (temporary_line_split[:1]==['flagged']):
                temporary_line = input_file.readline()
                temporary_line = input_file.readline()
                temporary_line_split = temporary_line.split()
                boxf[k][i]=float(temporary_line_split[0])
                boxf_error[k][i]=float(temporary_line_split[1])
                i=i+1
            else:
                temp_line = input_file.readline()
                temp_line_split = temp_line.split()
                box[k][j]=float(temp_line_split[0])
                box_error[k][j]=float(temp_line_split[1])
                j=j+1

input_file.close()

input_file=open("beamdivergence.txt","r")
k=1
while 1:
    surf=str(6.2+k)
    i=0
    j=0
    input_file.readline()
    temporary_line = input_file.readline()
    temporary_line_split = temporary_line.split()
    if( len(temporary_line) < 1 ) :
        print( 'found an end of file condition and will break' )
        break
    
    if(temporary_line_split[:2]==['surface',surf]):
        temporary_line = input_file.readline()
        temporary_line_split = temporary_line.split()
        if (temporary_line_split[:1]==['flagged']):
            temporary_line = input_file.readline()
            temporary_line = input_file.readline()
            temporary_line_split = temporary_line.split()
            boxf[k][i]=float(temporary_line_split[0])
            boxf_error[k][i]=float(temporary_line_split[1])
            i=i+1
        else:
            temp_line = input_file.readline()
            temp_line_split = temp_line.split()
            box[k][j]=float(temp_line_split[0])
            box_error[k][j]=float(temp_line_split[1])
            j=j+1

input_file.close()

input_file=open("beamdivergence.txt","r")
k=2
while 1:
    surf=str(6.2+k)
    i=0
    j=0
    input_file.readline()
    temporary_line = input_file.readline()
    temporary_line_split = temporary_line.split()
    if( len(temporary_line) < 1 ) :
        print( 'found an end of file condition and will break' )
        break
    
    if(temporary_line_split[:2]==['surface',surf]):
        temporary_line = input_file.readline()
        temporary_line_split = temporary_line.split()
        if (temporary_line_split[:1]==['flagged']):
            temporary_line = input_file.readline()
            temporary_line = input_file.readline()
            temporary_line_split = temporary_line.split()
            boxf[k][i]=float(temporary_line_split[0])
            boxf_error[k][i]=float(temporary_line_split[1])
            i=i+1
        else:
            temp_line = input_file.readline()
            temp_line_split = temp_line.split()
            box[k][j]=float(temp_line_split[0])
            box_error[k][j]=float(temp_line_split[1])
            j=j+1

input_file.close()

input_file=open("beamdivergence.txt","r")
k=3
while 1:
    surf=str(6.2+k)
    i=0
    j=0
    input_file.readline()
    temporary_line = input_file.readline()
    temporary_line_split = temporary_line.split()
    if( len(temporary_line) < 1 ) :
        print( 'found an end of file condition and will break' )
        break
    
    if(temporary_line_split[:2]==['surface',surf]):
        temporary_line = input_file.readline()
        temporary_line_split = temporary_line.split()
        if (temporary_line_split[:1]==['flagged']):
            temporary_line = input_file.readline()
            temporary_line = input_file.readline()
            temporary_line_split = temporary_line.split()
            boxf[k][i]=float(temporary_line_split[0])
            boxf_error[k][i]=float(temporary_line_split[1])
            i=i+1
        else:
            temp_line = input_file.readline()
            temp_line_split = temp_line.split()
            box[k][j]=float(temp_line_split[0])
            box_error[k][j]=float(temp_line_split[1])
            j=j+1

input_file.close()

input_file=open("beamdivergence.txt","r")
k=4
while 1:
    surf=str(6.2+k)
    i=0
    j=0
    input_file.readline()
    temporary_line = input_file.readline()
    temporary_line_split = temporary_line.split()
    if( len(temporary_line) < 1 ) :
        print( 'found an end of file condition and will break' )
        break
    
    if(temporary_line_split[:2]==['surface',surf]):
        temporary_line = input_file.readline()
        temporary_line_split = temporary_line.split()
        if (temporary_line_split[:1]==['flagged']):
            temporary_line = input_file.readline()
            temporary_line = input_file.readline()
            temporary_line_split = temporary_line.split()
            boxf[k][i]=float(temporary_line_split[0])
            boxf_error[k][i]=float(temporary_line_split[1])
            i=i+1
        else:
            temp_line = input_file.readline()
            temp_line_split = temp_line.split()
            box[k][j]=float(temp_line_split[0])
            box_error[k][j]=float(temp_line_split[1])
            j=j+1

input_file.close()

input_file=open("beamdivergence.txt","r")
k=5
while 1:
    surf=str(6.2+k)
    i=0
    j=0
    input_file.readline()
    temporary_line = input_file.readline()
    temporary_line_split = temporary_line.split()
    if( len(temporary_line) < 1 ) :
        print( 'found an end of file condition and will break' )
        break
    
    if(temporary_line_split[:2]==['surface',surf]):
        temporary_line = input_file.readline()
        temporary_line_split = temporary_line.split()
        if (temporary_line_split[:1]==['flagged']):
            temporary_line = input_file.readline()
            temporary_line = input_file.readline()
            temporary_line_split = temporary_line.split()
            boxf[k][i]=float(temporary_line_split[0])
            boxf_error[k][i]=float(temporary_line_split[1])
            i=i+1
        else:
            temp_line = input_file.readline()
            temp_line_split = temp_line.split()
            box[k][j]=float(temp_line_split[0])
            box_error[k][j]=float(temp_line_split[1])
            j=j+1

input_file.close()

text_string="angle 6.2ftally error 7.2ftally error 8.2ftally error 9.2ftally error 10.2ftally error 11.2ftally error"
text_string += "\n"
for i in range(0,600):
    text_string += str(angle[i])
    text_string += " "
    text_string += str(boxf[0][i])
    text_string += " "
    text_string += str(boxf_error[0][i])
    text_string += " "
    text_string += str(boxf[1][i])
    text_string += " "
    text_string += str(boxf_error[1][i])
    text_string += " "
    text_string += str(boxf[2][i])
    text_string += " "
    text_string += str(boxf_error[2][i])
    text_string += " "
    text_string += str(boxf[3][i])
    text_string += " "
    text_string += str(boxf_error[3][i])
    text_string += " "
    text_string += str(boxf[4][i])
    text_string += " "
    text_string += str(boxf_error[4][i])
    text_string += " "
    text_string += str(boxf[5][i])
    text_string += " "
    text_string += str(boxf_error[5][i])
    text_string += "\n"
    
output_file=open("f2ftallies.txt","w")
output_file.write(text_string)
output_file.close()