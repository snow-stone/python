

import numpy as np
import os

def write_headerSetting_sampleLines(f):
    f.write("setFormat raw;\r\n")
    f.write("\r\n")
    f.write("interpolationScheme cell;\r\n")
    f.write("\r\n")
    f.write("fields\r\n")
    f.write("(\r\n")
    f.write("\tU\r\n")
    f.write(");\r\n")

#def writeLines(f,z_value_List,N,total_nb_of_Line,resolution):
#    for i in total_nb_of_Line:
#        if i in range(N):
#            f.write("\t"+"line"+str(i)+"\r\n")
#            f.write("\t{\r\n")
#            
#            writeStartEnd0(f,z_value_List[i],resolution)
#            
#            f.write("\t}\r\n")
#            f.write("\r\n")
#        elif i >= N and i < 2*N:
#            f.write("\t"+"line"+str(i)+"\r\n")
#            f.write("\t{\r\n")
#            
#            writeStartEnd1(f,z_value_List[i-N],resolution)
#            
#            f.write("\t}\r\n")
#            f.write("\r\n")
#        elif i >= 2*N and i < 3*N:
#            f.write("\t"+"line"+str(i)+"\r\n")
#            f.write("\t{\r\n")
#            
#            writeStartEnd2(f,z_value_List[i-2*N],resolution)
#            
#            f.write("\t}\r\n")
#            f.write("\r\n")      
#        elif i >= 3*N and i < 4*N:
#            f.write("\t"+"line"+str(i)+"\r\n")
#            f.write("\t{\r\n")
#            
#            writeStartEnd3(f,z_value_List[i-3*N],resolution)
#            
#            f.write("\t}\r\n")
#            f.write("\r\n")
#        else:
#            print "###########################\n"
#            print "There is a problem !\n"
#            print "###########################\n"


def writeLines(f,z_value_List,N,total_nb_of_Line,resolution):
    for i in total_nb_of_Line:
        whichLine = i // N
        j = i % N
        
        f.write("\t"+"line"+str(i)+"\r\n")
        f.write("\t{\r\n")
        writeStartEnd(whichLine,f,z_value_List[j],resolution)
        f.write("\t}\r\n")
        f.write("\r\n")

def writeStartEnd(whichLine,f,z,nPoints):
    if whichLine == 0:
        f.write("\t\t"+ "type\t" + "uniform;" +"\r\n")
        f.write("\t\t"+ "axis\t" + "distance;" +"\r\n")
        f.write("\t\t"+ "start\t" + "(0. 0 "+ z +");" +"\r\n")
        f.write("\t\t"+ "end\t" + "(0. -0.004 "+ z +");" +"\r\n")
        f.write("\t\t"+ "nPoints\t" + str(nPoints) + ";" +"\r\n")
    elif whichLine == 1:
        f.write("\t\t"+ "type\t" + "uniform;" +"\r\n")
        f.write("\t\t"+ "axis\t" + "distance;" +"\r\n")
        f.write("\t\t"+ "start\t" + "(0. 0 "+ z +");" +"\r\n")
        f.write("\t\t"+ "end\t" + "(0. 0.004 "+ z +");" +"\r\n")
        f.write("\t\t"+ "nPoints\t" + str(nPoints) + ";" +"\r\n")
    elif whichLine == 2:
        f.write("\t\t"+ "type\t" + "uniform;" +"\r\n")
        f.write("\t\t"+ "axis\t" + "distance;" +"\r\n")
        f.write("\t\t"+ "start\t" + "(0 0 "+ z +");" +"\r\n")
        f.write("\t\t"+ "end\t" + "(-0.004 0 "+ z +");" +"\r\n")
        f.write("\t\t"+ "nPoints\t" + str(nPoints) + ";" +"\r\n")
    elif whichLine == 3:
        f.write("\t\t"+ "type\t" + "uniform;" +"\r\n")
        f.write("\t\t"+ "axis\t" + "distance;" +"\r\n")
        f.write("\t\t"+ "start\t" + "(0 0 "+ z +");" +"\r\n")
        f.write("\t\t"+ "end\t" + "(0.004 0 "+ z +");" +"\r\n")
        f.write("\t\t"+ "nPoints\t" + str(nPoints) + ";" +"\r\n")
    else:
        print "We've got a problem here !"        
    
def writeStartEnd0(f,z,nPoints):
    f.write("\t\t"+ "type\t" + "uniform;" +"\r\n")
    f.write("\t\t"+ "axis\t" + "distance;" +"\r\n")
    f.write("\t\t"+ "start\t" + "(0. 0 "+ z +");" +"\r\n")
    f.write("\t\t"+ "end\t" + "(0. -0.004 "+ z +");" +"\r\n")
    f.write("\t\t"+ "nPoints\t" + str(nPoints) + ";" +"\r\n")

def writeStartEnd1(f,z,nPoints):
    f.write("\t\t"+ "type\t" + "uniform;" +"\r\n")
    f.write("\t\t"+ "axis\t" + "distance;" +"\r\n")
    f.write("\t\t"+ "start\t" + "(0. 0 "+ z +");" +"\r\n")
    f.write("\t\t"+ "end\t" + "(0. 0.004 "+ z +");" +"\r\n")
    f.write("\t\t"+ "nPoints\t" + str(nPoints) + ";" +"\r\n")
    
def writeStartEnd2(f,z,nPoints):
    f.write("\t\t"+ "type\t" + "uniform;" +"\r\n")
    f.write("\t\t"+ "axis\t" + "distance;" +"\r\n")
    f.write("\t\t"+ "start\t" + "(0 0 "+ z +");" +"\r\n")
    f.write("\t\t"+ "end\t" + "(-0.004 0 "+ z +");" +"\r\n")
    f.write("\t\t"+ "nPoints\t" + str(nPoints) + ";" +"\r\n")

def writeStartEnd3(f,z,nPoints):
    f.write("\t\t"+ "type\t" + "uniform;" +"\r\n")
    f.write("\t\t"+ "axis\t" + "distance;" +"\r\n")
    f.write("\t\t"+ "start\t" + "(0 0 "+ z +");" +"\r\n")
    f.write("\t\t"+ "end\t" + "(0.004 0 "+ z +");" +"\r\n")
    f.write("\t\t"+ "nPoints\t" + str(nPoints) + ";" +"\r\n")

def write_LineSet(f,z_value_List,N,total_nb_of_Line,resolution):
    f.write("sets\r\n")
    f.write("(\r\n")
    writeLines(f,z_value_List,N,total_nb_of_Line,resolution)
    f.write(");\r\n")

def write_sampleLines(fileName,z_value_List,N,total_nb_of_Line,resolution):
    f= open(fileName,"a")
    write_headerSetting_sampleLines(f)
    write_LineSet(f,z_value_List,N,total_nb_of_Line,resolution)
    f.close()
    
def NLines2Dict(Nb_slices_along_z):
    l = np.linspace(0.0052,0.0352,num=Nb_slices_along_z)
    listStr = [str(x) for x in l]
    print "A list of all z positions :\n"
    print listStr
    
    dictName="../../system/sampleDict_lines"
    write_sampleLines(dictName,listStr,Nb_slices_along_z,range(4*Nb_slices_along_z),resolution=200)
    
    os.system('dos2unix '+dictName)

# exactly 40 mesh grid in 0.03m
NLines2Dict(40)