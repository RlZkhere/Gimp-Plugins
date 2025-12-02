#!/usr/bin/python2
from gimpfu import *
import os
def taglia_foto(cartella):
 percorso=os.getcwd()
 print('Di quanti pixel tagliare?')
 pixel_taglia=input()
 for x in os.listdir(cartella):
  if ".png" in x or ".jpg" in x:   
   percorso_completo=percorso+"/"+x
   percorso_output=percorso+"/OUTPUT/"+x
   immagine=pdb.gimp_file_load(percorso_completo,percorso_completo)
   larghezza=immagine.width
   altezza=immagine.height
   nuova_larghezza=larghezza - pixel_taglia
   nuova_altezza=altezza - 100
   pdb.gimp_image_crop(immagine,nuova_larghezza,nuova_altezza,(pixel_taglia/2),50)
   livello = pdb.gimp_image_get_active_layer(immagine)
   pdb.file_png_save_defaults(immagine,livello,percorso_output,percorso_output)
   pdb.gimp_image_delete(immagine)
register(
"python-fu-batch-taglia-foto",
"Taglia x pixel da tutti i lati",
"Taglia i pixel mandati in imput dai lati della foto",
"Khere",
"Khere",
"02-12-2025",
"",
"",
[
(PF_DIRNAME,"cartella","cartella con foto",None)
],
[],
taglia_foto
)
main()
