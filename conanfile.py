from conans import ConanFile
from conans.tools import download, unzip


class CUTEConan(ConanFile):
    url = 'https://github.com/fmorgner/cute-conan.git'
    license = 'LGPL 3'
    name = 'CUTE'
    version = '2.0.0'
    settings = None

    def _get_archive_name(self):
        return 'cute%s.zip' % self.version.replace('.', '_')

    def source(self):
        zip_name = self._get_archive_name()
        download('http://cute-test.com/attachments/download/86/' + zip_name,
                 zip_name)
        unzip(zip_name)

    def build(self):
        pass

    def package(self):
        self.copy('*.h', src='cute_lib', dst='include/cute')
