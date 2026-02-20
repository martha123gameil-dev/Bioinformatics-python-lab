DNA=input("please enter your DNA sequence in capital")
# convert DNA to RNA
RNA=DNA.replace("T","U")
print("RNA Sequence is",(RNA))
# calculate C-G content
G_cotent= RNA.count("G")
C_content= RNA.count("C")
total_length= len(RNA)
C_G_pecentage= ((G_cotent+C_content)/total_length)*100
print("C_G_pecentage",C_G_pecentage)
# calculate purines
A_content= RNA.count("A")
purines= A_content+G_cotent
print("purines(A+G) IS",purines)
