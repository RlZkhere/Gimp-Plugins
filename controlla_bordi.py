#!/usr/bin/python2
from gimpfu import *
import os
def controlla_bianco(cartella):
 SOGLIA_BIANCO=245
 pwd=os.getcwd()
 print('Quanti pixel controllare:')
 numero_pixel=input()
 print('Inserisci 0 per verticale, 1 per orizzontale')
 scelta=input()
 for foto in os.listdir(pwd):
  errori=int(0)
  if '.jpg' in foto:    
   percorso_file=pwd+'/'+foto
   percorso_output=pwd+'/1_'+foto
   percorso_output_2=pwd+'/2_'+foto
   immagine=pdb.gimp_file_load(percorso_file,percorso_file)
   livello=immagine.active_layer
   altezza=immagine.height
   larghezza=immagine.width
   nuova_larghezza = larghezza - numero_pixel
   nuova_altezza = altezza - numero_pixel
   if scelta == 0:
    pdb.gimp_image_crop(immagine,larghezza,numero_pixel,0,nuova_altezza)  #TAGLIA LA FOTO ESCLUDENDO 0 PIXEL DALL ALTO E (PIXEL TOTALI-TAGLIATI) DAL BASSO --> FOTO ORIZZONTALE 
   else:
    pdb.gimp_image_crop(immagine,numero_pixel,altezza,nuova_larghezza,0) #TAGLIA LA FOTO ESCLUDENDO 0 PIXEL DA DESTRA E (PIXEL TOTALI-TAGLIATI) DA SINISTRA --> FOTO VERTICALE
   livello=immagine.active_layer
   pdb.file_png_save_defaults(immagine,livello,percorso_output,percorso_output) #SALVA LA FOTO DEL BORDO DESTRO CON 1_ DAVANTI AL NOME
   pdb.gimp_image_delete(immagine)
   bordo_destro=pdb.gimp_file_load(percorso_output,percorso_output) #CARICA IL BORDO DESTRO
   livello=bordo_destro.active_layer
   bpp=livello.bpp
   listapixel=livello.get_pixel_rgn(0,0,bordo_destro.width,bordo_destro.height,False,False)
   pixels=[]
   for i in range(bordo_destro.height): #ITERA SU TUTTI I PIXEL DELL ALTEZZA
    for j in range(bordo_destro.width): #ITERA SU TUTTI I PIXEL DELLA LARGHEZZA
     pixel=listapixel[j, i] #PRENDE IL PIXEL DALLA LISTA --> J = x, I = y nell asse cartesiano
     valore_pixel=tuple(ord(c) for c in pixel)
     pixels.append(valore_pixel)
   for pixel in pixels:
    r,g,b=pixel[:3]
    if not (r >= SOGLIA_BIANCO and g >= SOGLIA_BIANCO and b >= SOGLIA_BIANCO): #MINIMO TOLLERABILE E (245,245,245)
     errori=1
     break
   pdb.gimp_image_delete(bordo_destro)
   os.remove(percorso_output)
   if errori == 0: #QUA DEVO RIAPRIRE LA FOTO E RIFARE IL CONTROLLO
    pixels=[]
    immagine=pdb.gimp_file_load(percorso_file,percorso_file)
    if scelta == 1:
     pdb.gimp_image_crop(immagine,numero_pixel,altezza,0,0) #CONTROLLA ORIZZONTALMENTE
    else:
     pdb.gimp_image_crop(immagine,larghezza,numero_pixel,0,0) #CONTROLLA VERTICALMENTE
    livello=immagine.active_layer
    pdb.file_png_save_defaults(immagine,livello,percorso_output_2,percorso_output_2)
    pdb.gimp_image_delete(immagine)
    bordo_sinistro=pdb.gimp_file_load(percorso_output_2,percorso_output_2)
    livello=bordo_sinistro.active_layer
    listapixel=livello.get_pixel_rgn(0,0,bordo_sinistro.width,bordo_sinistro.height,False,False)
    for y in range(bordo_sinistro.height):
     for x in range(bordo_sinistro.width):
      pixel=listapixel[x, y]
      valore_pixel=tuple(ord(c) for c in pixel)
      pixels.append(valore_pixel)
    for pixel in pixels:
     r,g,b=pixel[:3]
     if not (r >= SOGLIA_BIANCO and g >= SOGLIA_BIANCO and b >= SOGLIA_BIANCO):
      errori=1
      break
    pdb.gimp_image_delete(bordo_sinistro)
    os.remove(percorso_output_2)
    if errori == 0:
     f=open('dati.csv','a')
     f.write(foto+';'+str(numero_pixel)+"\n")
     f.close()
register(
"python-fu-batch-controlla-bordo",
"Controlla bianco del bordo",
"Controlla quanti pixel  bianchi ci sono sia laterali che veritcali",
"Khere",
"Khere",
"19-01-2026",
"",
"",
[
(PF_DIRNAME,"cartella","cartella",None)
],
[],
controlla_bianco
)
main()
