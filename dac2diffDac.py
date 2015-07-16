
"""   
     
     Aim: Transform Feflow *.dac file into another *.dac file presenting data
          values differences with time step 0 instead of absolute data values

"""

# Imports #####

import sys

# Input file choice #####

try:
  input_file=sys.argv[1]
except:
  print "Usage: dac2diffDac.py FeflowFileName.dac"
  sys.exit(1)

"""
input_file='AA_AllDiri_beginningTest.dac'
input_file='BTSL_raf3d_failles_comp1_nest_couv_go_1_0.dac'

"""
output_file=input_file[:-4]+'_diffDac.dac'
input_data=open(input_file,'r')
output_data=open(output_file,'w')

# Debug tools #####

debug=0

if debug:
  test1=open('test1','w')
  test2=open('test2','w')



# Main #####

init_cond=[] # Initial conditions variable

lineInit=input_data.readline()
if lineInit=='\n' or lineInit=='\r':
  line=' '
else:
  line=lineInit.rstrip('\n\r')

while line != '': 
  
  if line[0]=='$': # New time step !
    print >> output_data, line
    lineS=line.replace(',',' ').replace('    ',' ').replace('   ',' ').replace('  ',' ').split(' ')   
    print lineS[1]
    lineInit=input_data.readline()
    if lineInit=='\n' or lineInit=='\r':
      line=' '
    else:
      line=lineInit.rstrip('\n\r')

    if float(lineS[1]) == 0:                       # Initial conditions time step
      print "Initial data record"
      while line[0] not in ['','$','D']:           # 'D' for 'DIAGRAM'
        init_cond.append(line.split(',')[:-1])     # recording IC variable
        print >> output_data, line                 # copying in output file
        lineInit=input_data.readline()
        if lineInit=='\n' or lineInit=='\r':
          line=' '
        else:
          line=lineInit.rstrip('\n\r')
  
    if float(lineS[1]) > 0:                        # Time step t
      print "Comparision initial data and time step #",lineS[1]
      count=0
      
      countFloat0=0                                # check 
      countFloatT=0                                # check 
      while line[0] not in ['','$','D'] and line [0:2] != '  ':     # 'D' for 'DIAGRAM'
        data_line_out=''
        data_line_in=line.split(',')[:-1]
        for u in range(len(data_line_in)):
          try:
            point=float(data_line_in[u])
            init=float(init_cond[count][u])
            if type(point)==float:                 # check
              countFloatT+=1                       # check
            if type(init)==float:                  # check
              countFloat0+=1                       # check
            data_line_out += '{:1.14e}, '.format(point-init)
            if countFloat0 != countFloatT:              # check
              print "Different number of floats in time step",lineS[1],"(",countFloatT,"versus",countFloat0,"at time step 0)"
            point,init='',''                       # check
            
            if u == len(data_line_in)-1 and debug:
              print >> test1, 'count',count,'u',u,'" "+data line out[:-1]',' '+data_line_out[:-1]
          except:
            data_line_out += '1.#QNAN000000000e+00, '
            if u == len(data_line_in)-1 and debug:
              print >> test1, 'count',count,'u',u,'" "+data line out[:-1]',' '+data_line_out[:-1]
        if debug:
          print >> test2, 'count',count,'u',u,'" "+data line out[:-1]',' '+data_line_out[:-1]
        print >> output_data, ' '+data_line_out[:-1] 
        lineInit=input_data.readline()
        if lineInit=='\n' or lineInit=='\r':
          line=' '
        else:
          line=lineInit.rstrip('\n\r')
        count+=1
        
        if countFloat0 != countFloatT:              # check
          
          print "Different number of floats in time step",lineS[1],"(",countFloatT,"versus",countFloat0,"at time step 0)"
         # print init_cond                          # Only for small *.dac files

    if line[0:3]=='   ':
      print >> output_data,line
      lineInit=input_data.readline()
      if lineInit=='\n' or lineInit=='\r':
        line=' '
      else:
        line=lineInit.rstrip('\n\r')


  if line[0]!='$':                                  # Normal copy
    print >> output_data, line
    lineInit=input_data.readline()
    if lineInit=='\n' or lineInit=='\r':
      line=' '
    else:
      line=lineInit.rstrip('\n\r')

# End #####

input_data.close()
output_data.close()

if debug:
  test1.close()
  test2.close()

print '\n = = = = Done = = = =\n'


