// example multithreaded application

#include <iostream>
#include <thread>

void function1(char symbol) {
  for (int i = 0; i < 200; i++) { std::cout << symbol ; }
}

void function2() {
  for (int i = 0; i < 200; i++) { std::cout << "-"; }
}

int main() {
  // whenever one function hangs or another thread is faster the other function runs
  // interleaving; faster thread executes first
  std::thread t1(&function1, '+');
  std::thread t2(&function2);
  t1.join();
  t2.join();

  // function1();
  // function2();
}