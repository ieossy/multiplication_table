def for_loop_multiplication_table(m, last_number):
    #k = 1

    for z in range(1, last_number+1):
        product = m * z
        print('{} * {} = {}'.format(m, z, product))
        
last_number = int(input('Please enter the last number you wish to multiple: '))
m = int(input('Please enter the number you wish to multiple with: '))
for_loop_multiplication_table(m, last_number)
        
