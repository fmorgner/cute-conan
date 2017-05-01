from conans import ConanFile


class CUTEConan(ConanFile):
    name = 'CUTE'
    version = '2.1.0'
    description = """CUTE is a fully featured, header-only, efficient C++ unit
                     testing framework"""
    url = 'https://github.com/fmorgner/cute-conan.git'
    license = 'LGPL 3'
    settings = None
    sourceUrl = 'https://github.com/PeterSommerlad/CUTE.git'

    def source(self):
        self.run('git clone ' + self.sourceUrl)

    def build(self):
        pass

    def package(self):
        self.copy('*.h', src='CUTE/cute', dst='include/cute')
