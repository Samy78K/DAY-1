#COMPTER JUSQU'A 10 !

# for compter in range(1, 11):
#     print("Numero", compter)


#Table de Multiplication !

# n = int(input("Entre un nombre"))
# print("La table de Multiplication :")
# for i in range (1,11):
#     print(i, "x", n, "=", i*n)  


#Accumulateur !

# n = int(input("Entre un nombre: "))
# accumulateur = 0
# for i in range(1, n+1):
#     accumulateur += i 
#     print("l'accumulateur = ", accumulateur)



#Trouver le bon nombre !

# import random

# nombreMagique = random.randint(1, 10)
# for i in range (0,4):
#     nombreEntre = int(input("Devine le nombre magique:"))
#     if nombreEntre > nombreMagique:
#         print("t'es nul essaye encore")
#         print("essai#", i+1)
#     if nombreEntre < nombreMagique:
#         print("t'es nul essaye encore")
#         print("essai#", i+1)
#     if nombreEntre == nombreMagique:
#         print("Bravo vous l'avez trouver", nombreMagique)
#         print("essai#", i+1)
#         break
#     elif i==3:
#         print(" pas gagner dsl je te donnerai pas le nombre magique")

        
        


        #Trouver le plus grand nombre !

# li = [10, 4, 7, 12, 5]
# ma=li[0]
# for i in range(0,len(li)):
#  if li[i]>ma:
#     ma=li[i]
#     print(ma)




#Affiche directment le resultat de la multiplication !


# def multiplier(a, b):
#  return a * b 

# resultat = multiplier(6 , 4)
# print(f"le resultat de la multiplication est {resultat}")

   
    
 
#Afficher lequel des deux nombre et le plus grand !

# max_deux_nombres = [15, 18]
# ma=max_deux_nombres[0]
# for i in range(0, len(max_deux_nombres)):
#     if max_deux_nombres[i]>ma:
#         ma=max_deux_nombres[i]
#         print("le plus grand est : ",ma)







#Calculer la moyenne !

# notes = [2, 16, 10, 8, 14]
# a = 5 
# for i in (notes) :
#     a=a+i
#     a=a/len(notes)
#     print("la moyenne est de : ",a)


# calculer une moyenne !

# def cal_average(num):
#     sum_num = 0
#     for t in num:
#         sum_num = sum_num + t           
#     avg = sum_num / len(num)
#     return avg
# print("The average is", cal_average([18,25,3,41,5]))





#Calculatrice !


# def addition(x,y) :
#     return x + y

# def  soustraction(x,y):
#     return x - y

# def multiplication(x,y):
#     return x * y

# def division(x,y):
#     return x / y

# print("""Choix option \n
# 1- Addition \n
# 2- Soustraction \n
# 3- Multiplication \n
# 4- Division \n""")

# while True :
    
#     choix = input("Entrer votre choix (1,2,3,4) :")
    
#     if choix in ('1', '2', '3', '4'):

#         num1 = float(input("Entrer votre premier nombre :"))
#         num2 =float(input("Entrer votre deuxieme nombre :"))

#         if choix == '1' :
#             print(num1, "+" ,num2, "=" ,addition(num1, num2))

#         if choix == '2' :
#             print(num1, "-" ,num2, "=" ,soustraction(num1, num2))    
        
#         if choix == '3' :
#             print(num1, "*" ,num2, "=" ,multiplication(num1, num2))    
        
#         if choix == '4' :
#             print(num1, "/" ,num2, "=" ,division(num1, num2))   



# Compter_pairs ( pas eu le temps de corriger ) !


# def compter_pairs(listes):
#     res = 0
#     for i in listes:
#         if i%2 == 0:
#             res += 1
#             return res

#             nombre = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#             print("nombre de valeur pair sont {compter_pairs(nombre)}")


