#include <iostream>

using string = std::string;

const string EXIT = "exit";

string[] tokenized_line(string line){
  string tokens[] = [];
}

bool should_exit(string line){
  return line == EXIT;
}

int main() {
  while(true) {
    string line;
    std::cout<< "> ";
    std::cin >> line;

    if(should_exit(line)){
      break;
    }

    std::cout << "Evaluates to: "<< line << std::endl;
  }

  std::cout << "Goodbye :wave:" << std::endl;
  return 0;
}
