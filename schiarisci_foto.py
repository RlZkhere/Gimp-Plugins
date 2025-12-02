#!/usr/bin/python2
from gimpfu import *
import os
def schiarisci(cartella):
 lista_file = [f for f in os.listdir(cartella) if f.startswith("LR-")]   
 for x in lista_file:
  percorso_foto=os.path.join(cartella,x)
  file_output = os.path.join(cartella, "OUTPUT/" + os.path.splitext(x)[0] + ".jpg")
  print(file_output)
  immagine=pdb.gimp_file_load(percorso_foto,percorso_foto)
  layer=pdb.gimp_image_get_active_layer(immagine)
  punti=[0,0,240,255,255,255]
  pdb.gimp_curves_spline(layer,HISTOGRAM_VALUE,len(punti),punti)
  pdb.file_png_save_defaults(immagine,layer,file_output,file_output)
  pdb.gimp_image_delete(immagine)
register(
 "python-fu-batch-schiarisci-foto",
 "Batch schiarisci foto larsson",
 "Script che schiarisce le foto di larsson dopo aver tolto il logo",
 "Khere",
 "Khere",
 "2025",
 "",
 "",
 [
  (PF_DIRNAME, "cartella", "Cartella con file LR-*", None),
 ],
 [],
 schiarisci
)
main()
