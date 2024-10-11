input_data = open('input.txt', 'r') 
data = input_data.read()
a = int(data)
c = 1
for i in range( 1 , a + 1):
    c*=i
output_data = open ('output.txt','w') 
output_data.write(str(c))
input_data.close()
output_data.close()