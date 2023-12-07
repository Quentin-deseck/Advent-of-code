with open("input.txt",'r') as file:
    #lire les lignes du fichier
        lines = file.readlines()
        
#initialiser la somme total
total_sum=0

#parcourir chaque ligne et extraire le premier et dernier chiffre pour en faire une somme 
for line in lines:
    #1er chiffre 
    first_digit = next((char for char in line if char.isdigit()), None)
    #dernier chiffre
    last_digit = next((char for char in reversed(line) if char.isdigit()),None )
    
    combined_digit = int(first_digit + last_digit if first_digit and last_digit else first_digit * 2)
    #si les deux chiffres sont trouvé les ajoutés à la somme 
    
    
        
        
    total_sum += combined_digit
        
#afficher le resultat 

print("somme totales des premiers et dernier chiffre de chaque ligne est de : ",total_sum)