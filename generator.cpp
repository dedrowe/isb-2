#include <iostream>
#include <ctime>


int main() {
    srand(time(0));
    int rand_num = std::rand() % 32767;
    for (int i = 0; i < 128; ++i) {
        rand_num = (rand_num * 255 + 7) % 32767;
        std::cout << rand_num % 2;
    }
    return 0;
}
//11100010010111010010101001010000110011110100100110011010000100101101011110001101100111010000010111101111011110100010010000110101