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
