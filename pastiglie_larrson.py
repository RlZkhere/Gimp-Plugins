#!/usr/bin/python2
from gimpfu import *
import os
def schiarisci_foto(cartella):
 percorso=os.getcwd()
 for x in os.listdir(cartella):
  if x.startswith('LR-'):   
   percorso_completo=percorso+"/"+x
   file_output=percorso+"/OUTPUT/"+"1_"+x
   punti=[0,0,85,255,255,255]
   immagine=pdb.gimp_file_load(percorso_completo,percorso_completo)
   immagine_modifica=pdb.gimp_image_get_active_layer(immagine)
   pdb.gimp_drawable_invert(immagine_modifica,False)
   pdb.gimp_curves_spline(immagine_modifica,HISTOGRAM_VALUE,len(punti),punti)
   #pdb.gimp_image_crop(immagine,857,265,174,485) QUESTO RITAGLIA LA FOTO SONO LE COORDINATE DEL RITAGLIO 
   pdb.file_png_save_defaults(immagine,immagine_modifica,file_output,file_output)
   pdb.gimp_image_delete(immagine)
register(
"python-fu-batch-pastiglie-larsson",
"Recupero dati",
"Recupera informazioni dalle foto delle pastiglie",
"Khere",
"Khere",
"03-11-2025",
"",
"",
[
(PF_DIRNAME,"cartella","cartella dove eseguire il comando",None),
],
[],
schiarisci_foto
)
main()
