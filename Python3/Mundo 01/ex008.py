#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
medida = float(input('Uma distância em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print ('Quilômetro {:.3f} Km \nHectômetro {:.2f} Hm \nDecâmetro {:.1f} Dam \nDecímetro {:.0f} Dm \nCentrímetro {:.0f} Cm\nMilímetro {:.0f} Mm'. format(km, hm, dam, dm, cm, mm))