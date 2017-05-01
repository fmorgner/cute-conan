#include "cute/cute.h"
#include "cute/cute_runner.h"
#include "cute/ostream_listener.h"

void test_conan_package()
  {
  ASSERTM("Conan package test failed!", true);
  }

int main(int argc, char * * argv)
  {
  auto suite = cute::suite{};

  suite += CUTE(test_conan_package);

  auto listener = cute::ostream_listener<>{};
  auto runner = cute::makeRunner(listener, argc, argv);

  return !runner(suite, "Conan package suite");
  }
