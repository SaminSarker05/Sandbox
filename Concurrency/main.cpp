#include <iostream>
#include <thread>
#include <chrono> // use for sleeping
#include <condition_variable>

std::mutex gLock;
std::condition_variable gConditionVariable;

int main() {
  int result = 0;
  bool notified = false;

  // reporting thread
  // must wait on worker thread
  std::thread reporter([&]{
    std::unique_lock<std::mutex> lock(gLock);
    // even if reporter thread executes first, it is blocked if not notified
    if (!notified) {
      // thread will sleep until notified/unblocked
      gConditionVariable.wait(lock); // unlocks lock when notified
    }
    std::cout << "reporting result: " << result << std::endl;
  });

  // working thread
  std::thread worker([&]{
    // more powerful then normal locks
    std::unique_lock<std::mutex> lock(gLock);
    notified = true;
    result++;
    std::this_thread::sleep_for(std::chrono::seconds(5));
    std::cout << "work done" << std::endl;

    gConditionVariable.notify_one();  // wake up any sleeping threads
  });

  // join threads so main thread does not finish before worker and reporter
  reporter.join();
  worker.join();

  return 0;
}