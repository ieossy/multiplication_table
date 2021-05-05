def multiplication_table(z, y):
    x = 1 # initializing the variable "x"
    while x <= y: #condition to check
        prod = x * z # operation to do
        print('{} * {} = {}' .format(z, x, prod))
        x += 1 # variable increment
        
z = int(input('please enter a number: '))
y = int(input('please enter the last number to multiple with: '))

multiplication_table(z, y)
    
