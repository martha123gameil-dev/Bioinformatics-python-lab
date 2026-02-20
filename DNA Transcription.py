DNA="ATTCGGAATCCGTAAG"
# convert DNA sequnce into RNA
RNA= DNA.replace("T","U")
length= len(RNA)
print(f"RNA sequence is {RNA} and its length is {length}")
