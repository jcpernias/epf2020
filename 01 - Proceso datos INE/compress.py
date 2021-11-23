import zipfile
import bz2
import os.path

def unzip(fname, path = None):
  with zipfile.ZipFile(fname, "r") as zfile:
    members = [ x for x in zfile.infolist() if not x.is_dir() ]
    for m in members:
      m.filename = os.path.basename(m.filename) # remove directories
      zfile.extract(m, path)

def compress(ipath, opath, chunk_size = 1024):
  compressor = bz2.BZ2Compressor()
  with open(ipath, "rb") as ifile, open(opath, "wb") as ofile:
    while chunk := ifile.read(chunk_size):
      comp_chunk = compressor.compress(chunk)
      ofile.write(comp_chunk)
    ofile.write(compressor.flush())

