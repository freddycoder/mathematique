class Main:
  def menu():
    # Demarrage du programme
    run = True

    # Titre
    print("Calculateur d'incertitude version 0.1")
    
    while run == True:
      #Génération du menu
      print()
      print("|--------- Menu ---------|")
      print("|Erreur absolue      : 0 |")
      print("|Erreur relative     : 1 |")
      print("|a + b               : 2 |")
      print("|a - b               : 3 |")
      print("|ka                  : 4 |")
      print("|ab                  : 5 |")
      print("|a/b                 : 6 |")
      print("|a^n                 : 7 |")      
      print("|Votre choix         : ", end="")
      choice = -2
      while choice < -1 or 7 < choice:
        try:
          choice = float(input())
          if choice == -1:
            run = False
          elif choice < 0 or 7 < choice:
            print("Entrer un nombre valide. -1 pour quitté")
          else:
            print("Entrer un nombre valide. -1 pour quitté")
        except:
          print("Entrer un nombre valide. -1 pour quitté")

      # Faire la bonne action selon le choix de l'utilisateur
      # Erreur absolue
      if choice == 0:
        print("Calcule de l'erreur absolue.")
        valeur_reel = float(input("Entrer la valeur exacte : "))
        valeur_approcher = float(input("Entrer la valeur approcher : "))
        print(Incertitude.erreur_absolue(valeur_approcher, valeur_reel))

      # Erreur relative
      elif choice == 1:
        print("Calcule de l'erreur relative.")
        valeur_reel = float(input("Entrer la valeur exacte : "))
        valeur_approcher = float(input("Entrer la valeur approcher : "))
        print(Incertitude.erreur_relative(valeur_approcher, valeur_reel))
    
      # a + b
      elif choice == 2:
        print("a + b")
        valeur_approcher_a = float(input("Entrer la valeur approcher de a : "))
        incertitude_a = float(input("Entrer la valeur de l'incertitude de a :"))
        valeur_approcher_b = float(input("Entrer la valeur approcher de b : "))
        incertitude_b = float(input("Entrer la valeur de l'incertitude de b :"))
        print(Incertitude.a_plus_b(valeur_approcher_a, incertitude_a, valeur_approcher_b, incertitude_b))
    
      # a - b
      elif choice == 3:
        print("a - b")
        valeur_approcher_a = float(input("Entrer la valeur approcher de a : "))
        incertitude_a = float(input("Entrer la valeur de l'incertitude de a :"))
        valeur_approcher_b = float(input("Entrer la valeur approcher de b : "))
        incertitude_b = float(input("Entrer la valeur de l'incertitude de b :"))
        print(Incertitude.a_moins_b(valeur_approcher_a, incertitude_a, valeur_approcher_b, incertitude_b))
  
      # ka
      elif choice == 4:
        print("ka")
        valeur_approcher = float(input("Entrer la valeur approcher de a : "))
        incertitude = float(input("Entrer la valeur de l'incertitude de a :"))
        print(Incertitude.constance_a(valeur_approcher, incertitude))
    
      # ab
      elif choice == 5:
        print("ab")
        valeur_approcher_a = float(input("Entrer la valeur approcher de a : "))
        incertitude_a = float(input("Entrer la valeur de l'incertitude de a :"))
        valeur_approcher_b = float(input("Entrer la valeur approcher de b : "))
        incertitude_b = float(input("Entrer la valeur de l'incertitude de b :"))
        print(Incertitude.a_fois_b(valeur_approcher_a, incertitude_a, valeur_approcher_b, incertitude_b))
        
      # a/b
      elif choice == 6:
        print("a/b")
        valeur_approcher_a = float(input("Entrer la valeur approcher de a : "))
        incertitude_a = float(input("Entrer la valeur de l'incertitude de a :"))
        valeur_approcher_b = float(input("Entrer la valeur approcher de b : "))
        incertitude_b = float(input("Entrer la valeur de l'incertitude de b :"))  
        print(Incertitude.a_diviser_par_b(valeur_approcher_a, incertitude_a, valeur_approcher_b, incertitude_b))
    
      # a^n
      elif choice == 7:
        print("a^n")
        valeur_approcher_a = float(input("Entrer la valeur approcher de a : "))
        incertitude_a = float(input("Entrer la valeur de l'incertitude de a :"))
        puissance = float(input("Entrer la puissance :"))
        print(Incertitude.a_power_n(valeur_approcher_a, incertitude_a, puissance))
    
      elif choice == -1:
        print("Merci d'avoir utilisé le calculateur d'erreur! ")
        run = False

      else:
        print("Something dosen't work well... ")

class Incertitude:
  def erreur_absolue(valeur_approcher, valeur_reel):
    erreur_absolue = abs(valeur_approcher - valeur_reel)
    return erreur_absolue
      
  def erreur_relative(valeur_approcher, valeur_reel):
    erreur_relative = (abs(valeur_approcher - valeur_reel) / abs(valeur_reel))*100
    return erreur_relative

  def a_plus_b(valeur_approcher_a, incertitude_a, valeur_approcher_b, incertitude_b):
    delta = valeur_approcher_a + valeur_approcher_b
    incertitude = incertitude_a + incertitude_b
    return delta, incertitude

  def a_moins_b(valeur_approcher_a, incertitude_a, valeur_approcher_b, incertitude_b):
    delta = valeur_approcher_a - valeur_approcher_b
    incertitude = incertitude_a + incertitude_b
    return delta, incertitude

  def constance_a(valeur_approcher, incertitude):
    delta = valeur_approcher
    return delta, incertitude

  def a_fois_b(valeur_approcher_a, incertitude_a, valeur_approcher_b, incertitude_b):
    delta = valeur_approcher_a * valeur_approcher_b
    incertitude = (valeur_approcher_a * incertitude_b) + (valeur_approcher_b * incertitude_a)
    return delta, incertitude

  def a_diviser_par_b(valeur_approcher_a, incertitude_a, valeur_approcher_b, incertitude_b):
    delta = valeur_approcher_a / valeur_approcher_b
    incertitude = ((valeur_approcher_a * incertitude_b + valeur_approcher_b * incertitude_a) / valeur_approcher_b**2 )
    return delta, incertitude

  def a_power_n(valeur_approcher_a, incertitude_a, puissance):
    delta = valeur_approcher_a ** puissance
    incertitude = puissance * ((valeur_approcher_a)**(puissance-1)) * incertitude_a
    return delta, incertitude

