
class erreur:
  def calcule_incertitude(valeur_approcher, valeur_reel):
    erreur_absolue = abs(valeur_approcher - valeur_reel)
    erreur_relative = (valeur_approcher - valeur_reel) / abs(valeur_reel)

    print("L'erreur absolue est plus ou moins " + str(erreur_absolue))
    print("L'erreur relative est " + str(erreur_relative) + "%")

class propriete_incertitude:
  def a_plus_b(valeur_approcher_a, incertitude_a, valeur_approcher_b, incertitude_b):
    somme_a_b_max = valeur_approcher_a + valeur_approcher_b + (incertitude_a + incertitude_b)
    somme_a_b_min = valeur_approcher_a + valeur_approcher_b - (incertitude_a - incertitude_b)
    print("max est : ", somme_a_b_max, "min est", somme_a_b_min)

  def a_moins_b(valeur_approcher_a, incertitude_a, valeur_approcher_b, incertitude_b):
    difference_a_b_max = valeur_approcher_a - valeur_approcher_b + (incertitude_a - incertitude_b)
    difference_a_b_min = valeur_approcher_a - valeur_approcher_b - (incertitude_a - incertitude_b)
    print("max est : ", difference_a_b_max, "min est", difference_a_b_min)

  def constance_a(valeur_approcher, incertitude):
    print("Est-ce vraiment utile de trouver le taux d'erreur d'une constante?")

  def a_fois_b(valeur_approcher_a, incertitude_a, valeur_approcher_b, incertitude_b):
    ab_max = valeur_approcher_a * valeur_approcher_b + (valeur_approcher_a * incertitude_b + valeur_approcher_b * incertitude_a)
    ab_min = valeur_approcher_a * valeur_approcher_b - (valeur_approcher_a * incertitude_b + valeur_approcher_b * incertitude_b)
    print("max est : ", ab_max, "min est", ab_min)

  def a_diviser_par_b(valeur_approcher_a, incertitude_a, valeur_approcher_b, incertitude_b):
    a_sur_b_max = valeur_approcher_a / valeur_approcher_b + ((valeur_approcher_a * incertitude_b + valeur_approcher_b * incertitude_a) / valeur_approcher_b**2 )
    a_sur_b_min = valeur_approcher_a / valeur_approcher_b - ((valeur_approcher_a * incertitude_b + valeur_approcher_b * incertitude_a) / valeur_approcher_b**2 )
    print("max est : ", a_sur_b_max, "min est", a_sur_b_min)

  def a_power_n(valeur_approcher_a, incertitude_a, puissance):
    a_power_n_max = (valeur_approcher_a) ** puissance + puissance * (valeur_approcher_a)**puissance-1 * incertitude_a
    a_power_n_min = (valeur_approcher_a) ** puissance - puissance * (valeur_approcher_a)**puissance-1 * incertitude_a
    print("max est : ", a_power_n_max, "min est", a_power_n_min)

print("\n")
print("Calculer l'incertitude")
erreur.calcule_incertitude(5000, 5300)
print("\n")
print("a + b")
propriete_incertitude.a_plus_b(500, 40, 400, 35)
print("\n")
print("a - b")
propriete_incertitude.a_moins_b(500, 40, 400, 35)
print("\n")
print("ka")
propriete_incertitude.constance_a(15, 15)
print("\n")
print("ab")
propriete_incertitude.a_fois_b(20, 2, 35, 3)
print("\n")
print("a/b")
propriete_incertitude.a_diviser_par_b(100, 20, 10, 5)
print("\n")
print("a^n")
propriete_incertitude.a_power_n(25, 3, 3)
print("\n")