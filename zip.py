import zipfile, os
zipFile = zipfile.ZipFile(os.path.join(os.getcwd(), 'txt.zip'))
zipInfo = zipFile.getinfo('doc.doc')
print 'filename:', zipInfo.filename
print 'date_time:', zipInfo.date_time
print 'compress_type:', zipInfo.compress_type
print 'comment:', zipInfo.comment
print 'extra:', zipInfo.extra
print 'create_system:', zipInfo.create_system
print 'create_version:', zipInfo.create_version
print 'extract_version:', zipInfo.extract_version
print 'extract_version:', zipInfo.reserved
print 'flag_bits:', zipInfo.flag_bits
print 'volume:', zipInfo.volume
print 'internal_attr:', zipInfo.internal_attr
print 'external_attr:', zipInfo.external_attr
print 'header_offset:', zipInfo.header_offset
print 'CRC:', zipInfo.CRC
print 'compress_size:', zipInfo.compress_size
print 'file_size:', zipInfo.file_size
zipFile.close()