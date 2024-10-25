#include <iostream>
#include "composer.hpp"

const int kMaxComposers = 100;

class Database {
  public:
    Database();
    ~Database();

    // return reference to composer
    Composer& AddComposer(std::string in_first_name, std::string in_last_name, std::string in_genre, int in_yob, std::string in_fact);
    Composer& GetComposer(std::string in_last_name);

    void DisplayAll();
    void DisplayByRank();

  private:
    // array of composers
    Composer composers_[kMaxComposers];
    int next_slot_;
};