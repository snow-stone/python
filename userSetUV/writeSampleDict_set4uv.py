import numpy as np
import os

def writeStartEnd(whichLineGroup,f,z,nPoints):
    if whichLineGroup == 0:
        f.write("\t\t"+ "type\t"  + "uniform;" +"\r\n")
        f.write("\t\t"+ "axis\t"  + "distance;" +"\r\n")
        f.write("\t\t"+ "start\t" + "("+z+ " 0 0);" +"\r\n")
        f.write("\t\t"+ "end\t" + "("+z+ " -0.004  0);" +"\r\n")
        f.write("\t\t"+ "nPoints\t" + str(nPoints) + ";" +"\r\n")
    elif whichLineGroup == 1:
        f.write("\t\t"+ "type\t"  + "uniform;" +"\r\n")
        f.write("\t\t"+ "axis\t"  + "distance;" +"\r\n")
        f.write("\t\t"+ "start\t" + "("+z+ " 0 0);" +"\r\n")
        f.write("\t\t"+ "end\t" + "("+z+ " 0.004    0);" +"\r\n")
        f.write("\t\t"+ "nPoints\t" + str(nPoints) + ";" +"\r\n")
    else:
        print "big problem"

def writeLines(f,z_value_List,N,Nb_lineGroup,resolution,dictName):
    for i in range(Nb_lineGroup*N):
        whichLineGroup = i // N  # quotient  0, 1 ,2... Nb_lineGroup
        j = i % N                # remainder 0, 1, 2... Ns
        
        f.write("\t"+dictName+'-'+str(i)+"\r\n")
        f.write("\t{\r\n")
        writeStartEnd(whichLineGroup,f,z_value_List[j],resolution)
        f.write("\t}\r\n")
        f.write("\r\n")        
    
def write_LineSet(f,z_value_List,Nb_slices_along_z,Nb_lineGroup,resolution,dictName):
    f.write("sets\r\n")
    f.write("(\r\n")
    writeLines(f,z_value_List,Nb_slices_along_z,Nb_lineGroup,resolution,dictName)
    f.write(");\r\n")

def write_headerSetting_sampleLines(f,fieldName,interpolationScheme):
    f.write("setFormat raw;\r\n")
    f.write("\r\n")
    f.write("interpolationScheme "+interpolationScheme+";\r\n")
    f.write("\r\n")
    f.write("fields\r\n")
    f.write("(\r\n")
    f.write("\t"+fieldName+"\r\n")
    f.write(");\r\n")

def write_sampleLines(dictName,fieldName,interpolationScheme,z_value_List,Nb_lineDisplacement,Nb_lineGroup,resolution):
    f= open(dictName,"w")
    write_headerSetting_sampleLines(f,fieldName,interpolationScheme)
    write_LineSet(f,z_value_List,Nb_lineDisplacement,Nb_lineGroup,resolution,dictName)
    f.close()
    
def NLines2Dict(Nb_lineDisplacement):
    l = np.linspace(-0.08,-0.04,num=Nb_lineDisplacement)
    listStr = [str(x) for x in l]
    print "A list of all line displacements :\n"
    print listStr
    
    dictName="set4uv"
    fieldName="uv"
    interpolationScheme="cell"
    write_sampleLines(dictName,fieldName,interpolationScheme,listStr,Nb_lineDisplacement,2,resolution=80)
    
    os.system('dos2unix '+dictName)
    print "\n"
    print "sampleDict written. Think to add a file header!"

# exactly 40 mesh grid in 0.03m
NLines2Dict(64)
