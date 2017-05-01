The CUTE conan.io package
=========================

[![badge](https://img.shields.io/badge/conan.io-CUTE%2F2.0.0-green.svg?logo=dat\
a:image/png;base64%2CiVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAMAAAAolt3jAAAA1VBMVEUAAA\
Bhlctjlstkl8tlmMtlmMxlmcxmmcxnmsxpnMxpnM1qnc1sn85voM91oM11oc1xotB2oc56pNF6pNJ2p\
tJ8ptJ8ptN9ptN8p9N5qNJ9p9N9p9R8qtOBqdSAqtOAqtR%2BrNSCrNJ/rdWDrNWCsNWCsNaJs9eLs9\
iRvNuVvdyVv9yXwd2Zwt6axN6dxt%2Bfx%2BChyeGiyuGjyuCjyuGly%2BGlzOKmzOGozuKoz%2BKqz\
%2BOq0OOv1OWw1OWw1eWx1eWy1uay1%2Baz1%2Baz1%2Bez2Oe02Oe12ee22ujUGwH3AAAAAXRSTlMA\
QObYZgAAAAFiS0dEAIgFHUgAAAAJcEhZcwAACxMAAAsTAQCanBgAAAAHdElNRQfgBQkREyOxFIh/AAA\
AiklEQVQI12NgAAMbOwY4sLZ2NtQ1coVKWNvoc/Eq8XDr2wB5Ig62ekza9vaOqpK2TpoMzOxaFtwqZu\
a2Bm4makIM7OzMAjoaCqYuxooSUqJALjs7o4yVpbowvzSUy87KqSwmxQfnsrPISyFzWeWAXCkpMaBVI\
C4bmCsOdgiUKwh3JojLgAQ4ZCE0AMm2D29tZwe6AAAAAElFTkSuQmCC)](http://www.conan.io/s\
ource/CUTE/2.1.0/fmorgner/stable)

This package contains the CUTE unit testing framework, a light-weight, modern,
and efficient testing framework for C++. CUTE is a header-only testing
framework and does not depend on any external libraries besides the C++
Standard Template Library (STL).

For more information on cute visit: http://www.cute-test.com

Using this package
------------------

To use this package in your projects, include it in your `conanfile.txt`:

```
[requires]
CUTE/2.1.0@fmorgner/stable
```

After adding the conan header paths to your build environment, you are set to
start writing test.

Writing tests using CUTE
------------------------

Getting started using cute is fast and easy. The following is an example with a
single failing test.

```cpp
#include <cute/cute.h>
#include <cute/cute_runner.h>
#include <cute/ide_listener.h>
#include <cute/xml_listener.h>

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
```

This is a very basic example, of course you can do a lot more with CUTE. To
learn more, visit: http://www.cute-test.com

Disclaimer
==========

I am not the creator of CUTE. The toolkit is being developed by Prof. Peter
Sommerlad and the Institute for Software at the University of Applied Sciences
Rapperswil (HSR) in Switzerland. The source code is released under the terms
and conditions of the GNU Lesser General Public License version 3.
