input_data = open('input.txt', 'r') 
data = input_data.read()
l = list()
a = int(data)
c = 1
for i in range( 1 , a + 1):
    c*=i
    l.append(c)
output_data = open ('output.txt','w') 
output_data.write(str(l))
input_data.close()
output_data.close()