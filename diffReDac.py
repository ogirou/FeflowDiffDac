import sys

file1=sys.argv[1]
file2=file1[:-4]+'_diffDac_reDac.dac'
#file2=sys.argv[2]
#fileOut=sys.argv[3]

data1=open(file1,'r')
data2=open(file2,'r')

#logOut=open(fileOut,'w')

line1=data1.readline()
line2=data2.readline()

error=1e-10
count=1

while line1 != '':
  if line1[0]=='$' and line2[0]=='$': # New time step !
    lineS=line1.replace(',',' ').replace('    ',' ').replace('   ',' ').replace('  ',' ').split(' ')   
    print lineS[1]
    line1=data1.readline()
    line2=data2.readline()
    if float(lineS[1]) > 0:                        # Time step t
      while line1[0] not in ['','$','D']:           # 'D' for 'DIAGRAM'
        data_line_1=line1.split(',')[:-1]
        data_line_2=line2.split(',')[:-1]
        if len(data_line_1) != len(data_line_2) : 
          print "Different lengths of data lines"
          sys.exit(1)										
        for u in range(len(data_line_1)):
          try:
            one=float(data_line_1[u])
          except:
            one=data_line_1[u]
          try:
            two=float(data_line_2[u])
          except:
            two=data_line_2[u]
          if type(one) != type(two) :
            print "Different type of data at line :",count
            print "one =",one,"vs two =",two
          elif type(one)==float:
            if abs(one-two)>error:
              print "Error: Different values between original file and *_diffDac_reDac.dac file."
              sys.exit(1)
          else:
            pass    
          one,two='',''
        count+=1
        line1=data1.readline()
        line2=data2.readline()

  elif (line1[0]=='$' and line2[0]!='$') or (line1[0]!='$' and line2[0]=='$'):
    print "Results start at different lines."
    sys.exit(1)

  else:  
    count+=1
    line1=data1.readline()
    line2=data2.readline()


#logOut.close()
data1.close()
data2.close()

print "Done."










