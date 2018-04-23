

import numpy as np
import os

#for i in range(10):
#     f.write("This is line %d\r\n" % (i+1))

def write_headerSetting_sampleLines(f):
    f.write("setFormat raw;\r\n")
    f.write("\r\n")
    f.write("interpolationScheme cell;\r\n")
    f.write("\r\n")
    f.write("fields\r\n")
    f.write("(\r\n")
    f.write("\tU\r\n")
    f.write(");\r\n")

def writeLines(f,zList,N,iList):
    for i in iList:
        if i in range(N):
            f.write("\t"+"line"+str(i)+"\r\n")
            f.write("\t{\r\n")
            
            writeStartEnd0(f,zList[i])
            
            f.write("\t}\r\n")
            f.write("\r\n")
        elif i >= N and i < 2*N:
            f.write("\t"+"line"+str(i)+"\r\n")
            f.write("\t{\r\n")
            
            writeStartEnd1(f,zList[i-N])
            
            f.write("\t}\r\n")
            f.write("\r\n")
        elif i >= 2*N and i < 3*N:
            f.write("\t"+"line"+str(i)+"\r\n")
            f.write("\t{\r\n")
            
            writeStartEnd2(f,zList[i-2*N])
            
            f.write("\t}\r\n")
            f.write("\r\n")      
        elif i >= 3*N and i < 4*N:
            f.write("\t"+"line"+str(i)+"\r\n")
            f.write("\t{\r\n")
            
            writeStartEnd3(f,zList[i-3*N])
            
            f.write("\t}\r\n")
            f.write("\r\n")
        else:
            print "###########################\n"
            print "There is a problem !\n"
            print "###########################\n"
    
def writeStartEnd0(f,z):
    f.write("\t\t"+ "type\t" + "uniform;" +"\r\n")
    f.write("\t\t"+ "axis\t" + "distance;" +"\r\n")
    f.write("\t\t"+ "start\t" + "(0. 0 "+ z +");" +"\r\n")
    f.write("\t\t"+ "end\t" + "(0. -0.004 "+ z +");" +"\r\n")
    f.write("\t\t"+ "nPoints\t" + "200;" +"\r\n")

def writeStartEnd1(f,z):
    f.write("\t\t"+ "type\t" + "uniform;" +"\r\n")
    f.write("\t\t"+ "axis\t" + "distance;" +"\r\n")
    f.write("\t\t"+ "start\t" + "(0. 0 "+ z +");" +"\r\n")
    f.write("\t\t"+ "end\t" + "(0. 0.004 "+ z +");" +"\r\n")
    f.write("\t\t"+ "nPoints\t" + "200;" +"\r\n")
    
def writeStartEnd2(f,z):
    f.write("\t\t"+ "type\t" + "uniform;" +"\r\n")
    f.write("\t\t"+ "axis\t" + "distance;" +"\r\n")
    f.write("\t\t"+ "start\t" + "(0 0 "+ z +");" +"\r\n")
    f.write("\t\t"+ "end\t" + "(-0.004 0 "+ z +");" +"\r\n")
    f.write("\t\t"+ "nPoints\t" + "200;" +"\r\n")

def writeStartEnd3(f,z):
    f.write("\t\t"+ "type\t" + "uniform;" +"\r\n")
    f.write("\t\t"+ "axis\t" + "distance;" +"\r\n")
    f.write("\t\t"+ "start\t" + "(0 0 "+ z +");" +"\r\n")
    f.write("\t\t"+ "end\t" + "(0.004 0 "+ z +");" +"\r\n")
    f.write("\t\t"+ "nPoints\t" + "200;" +"\r\n")

def write_LineSet(f,zList,N,iList):
    f.write("sets\r\n")
    f.write("(\r\n")
    writeLines(f,zList,N,iList)
    f.write(");\r\n")

def write_sampleLines(fileName,zList,N,iList):
    f= open(fileName,"a")
    write_headerSetting_sampleLines(f)
    write_LineSet(f,zList,N,iList)
    f.close()
    
def NLines2Dict(N):
    #l = np.linspace(0,0.04,num=10)
    l = np.linspace(0.0052,0.0352,num=N)
    listStr = [str(x) for x in l]
    print "A list of all z positions :\n"
    print listStr
    
    dictName="../../system/sampleDict_lines"
    write_sampleLines(dictName,listStr,N,range(4*N))
    
    os.system('dos2unix '+dictName)

NLines2Dict(40)
#write_N_sampleLines2Dict(10)