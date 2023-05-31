Close = False
while not Close:
    Exit = input("Hej och välkomen! \nVill du veta något om Fria Karlstad? (Ja/Nej) ")
    if Exit == 'Nej':
        Close = True   

    else:
        Question = input("Vad vill du veta? ")
        haystack = 'Mat,Lärare,Sjuk'

        if haystack.find(Question) >= 0:
            print(' Vad om ' + Question +' vill du veta?')
        
            if Question == "Mat":
                print("1. Vill du veta vad det blir för mat? Tryck 1. \n")
                print("2. Vill du veta vad vilka matpersonlaen är? Tryck 2 \n")
                print("3. Vill du ge dagens mat ett omdömme? Tryck 3 \n")
            
                Mat_altA = int(input("Ange alternativ "))

                if Mat_altA == 1:
                    print("Dagens mat blir Köttbullar och makaroner. \n Tryck 1 för starta om 2 för avbryt")
            else:
                print('Jag förståd inte ditt svar')
        
      
            
    if Question == 'Nej' :
        Close = True