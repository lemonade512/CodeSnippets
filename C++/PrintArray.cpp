#include <stdio.h>

void printArray(const int arr[], int n) {
    const char* prefix = "[ ";
    for (int i = 0; i < n; i++) {
        printf("%s%d", prefix, arr[i]);
        prefix = ", ";
    }
    printf(" ]\n");
}

int main(int argc, const char* argv[]) {
    int my_arr1[] = { 1, 2, 3, 4, 5 };
    int my_arr2[] = { 2, 3, 5, 8, 1 };

    printArray(my_arr1, 5);
    printArray(my_arr2, 5);
}
