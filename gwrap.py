inp_str ='aabbccdfg'
out_str =""
count =1

for i in range(len(inp_str)):
    if i<len(inp_str)-1 and inp_str[i]==inp_str[i+1]:
        count +=1
    else:
        out_str += str(count) + inp_str[i]
        count =1
print(out_str)