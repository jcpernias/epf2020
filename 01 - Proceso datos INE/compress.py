import zipfile
import bz2

def unzip(fname, path = None):
  with zipfile.ZipFile(fname, "r") as zfile:
    zfile.extractall(path)

def compress(ipath, opath, chunk_size = 1024):
  compressor = bz2.BZ2Compressor()
  with open(ipath, "rb") as ifile, open(opath, "wb") as ofile:
    while chunk := ifile.read(chunk_size):
      comp_chunk = compressor.compress(chunk)
      ofile.write(comp_chunk)
    ofile.write(compressor.flush())

