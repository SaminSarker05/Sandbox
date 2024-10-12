// templates
// allows generic class for family of classes
// reduces redundant code
// pass type into class instance to specify; tells compiler what to do

#include <iostream>

template <typename T, int length> // can have multiple variables
class Array {
public:
  T array[length];

  void fill(T value) {
    for (int i = 0; i < length; i++) {
      array[i] = value;
    }
  }

  T& at(int index) {
    return array[index];
  }
};

int main() {
  Array<int, 10> array;  // all occurences of T and length in template replaced at compile time
  array.fill(4);
  std::cout << array.at(0) << std::endl;

  Array<std::string, 5> another;
  another.fill("hello");
  another.at(3) = "!23";  // method returns reference so we can modify
  std::cout << another.at(3) << std::endl;
}