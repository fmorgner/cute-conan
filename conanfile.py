from conans import ConanFile


class CUTEConan(ConanFile):
    name = 'CUTE'
    version = '2.2.0'
    description = """CUTE - C++ Unit Testing Easier"""
    url = 'https://github.com/fmorgner/cute-conan.git'
    license = 'LGPL 3'
    settings = None

    sourceUrl = 'https://github.com/PeterSommerlad/CUTE.git'
    commitHash = '2d1944fa73d9ce16b237068d1289fc7d9d68fbf4'

    def source(self):
        self.run('git clone ' + self.sourceUrl)
        self.run('cd CUTE && git checkout ' + self.commitHash)

    def build(self):
        pass

    def package(self):
        self.copy('*.h', src='CUTE/cute', dst='include/cute')
