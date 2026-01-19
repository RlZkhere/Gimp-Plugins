#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from gimpfu import *
import os
def unisci_foto(cartella):
 for sub in os.listdir(cartella):
  percorso_cartella = os.path.join(cartella, sub)
  files = os.listdir(percorso_cartella)
  f1, f2 = files[0], files[1]
  if "_2" in f2:
   f1 = files[1]
   f2 = files[0]
  file_1 = os.path.join(percorso_cartella, f1)
  file_2 = os.path.join(percorso_cartella, f2)
  img1 = pdb.gimp_file_load(file_1, file_1)
  img2 = pdb.gimp_file_load(file_2, file_2)
  w1_orig = img1.width
  pdb.plug_in_autocrop(img1, img1.active_layer)
  h1_crop = img1.height
  pdb.gimp_image_resize(img1, w1_orig, h1_crop, 0, 0)
  bg1 = pdb.gimp_layer_new(img1, img1.width, img1.height, RGB_IMAGE, "BG", 100, NORMAL_MODE)
  pdb.gimp_image_insert_layer(img1, bg1, None, 0)
  pdb.gimp_context_set_foreground((255, 255, 255))
  pdb.gimp_drawable_fill(bg1, FOREGROUND_FILL)
  pdb.gimp_image_lower_item_to_bottom(img1, bg1)
  pdb.gimp_image_flatten(img1)
  w2_orig = img2.width
  pdb.plug_in_autocrop(img2, img2.active_layer)
  h2_crop = img2.height
  pdb.gimp_image_resize(img2, w2_orig, h2_crop, 0, 0)
  bg2 = pdb.gimp_layer_new(img2, img2.width, img2.height, RGB_IMAGE, "BG", 100, NORMAL_MODE)
  pdb.gimp_image_insert_layer(img2, bg2, None, 0)
  pdb.gimp_context_set_foreground((255, 255, 255))
  pdb.gimp_drawable_fill(bg2, FOREGROUND_FILL)
  pdb.gimp_image_lower_item_to_bottom(img2, bg2)
  pdb.gimp_image_flatten(img2)
  h1 = img1.height
  h2 = img2.height
  if h1 + h2 > 1200:
   pdb.gimp_image_delete(img1)
   pdb.gimp_image_delete(img2)
   continue   
  finale = pdb.gimp_image_new(1200, 1200, RGB)
  sfondo = pdb.gimp_layer_new(finale, 1200, 1200, RGB_IMAGE, "Sfondo", 100, NORMAL_MODE)
  pdb.gimp_image_insert_layer(finale, sfondo, None, 0)
  pdb.gimp_context_set_foreground((255, 255, 255))
  pdb.gimp_drawable_fill(sfondo, FOREGROUND_FILL)
  top = pdb.gimp_layer_new_from_drawable(img1.active_layer, finale)
  pdb.gimp_image_insert_layer(finale, top, None, -1)
  pdb.gimp_layer_set_offsets(top, 0, 0)
  bottom = pdb.gimp_layer_new_from_drawable(img2.active_layer, finale)
  pdb.gimp_image_insert_layer(finale, bottom, None, -1)
  pdb.gimp_layer_set_offsets(bottom, 0, h1)
  pdb.gimp_image_flatten(finale)
  drw = pdb.gimp_image_get_active_layer(finale)
  out_path = os.path.join(percorso_cartella, f1.replace('_2.jpg','_1.jpg'))
  pdb.file_jpeg_save(finale, drw, out_path, out_path,0.95, 0, 1, 0, "", 0, 1, 0, 0)
  pdb.gimp_image_delete(finale)
  pdb.gimp_image_delete(img1)
  pdb.gimp_image_delete(img2)
register(
    "python-fu-batch-unisci-foto",
    "Unisce 2 foto verticalmente su 1200x1200 (sfondo bianco)",
    "Prende 2 immagini per sottocartella, le mette una sopra l'altra su canvas 1200x1200 bianca, salva finale_merged.jpg",
    "Khere",
    "Khere",
    "2025-12-18",
    "Batch unisci foto 1200x1200",
    "",
    [(PF_DIRNAME, "cartella", "Cartella base (con sottocartelle)", None)],
    [],
    unisci_foto
)

main()
