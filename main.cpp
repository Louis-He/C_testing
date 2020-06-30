#include <iostream>

extern "C" {
#include "sample.h"
}

int main(int argc, char* argv[]) {
    // #ifdef _WIN32
    //     printf("You have Windows Operating System");
    // #elif __linux__
    //     printf("You have Linux Operating System");
    // #elif __APPLE__
    //     printf("You have Mac OS Operating System");
    // #else
    //     printf("Testing not supported");
    // #endif
    int test_num;
    std::cin >> test_num;
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

        hello();
    }
    return 0;
}
