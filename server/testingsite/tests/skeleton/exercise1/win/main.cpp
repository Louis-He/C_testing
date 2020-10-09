#include <iostream>

extern "C" {
#include "sample.h"
}

int main(int argc, char* argv[]) {
    int test_num;
    std::cin >> test_num;
    std::cout << "=== Test Number: " << test_num << " ===" << std::endl;
    for (int i = 0; i < test_num; i++) {
        int test_check;
        std::cin >> test_check;

        try {
            if (test_check != (i + 1)) {
                std::cerr << "\033[31mRead input file error, sanity check failed. Occured at case #" << i + 1 << "\033[0m\n";
                break;
            }
        } catch (const std::exception& e) {
            std::cerr << "\033[31mRead input file error, critical error. Occured at case #" << i + 1 << "\033[0m\n";
        }
        std::cout << "=== Case #" << i + 1 << " ===" << std::endl;
        hello();
        std::cout << "\n=== END ===" << std::endl;
    }
    return 0;
}
