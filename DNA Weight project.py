a= "ATCGTAGCGGATTG"
# calculate the number of each base
no_of_G= a.count("G")
no_of_C= a.count("C")
no_of_A= a.count("A")
no_of_T= a.count("T")
# calculate the weight of each base
weight_of_G= no_of_G*329.2
weight_of_C= no_of_C*289.2
weight_of_A= no_of_A*313.2
weight_of_T= no_of_T*304.2
# calculate total weight
total_weight= weight_of_A + weight_of_C + weight_of_G + weight_of_T
print (f"total weight of DNA sequence is {total_weight}")

