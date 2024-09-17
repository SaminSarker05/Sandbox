#include <thread>
#include <iostream>
#include <vector>
#include <mutex> // can also use mutrx to lock and unlock block of code
#include <atomic> // data type that locks variable to one thread

std::mutex gLock;

// constant variable that is allocated for program lifetime and value carries over
static std::atomic<int> shared_value = 0;
void increment_shared_value() {
  // lock access to shared resource while thread is running
  // gLock.lock();
  ++shared_value;
  // gLock.unlock();
  // error with threads as threads could be reading and writing at same time
  // fix by using std::mutex --> gives threads mutually exlusive access to a shared resource
}

int main() {
  // lambda function [](paramaters...) {code}
  auto lambda = [](int x) {std::cout << "arg: " << x << std::endl;};

  std::vector<std::thread> threads;
  for (int i = 0; i < 1000; i++) {
    threads.push_back(std::thread(increment_shared_value)); // pass function call to thread constructor
  }
  for (int i = 0; i < threads.size(); i++) {
    threads[i].join();  // join threads so threads complete before program
  }
  std::cout << "threads have finished executing... shared value: " << shared_value << std::endl;
}