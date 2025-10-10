import json


            ### Clubbing all the files into one
data = []
for i in range (0,3000):
    file = f"/project/agsgpa/Achyutan/params_chunk_{i:04}.out"
    with open(file,'r') as f:
       a = json.load(f)
    for i in a:
         data.append(i)

      ###Getting parameter values
p=[]
with open('/home/madhusud/modeling_gene_expression/Screens/three.txt', "r") as f:
    for line in f:
        numbers = [float(num_str) for num_str in line.strip().split(',') if num_str.strip() != '']
        p.extend(numbers)
def sets(p , totalparams): 
   q = []
   a = 0
   b = 32
   for i in range (0,len(p)//totalparams):
    q.append(p[a:b])
    b += 32
    a+=32
   return q
q = sets(p,32)

              #Good for all
indices1=[]
for i in data:
 if any(i[j]is None for j in [0,1,2,3,4,5]):
     continue
 if all(i[j] >=64 for j in [0,1,2,3,5]):
     indices1.append(data.index(i))
print(len(indices1))

# params = []
# #with open('/home/madhusud/modeling_gene_expression/Screens/All_modelA2.txt' ,'w') as f:
#  for i in indices1:
# #     print(data[i]) #50hr values
# #     #print(q[i]) #parameter values
#      params.extend(q[i])
# #     f.write(str(data[i]))
# #    f.write(str("\n"))
# #    f.write("p = " + str(params))
# #    f. write(str("\n"))
# #    f.write("Indices1:" + str(indices1))
# print(params)


#                 #only tetraploid and not present in all 

# indices2=[]
# for i in range(len(data)):
#    if data[i][5] is None or i in indices1:
#       continue
#    elif data[i][5] is not None and data[i][5] >= 67 :
#      indices2.append(i)
# print(len(indices2))

# params = []
# # with open('/home/madhusud/modeling_gene_expression/modelA_%cells/Screeningplots/2nd_screen/Tetraploid_only/Tetraploid_modelA.txt' ,'w') as f:
# # for i in indices2:
# #    print(data[i]) #50hr values
# #    #print(q[i]) #parameter values
#     params.extend(q[i])
# #    f.write(str(data[i]))
# #  f.write(str("\n"))
# #  f.write(str(params))
# #  f. write(str("\n"))
# #  f.write("Indices2:" + str(indices2))
# print(params)
                   #####Only tetrasomy

# indices3 = []
# for i in range(len(data)):
#    if data[i][3] is None or i in indices1:
#       continue
#    elif data[i][3] is not None and data[i][3] >= 92 :
#      indices3.append(i)
# print(len(indices3))

# params = []
# # with open('/home/madhusud/modeling_gene_expression/modelA_%cells/Screeningplots/2nd_screen/Tetrasomy_only/Tetrasomy_modelA.txt' ,'w') as f:
# for i in indices3:
# #    print(data[i]) #50hr values
# #    #print(q[i]) #parameter values
#     params.extend(q[i])
# #    f.write(str(data[i]))
# #  f.write(str("\n"))
# #  f.write(str(params))
# #  f. write(str("\n"))
# #  f.write("Indices3:" + str(indices3))
# print(params)
#                     #####Only trisomy

# indices4 = []
# for i in range(len(data)):
#    if data[i][2] is None or i in indices1:
#       continue
#    elif data[i][2] is not None and data[i][2] >= 94 :
#      indices4.append(i)
# #print(indices4)
# print(len(indices4))

# params = []
# with open('/home/madhusud/modeling_gene_expression/modelA_%cells/Screeningplots/2nd_screen/Trisomy_only/Trisomy_modelA.txt' ,'w') as f:
#   for i in indices4:
#    print(data[i]) #50hr values
#    #print(q[i]) #parameter values
#    params.extend(q[i])
#    f.write(str(data[i]))
#  f.write(str("\n"))
#  f.write(str(params))
#  f. write(str("\n"))
#  f.write("Indices4:" + str(indices4))
#print(params)
#                     ####Only triploid

indices5 = []
for i in range(len(data)):
   if data[i][4][0] is None or data[i][4][1] is None or i in indices1:
      continue
   elif data[i][4][0] >= 47 and data[i][4][1] >= 47 and abs(data[i][4][0] - data[i][4][1]) <= 3  :
     indices5.append(i)
print(len(indices5))

params = []
# with open('/home/madhusud/modeling_gene_expression/modelA_%cells/Screeningplots/2nd_screen/Triploid_only/Triploid_modelA.txt' ,'w') as f:
for i in indices5:
    print(data[i]) #50hr values
#    #print(q[i]) #parameter values
    params.extend(q[i])
#    f.write(str(data[i]))
#  f.write(str("\n"))
#  f.write(str(params))
#  f. write(str("\n"))
#  f.write("Indices5:" + str(indices5))
print(params)
