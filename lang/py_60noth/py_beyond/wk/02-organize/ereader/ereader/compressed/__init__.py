from ereader.compressed.bzipped import opener as bz2_opener
from ereader.compressed.gzipped import opener as gzip_opener

__all__ = ['bz2_opener', 'gzip_opener']