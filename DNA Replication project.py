a="ATTCGGAATCCGTAAG"
rep_A= a.replace("A","t")
rep_T= rep_A.replace("T","a")
rep_G= rep_T.replace("G","c")
rep_C= rep_G.replace("C","g")
print(rep_C.upper())