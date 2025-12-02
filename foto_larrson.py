#!/usr/bin/python2
from gimpfu import *
import os

def togli_logo(base_path, folder_path):
 logo_image = pdb.gimp_file_load(base_path, base_path)
 logo_layer = pdb.gimp_image_get_active_layer(logo_image)
 files = [f for f in os.listdir(folder_path) if f.startswith("LR-")]
 if not files:
  print("NESSUN FILE")
  return
 for f in files:
  path_x = os.path.join(folder_path, f)
  output_path = os.path.join(folder_path, "OUTPUT/" + os.path.splitext(f)[0] + ".jpg")
  print("Elaboro {} -> {}".format(path_x, output_path))
  img_x = pdb.gimp_file_load(path_x, path_x)
  img_tmp = pdb.gimp_image_duplicate(logo_image)
  logo_layer_tmp = pdb.gimp_image_get_active_layer(img_tmp)
  base_layer = pdb.gimp_file_load_layer(img_tmp, path_x)
  pdb.gimp_image_insert_layer(img_tmp, base_layer, None, 1)
  pdb.gimp_drawable_set_visible(logo_layer_tmp, True)
  pdb.gimp_drawable_set_visible(base_layer, True)
  pdb.gimp_layer_set_mode(logo_layer_tmp, LAYER_MODE_DIVIDE)
  pdb.gimp_image_set_active_layer(img_tmp, logo_layer_tmp)
  merged = pdb.gimp_image_merge_down(img_tmp, logo_layer_tmp, CLIP_TO_IMAGE) #QUA UNISCE I LIVELLI
  pdb.file_png_save_defaults(img_tmp, merged, output_path, output_path) #QUA SALVA IL FILE
  pdb.gimp_image_delete(img_tmp) #ELIMINA ENTRAMBE LE FOTO CREATE PER FARE L UNIONE DEI LIVELLI
  pdb.gimp_image_delete(img_x)
 pdb.gimp_image_delete(logo_image)
 print("Operazione completata su tutti i file LR-*.")
# ---- DESCRIZIONE PLUGIN ----
register(
 "python-fu-batch-divide-logo",
 "Batch merge Dividi (logo sopra)",
 "Toglie il logo dalle foto larrson partendo da foto.jpg come riferimento per posizione logo",
 "Khere",
 "Khere",
 "2025",
 "",
 "",
 [
  (PF_FILE, "base_path", "Immagine logo (livello superiore)", None),
  (PF_DIRNAME, "folder_path", "Cartella con file LR-*", None),
 ],
 [],
 togli_logo #QUA RICHIAMA LA FUNZIONE
)
main()
