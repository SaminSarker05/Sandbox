#include "composer.hpp"

Composer::Composer() {

}

void Composer::set_first_name(std::string in_first_name) {
  first_name_ = in_first_name;
}
std::string Composer::first_name() {
  return first_name_;
}

void Composer::set_last_name(std::string in_last_name) {
  last_name_ = in_last_name;
}
std::string Composer::last_name() {
  return last_name_;
}

