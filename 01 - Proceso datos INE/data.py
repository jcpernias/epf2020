#! /bin/env python3

import compress
import download
import os.path


zname = "datos_2020"
url = f"https://www.ine.es/ftp/microdatos/epf2006/{zname}.zip"
dest_name = f"./{zname}.zip"

if not os.path.exists(dest_name):
  download.download(url, dest_name)

dest_dir = "../data/INE"
compress.unzip(dest_name, dest_dir)


file_dict = {
  "gastos.bz2":  "Fichero de usuario de gastos a2020AJUSTE",
  "hogar.bz2":  "Fichero de usuario de hogar a2020IMPAJUSTE",
  "miembros.bz2":  "Fichero de usuario de miembros a2020IMPAJUSTE",
}

for oname, iname in file_dict.items():
  ipath = f"{dest_dir}/{zname}/{iname}"
  compress.compress(ipath, f"{dest_dir}/{zname}/{oname}")
  os.remove(ipath)

  
