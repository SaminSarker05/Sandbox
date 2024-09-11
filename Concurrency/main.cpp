#include <iostream>
#include <thread>
#include <map>
#include <string>
#include <chrono>
using namespace std::chrono_literals;

void refreshForecast(std::map<std::string, int> data) {
  while (true) {
    for (auto& item : data) { // take each item by reference
      item.second++;
      std::cout << item.first << " " << item.second << std::endl;
    }
    std::this_thread::sleep_for(2000ms);
  }
}

int main() {
  std::map<std::string, int> data = {
    {"New York", 15},
    {"Dubai", 10},
    {"Paris", 1},
    {"Berlin", 5},
    {"Bangladesh", 24},
  };

  std::thread api(refreshForecast, data);
  api.join();
}