# pylint: disable=missing-docstring

import os
from conans import ConanFile, CMake


CHAN = os.getenv("CONAN_CHANNEL", "stable")
USER = os.getenv("CONAN_USERNAME", "fmorgner")


class CUTETestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "CUTE/2.2.1@%s/%s" % (USER, CHAN)
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        os.chdir("bin")
        self.run(".%scute" % os.sep)
