import shutil

shutil.unpack_archive('py38.zip')

shutil.make_archive('py38','zip','test_zip')


print(shutil.get_archive_formats())