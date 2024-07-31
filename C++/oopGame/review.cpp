/*
- recreation of a game from my OOP class
- review of c++ syntax
*/

// include all libraries
#include <iostream>
#include <vector>
#include <fstream>
#include <string>
// allows use of objects from std library without qualification
using namespace std;

// creating a Warrior class
class Warrior {
public:
  // pass string into constructor by const reference use initilization list
  Warrior(const string& a_name, int a_strength) : name(a_name), strength(a_strength), hired(false) {}

  // specify return type for class methods
  void set_employment(bool choice) { hired = choice; };
  void set_strength(double new_strength) { strength = new_strength; };

  // if method does not alter object mark as const
  bool get_emplyoment() const { return hired; }
  const string& get_name() const { return name; };
  double get_strength() const { return strength; };

private:
  string name;
  double strength;
  bool hired;
};

int main() {
  // entry point for script
  cout << "hello world" << endl;
}