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
indices=[]
for i in data:
 if any(i[j]is None for j in [0,1,2,3,4,5]):
     continue
 if all(i[j] >=70 for j in [0,1,2,3,5]):
     indices.append(data.index(i))
print(indices)

params = []
with open('/home/madhusud/modeling_gene_expression/Screens/All_modelA.txt' ,'w') as f:
   for i in indices:
    print(data[i]) #50hr values
    #print(q[i]) #parameter values
    params.extend(q[i])
   f.write(str(params))

                #only tetraploid and not present in all 
indices1 = indices
indices=[]
for i in range(len(data)):
   if data[i][5] is None or i in indices1:
      continue
   elif data[i][5] is not None and data[i][5] >= 70 :
     indices.append(i)
print(indices)
params = []
with open('/home/madhusud/modeling_gene_expression/Screens/Tetraploid_modelA.txt' ,'w') as f:
 for i in indices:
   print(data[i]) #50hr values
   #print(q[i]) #parameter values
   params.extend(q[i])
 f.write(str(params))




