import numpy as nmp

inputfile = open("input.txt")
outputfile = open("output.txt","w")
s=int(inputfile.readline()) #grid size s
n=int(inputfile.readline()) #number of cars n
o=int(inputfile.readline()) #number of obstacles
genRewardFun=nmp.zeros((s,s), dtype=nmp.float64)
policy=nmp.zeros((s,s), dtype=nmp.int)
genRewardFun.fill(-1)
for q in range(o): #obstacle locations
        x=inputfile.readline()
        sepline=x.split(",")
        sepline[1]=sepline[1].rstrip()
        i=int(sepline[1])
        j=int(sepline[0])
        genRewardFun[i][j]=-101

startDict={}
for q in range(n): #start locations
        x=inputfile.readline()
        sepline=x.split(",")
        sepline[1]=sepline[1].rstrip()
        i=int(sepline[1])
        j=int(sepline[0])
        startDict[q]=(i,j)


endDict={}
for q in range(n): #end locations
        x=inputfile.readline()
        sepline=x.split(",")
        sepline[1]=sepline[1].rstrip()
        i=int(sepline[1])
        j=int(sepline[0])
        endDict[q]=(i,j)

#for each car
for car in range(n):
        currRewardFunction=genRewardFun.copy()
        start_i=startDict[car][0]
        start_j=startDict[car][1]
        end_i=endDict[car][0]
        end_j=endDict[car][1]
        currRewardFunction[end_i][end_j]=99
        currValFunction=currRewardFunction.copy()
        policy.fill(0)
        policy[end_i][end_j]=99
        while True:
                currValFunction1=currValFunction.copy()
                dif=0
                for i in range(s):
                        for j in range(s):
                                if not (i==end_i and j==end_j):
                                        if j-1>=0:
                                                valW=currValFunction1[i][j-1]
                                        else:
                                                valW=currValFunction1[i][j]
                                        if j+1<s:
                                                valE=currValFunction1[i][j+1]
                                        else:
                                                valE=currValFunction1[i][j]
                                        if i-1>=0:
                                                valN=currValFunction1[i-1][j]
                                        else:
                                                valN=currValFunction1[i][j]
                                        if i+1<s:
                                                valS=currValFunction1[i+1][j]
                                        else:
                                                valS=currValFunction1[i][j]
                                        
                                        north=(0.7*valN)+(0.1*valS)+(0.1*valW)+(0.1*valE)
                                        south=(0.1*valN)+(0.7*valS)+(0.1*valW)+(0.1*valE)
                                        west=(0.1*valN)+(0.1*valS)+(0.7*valW)+(0.1*valE)
                                        east=(0.1*valN)+(0.1*valS)+(0.1*valW)+(0.7*valE)
                                        currValFunction[i][j]=currRewardFunction[i][j]+0.9*(max(north,south,west,east))
                                        dif=max(dif, abs(currValFunction1[i][j]-currValFunction[i][j]))
                if dif<0.1*0.1/0.9:
                        break

        for i in range(s):
                for j in range(s):
                        if not (i==end_i and j==end_j):
                                if j-1>=0:
                                        valW=currValFunction1[i][j-1]
                                else:
                                        valW=currValFunction1[i][j]
                                if j+1<s:
                                        valE=currValFunction1[i][j+1]
                                else:
                                        valE=currValFunction1[i][j]
                                if i-1>=0:
                                        valN=currValFunction1[i-1][j]
                                else:
                                        valN=currValFunction1[i][j]
                                if i+1<s:
                                        valS=currValFunction1[i+1][j]
                                else:
                                        valS=currValFunction1[i][j]
                                north=(0.7*valN)+(0.1*valS)+(0.1*valW)+(0.1*valE)
                                south=(0.1*valN)+(0.7*valS)+(0.1*valW)+(0.1*valE)
                                west=(0.1*valN)+(0.1*valS)+(0.7*valW)+(0.1*valE)
                                east=(0.1*valN)+(0.1*valS)+(0.1*valW)+(0.7*valE)
                                action=1
                                best=north
                                if best<south:
                                        best=south
                                        action=3
                                if best<east:
                                        best=east
                                        action=2
                                if best<west:
                                        best=west
                                        action=4
                                policy[i][j]=action
                        
                        
        #2-simulate for each car
        totalscore=0
        for seed in range(10):
                curr_i=start_i
                curr_j=start_j
                nmp.random.seed(seed)
                swerve=nmp.random.random_sample(1000000)
                k=0
                counter=0
                while not (curr_i==end_i and curr_j==end_j):
                        move=policy[curr_i][curr_j]
                        if swerve[k]>0.7:
                                if swerve[k]>0.8:
                                        if swerve[k]>0.9:
                                                move=move+2
                                        else:
                                                move=move+1
                                else:
                                        move=move+3
                        k=k+1
                        if move>4:
                                move=move%4
                        if move==1:
                                curr_i=curr_i-1
                        elif move==2:
                                curr_j=curr_j+1
                        elif move==3:
                                curr_i=curr_i+1
                        else:
                                curr_j=curr_j-1
                        if curr_i<0:
                                curr_i+=1
                                totalscore-=1
                        elif curr_i>=s:
                                curr_i-=1
                                totalscore-=1
                        elif curr_j<0:
                                curr_j+=1
                                totalscore-=1
                        elif curr_j>=s:
                                curr_j-=1
                                totalscore-=1
                        else:
                                totalscore+=currRewardFunction[curr_i][curr_j]

                
        total=int(nmp.floor(totalscore/10))
        outputfile.write(str(total)+"\n")
        
outputfile.close()
