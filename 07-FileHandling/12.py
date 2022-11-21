n_product = input('Add new  products:')

file = open (' shopping.txt', "a")

file.write(n_product)
file.write("\n")

file.close