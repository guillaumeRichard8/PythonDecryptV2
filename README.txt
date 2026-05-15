####################################################################################################
#                                                                                                  #
#                                                                                                  #
# Solution logicielle de cryptanalyse des messages chiffrés par la méthode du carré de Vigenère :  #
# ===============================================================================================  #
#                                                                                                  #
####################################################################################################


	A) Method for deciphering long messages :

		1) Utiliser le script Python distance_trigrammes.py sur le message pour chercher à trouver la longueur

		   de la clé de chiffrement. (Voir documentation sur "Carré de Vigenère" et "Test de Kasisky").

		   -> nécessite de mettre un seuil de détection aux trigrammes qui se répètent : count > 10 et count > 13
			  et à ajuster si besoin.

		py distance_trigrammes.py


		2) Tester le script Python split.py avec la longueur de clé supposé (ajuster ncol pour cela).

		py split.py


	B) Scripts :
		
		- analyse_frequence.py
		
		- distance_trigrammes.py
		
		- filtrage.py
		
		- README.txt
		
		- split.py
		
		- vigenere.py

	
	C) Pistes d'améliorations :

- seuils de distance_trigrammes.


