#!/usr/bin/python2
from gimpfu import *
import os
def sdoppia(cartella):
 listafile=os.listdir(cartella)
 for file in listafile:
  if '.jpg' in file:
   percorso_cartella=os.getcwd()
   percorso_file=percorso_cartella+'/'+file
   percorso_temporaneo=percorso_cartella+'/1_'+file
   percorso_output=percorso_cartella+'/OUTPUT/'+file
   immagine=pdb.gimp_file_load(percorso_file,percorso_file)
   livello=pdb.gimp_image_get_active_layer(immagine)
   pdb.gimp_item_transform_flip_simple(livello, ORIENTATION_HORIZONTAL, True, 0)
   livello=pdb.gimp_image_get_active_layer(immagine)
   pdb.file_png_save_defaults(immagine,livello,percorso_temporaneo,percorso_temporaneo)
   pdb.gimp_image_delete(immagine)
   immagine_1=pdb.gimp_file_load(percorso_file,percorso_file) #IMMAGINE ORIGINALE
   immagine_2=pdb.gimp_file_load(percorso_temporaneo,percorso_temporaneo) #IMMAGINE TEMPORANEA
   sfondo=pdb.gimp_image_new(2400,2400,RGB_IMAGE) #CREA IMMAGINE CHE CONTERRA LO SFONDO BIANCO
   livello_sfondo=pdb.gimp_layer_new(sfondo,2400,2400,RGB_IMAGE,"Sfondo",100,NORMAL_MODE) #LIVELLO DA USARE NELLO SFONDO
   pdb.gimp_image_add_layer(sfondo,livello_sfondo,0) #AGGIUNGE IL LIVELLO ALLO SFONDO
   pdb.gimp_context_set_background((255,255,255)) #ASSEGNA VALORE DELLO SFONDO
   pdb.gimp_drawable_fill(livello_sfondo, BACKGROUND_FILL) #METTO LO SFONDO BIANCO AL VALORE
   livello_1=pdb.gimp_image_get_active_layer(immagine_1)
   livello_2=pdb.gimp_image_get_active_layer(immagine_2)
   livello_sopra=pdb.gimp_layer_new_from_drawable(livello_1, sfondo) #AGGIUNGE LIVELLO BIANCO A ENTRAMBE LE FOTO
   livello_sotto=pdb.gimp_layer_new_from_drawable(livello_2, sfondo)
   pdb.gimp_image_add_layer(sfondo, livello_sopra, -1)
   pdb.gimp_image_add_layer(sfondo, livello_sotto, -1)
   pdb.gimp_layer_set_offsets(livello_sopra,0,600) #UNISCE UNO ACCANTO ALL ALTRO
   pdb.gimp_layer_set_offsets(livello_sotto,1200,600) #UNISCE UNO ACCANTO ALL ALTRO
   #pdb.gimp_layer_set_offsets(livello_sopra,600,0) UNISCE UNO SOTTO L ALTRO
   #pdb.gimp_layer_set_offsets(livello_sopra,600,1200) UNISCE UNO SOTTO L ALTRO
   unite=pdb.gimp_image_merge_visible_layers(sfondo, CLIP_TO_IMAGE)
   pdb.file_png_save_defaults(sfondo, unite, percorso_output, percorso_output)
   pdb.gimp_image_delete(immagine_1)
   pdb.gimp_image_delete(immagine_2)
   os.remove(percorso_temporaneo)
register(
"python-fu-batch-sdoppia-guanti",
"Sdoppia immagine dei guanti, 1200x1200",
"Sdoppia immagine dei guanti verticalmente o orizzontalmente",
"Khere",
"Khere",
"11-02-2026",
"",
"",
[
(PF_DIRNAME,"cartella","cartella",None)
],
[],
sdoppia
)
main()
