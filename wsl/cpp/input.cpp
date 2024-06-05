#include <iostream>
#include <string>

int main() {
    std::string line;
    std::string multiline_text;

    // 逐行读取输入，直到遇到空行
    while (std::getline(std::cin, line) && !line.empty()) {
        multiline_text += line + "\n"; // 每行加上换行符
    }

    std::cout << multiline_text;

    return 0;
}
