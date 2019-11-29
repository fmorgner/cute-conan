# pylint: disable=missing-docstring

import os
from conans import ConanFile


class CUTEConan(ConanFile):
    default_user = 'fmorgner'
    default_channel = 'stable'
    description = '''CUTE - C++ Unit Testing Easier'''
    homepage = 'https://cute-test.com'
    license = 'MIT'
    name = 'CUTE'
    version = '2.2.5'
    scm = {
        'type': 'git',
        'subfolder': 'CUTE',
        'url':  'https://github.com/PeterSommerlad/CUTE.git',
        'revision': 'v%s' % version,
    }
    settings = None
    topics = (
        'framework',
        'test',
        'testing',
        'unit-testing',
    )
    url = 'https://github.com/fmorgner/cute-conan.git'

    def build(self):
        pass

    def package(self):
        self.copy('*.h', src='CUTE/cute', dst='include/cute')
        path = os.path.join(self.package_folder, 'include', 'cute')
        for file in os.listdir(path):
            os.chmod(os.path.join(path, file), 0o664)
