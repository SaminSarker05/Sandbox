#include <iostream> // input output stream
#include <thread>
#include <vector>

void test(int x) {
  std::cout << "hello from another thread" << std::endl;
  std::cout << "argument passed " << 100 << std::endl;
}

int main() {
  auto lambda = [](int x) {std::cout << "lambda function arg: " << x << std::endl; return 0;};

  // can create a vector of thread objects
  std::vector<std::thread> threads;
  // first launch 10 threads
  for (int i = 0; i < 10; i++) {
    threads.push_back(std::thread(lambda, i)); // can pass in function arguments
  }
  // then join the threads and wait for their execition to finish before going back to main program
  for (int i = 0; i < 10; i++) {
    threads[i].join();
  }
  // interleaving of thread outputs

  // to make a thread create a thread object passing in address to function and any arguments
  // std::thread t1(lambda, 100);
  // .join();  // blocks current thread untill identified thread finishes execution

  // the script itself is running on a thread
  std::cout << "hello this is the main thread" << std::endl;
  return 0;
}