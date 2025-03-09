# w=write
# a=append
# r=read

mesajlar =[]
for i in range(5):
    mesaj = input(f"{i+1}. Mesaji giriniz: ")
    mesajlar.append(mesaj + "\n")

dosya = open("Mesajlar.txt" , "w")
dosya.writelines(mesajlar)
dosya.close()



# read
dosya = open("Mesajlar.txt" , "r")
print("\n Mesajlariniz: ")
for mesaj in dosya:
    print(mesaj.strip())
dosya.close()


