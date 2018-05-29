Alphabet={}
Alphabet["A"] = ["EDE","DFD","CCBCC","BCDCB","BCDCB","BJB","BJB","BCDCB","BCDCB","BCDCB","BCDCB"]
Alphabet["B"] = ["BIC" , "BCCDB" , "BCDCB" , "BCDCB" , "BCCDB" , "BIC" , "BCCDB" , "BCDCB" , "BCDCB" , "BCCDB" , "BIC"]
Alphabet["C"] = ["DGC" , "CIB" , "BJB" , "BCI" , "BBJ" , "BBJ" , "BBJ" , "BCI" , "BJB" , "CIB" , "DGC"]
Alphabet["D"] = ["BHD" , "BIC" , "BCDCB" , "BCDCB" , "BCDCB" , "BCDCB" , "BCDCB" , "BCDCB" , "BCDCB", "BIC" , "BHD"]
Alphabet["E"] = ["CIB" , "BJB" , "BCEBB" , "BCI" , "BHD" , "BHD" , "BCI" , "BCI" , "BCEBB" , "BJB" , "CIB" ]
Alphabet["F"] = ["CHC" , "BJB" , "BCEBB" , "BCI" , "BCI" , "BIC" , "BIC" , "BCI" , "BCI" , "BCI" , "BCI"]
Alphabet["G"] = ["DGC" , "CIB" , "BJB" , "BCI" , "BBJ" , "BBBFB" , "BBBBBBB" , "BCEBB" , "BJB" , "CIB" , "DGC"]
Alphabet["H"] = ["CBDBC" , "BCDCB","BCDCB" , "BCDCB" , "BCDCB" , "BJB" , "BJB" , "BCDCB" , "BCDCB","BCDCB" , "BCDCB" ]
Alphabet["I"] = ["CHC" , "BJB" , "BABCCAB" , "ECF", "ECF", "ECF" , "ECF" , "ECF" , "BABCCAB" , "BJB" , "CHC"]
Alphabet["J"] = ["CHC" , "BJB" , "BACCBAB" , "FCE" , "FCE" , "FCE" , "BBBCE" , "BBBCE" , "BGE" , "BGE" , "CEF"]
Alphabet["K"] = ["BCCDB" , "BCBDC" , "BCACE" , "BFF" , "BEG" , "BDH" , "BEG" , "BFF" , "BCACE" , "BCBDC" , "BCCDB" ]
Alphabet["L"] = ["BCI" , "BCI" , "BCI" , "BCI" , "BCI" , "BCI" , "BCI" , "BCDCB" , "BJB" , "BJB" , "CHC"]
Alphabet["M"] = ["BBFBB" , "BCDCB" , "BDBDB" , "BJB" , "BJB" , "BBADABB" , "BBBBBBB" , "BBFBB" , "BBFBB" , "BBFBB" , "BBFBB"]
Alphabet["N"] = ["BBFBB" , "BCEBB" , "BDDBB" , "BECBB" , "BBACBBB" , "BBBCABB" , "BBCEB" , "BBDDB" , "BBECB" , "BBFBB","BBFBB"]
Alphabet["O"] = ["DFD" , "CHC" , "BJB" , "BCDCB" , "BBFBB" , "BBFBB" , "BBFBB" , "BCDCB" , "BJB" , "CHC" , "DFD"]
Alphabet["P"] = ["BIC" , "BJB" , "BCDCB" ,"BCDCB","BCDCB" , "BJB" , "BIC" , "BCI" ,"BCI" ,"BCI" , "BCI" ] 
Alphabet["Q"] = ["DFD" , "CHC" , "BJB" , "BCDCB" , "BBFBB" , "BBBBBBB" , "BBBCABB" , "BCBBABB" , "BIC" , "CFABB" , "DDBBB"]  
Alphabet["R"] = ["BIC" , "BJB" , "BCDCB" , "BCDCB" , "BCDCB" , "BJB" , "BIC" , "BGE" , "BCADD", "BCBDC" , "BCCDB"]
Alphabet["S"] = ["CHC" ,"BJB" , "BBFBB" , "BBJ" , "BBJ" , "CHC" , "DHB" , "JBB" , "BBFBB" , "BJB" , "CHC"]
Alphabet["T"] = ["CHC" , "BJB" , "BJB" , "BABCCAB" , "ECF" , "ECF", "ECF", "ECF", "ECF", "ECF", "ECF" ]
Alphabet["U"] = ["BBFBB" , "BBFBB", "BBFBB", "BBFBB", "BBFBB", "BBFBB", "BBFBB" , "BCDCB" , "BJB" , "CHC" , "DFD"]
Alphabet["V"] = ["BBFBB" , "BBFBB", "BBFBB", "BBFBB", "BBFBB", "BBFBB" , "BCDCB" , "CCBCC" , "DFD" , "EDE" , "FBF" ]
Alphabet["W"] = ["BBFBB" , "BBFBB", "BBFBB", "BBFBB", "BBFBB", "BBFBB" , "BBBBBBB" , "BBADABB" , "BJB" , "BDBDB" , "BCDCB"]
Alphabet["X"] = ["BCDCB" , "BCDCB" , "CCBCC" , "DFD" , "EDE" , "FBF" , "EDE" , "DFD" , "CCBCC" , "BCDCB" , "BCDCB"]
Alphabet["Y"] = ["BCDCB" , "BCDCB" , "CCBCC" , "DFD" , "EDE" , "FBF" , "FBF" , "FBF", "FBF", "FBF" , "EDE"]
Alphabet["Z"] = ["BJB" , "BJB" , "BBDCC" , "GCD" , "FCE" , "ECF" , "DCG" , "CCH" , "BCEBB" , "BJB" , "BJB"]

def printname(s):
    b=[]
    s = s.upper()
    for i in range(11):
    	line = ""
    	for j in s:
    		if j == ' ':
    			line += "*"
    		if j not in Alphabet:
    		    continue;
    		else:
    			line += Alphabet[j][i] + " "
    	b.append(line)
    def solve(arr):
    	for s in arr:
    		st=""
    		c=0
    		for i in s:
    			if i == "*":
    				st += 8 * " "
    				continue;
    			if(i==' '):
    			   c=0
    			   continue;
    			c+=1
    			if c%2 == 0:
    			   ch='s'
    			   st+=ch*(ord(i)-64)
    			else:
    			   st=st+ ' '*(ord(i)-64)
    		print(st)
    solve(b)

while True:
  try:
    str1 = input()
    if str1=="#":
        break;
    print()
    printname(str1)
   
  except (EOFError):
    break;
