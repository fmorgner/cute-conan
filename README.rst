=========================
The CUTE conan.io package
=========================

.. image:: https://img.shields.io/badge/conan.io-CUTE%2F2.2.0-green.svg?logo=data:image/png;base64%2CiVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAMAAAAolt3jAAAA1VBMVEUAAABhlctjlstkl8tlmMtlmMxlmcxmmcxnmsxpnMxpnM1qnc1sn85voM91oM11oc1xotB2oc56pNF6pNJ2ptJ8ptJ8ptN9ptN8p9N5qNJ9p9N9p9R8qtOBqdSAqtOAqtR%2BrNSCrNJ/rdWDrNWCsNWCsNaJs9eLs9iRvNuVvdyVv9yXwd2Zwt6axN6dxt%2Bfx%2BChyeGiyuGjyuCjyuGly%2BGlzOKmzOGozuKoz%2BKqz%2BOq0OOv1OWw1OWw1eWx1eWy1uay1%2Baz1%2Baz1%2Bez2Oe02Oe12ee22ujUGwH3AAAAAXRSTlMAQObYZgAAAAFiS0dEAIgFHUgAAAAJcEhZcwAACxMAAAsTAQCanBgAAAAHdElNRQfgBQkREyOxFIh/AAAAiklEQVQI12NgAAMbOwY4sLZ2NtQ1coVKWNvoc/Eq8XDr2wB5Ig62ekza9vaOqpK2TpoMzOxaFtwqZua2Bm4makIM7OzMAjoaCqYuxooSUqJALjs7o4yVpbowvzSUy87KqSwmxQfnsrPISyFzWeWAXCkpMaBVIC4bmCsOdgiUKwh3JojLgAQ4ZCE0AMm2D29tZwe6AAAAAElFTkSuQmCC
    :target: http://www.conan.io/source/CUTE/2.2.0/fmorgner/stable
    :alt: conan.io

CUTE is a fast, light-weight, header-only unit testing framework for C++. It is
also included in the `Cevelop C++ IDE <https://www.cevelop.com>`_.

When used with older versions of C++ (e.g. before C++11) cute requires parts of
the `Boost <http://www.boost.org>`_ libraries. With C++11 and later, CUTE
requires only the presence of a standard compliant compiler and standard
library.

For more information on cute visit: http://www.cute-test.com

Using this package
==================

To use this package in your projects, include it in your `conanfile.txt`:

.. code-block:: ini

  [requires]
  CUTE/2.2.0@fmorgner/stable


After adding the conan header paths to your build environment, you are set to
start writing test.

Writing tests using CUTE
========================

Getting started using CUTE is fast and easy. The following is an example with a
single failing test.

.. code-block:: cpp

  #include "cute/cute.h"
  #include "cute/cute_runner.h"
  #include "cute/ide_listener.h"
  #include "cute/xml_listener.h"

  void test_your_code()
    {
    ASSERTM("Start testing your code!", false);
    }

  int main(int argc, char * * argv)
    {
    auto suite = cute::suite{};

    suite += CUTE(test_your_code);

    auto xml = cute::xml_file_opener(argc, argv);
    auto listener = cute::xml_listener<cute::ide_listener<>>{xml.out};
    auto runner = cute::makeRunner(listener, argc, argv);

    return !runner(suite, "Example suite");
    }

This is a very basic example, of course you can do a lot more with CUTE. To
learn more, visit: http://www.cute-test.com

Disclaimer
==========

I am not the creator of CUTE. The toolkit is being developed by Prof. `Peter
Sommerlad <https://github.com/PeterSommerlad/CUTE.git>`_ and the `Institute for
Software <https://ifs.hsr.ch>`_ at the University of Applied Sciences
Rapperswil (HSR) in Switzerland. The source code is released under the terms
and conditions of the GNU Lesser General Public License version 3.
