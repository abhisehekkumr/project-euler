#include<bits/stdc++.h>
using namespace std;

bool nextPermutation(int array[], int size){

  int i = size - 1;
     while (i > 0 && array[i - 1] >= array[i])
         i--;
     // Now i is the head index of the suffix

     // Are we at the last permutation already?
     if (i <= 0)
         return false;

     // Let array[i - 1] be the pivot
     // Find rightmost element that exceeds the pivot
     int j = size - 1;
     while (array[j] <= array[i - 1])
         j--;
     // Now the value array[j] will become the new pivot
     // Assertion: j >= i

     // Swap the pivot with j
     int temp = array[i - 1];
     array[i - 1] = array[j];
     array[j] = temp;

     // Reverse the suffix
     j = size - 1;
     while (i < j) {
         temp = array[i];
         array[i] = array[j];
         array[j] = temp;
         i++;
         j--;
     }

     // Successfully computed the next permutation
     return true;
}

void printArr(int arr[], int size){

      for(int i = 0 ; i < size; i++)
        std::cout << arr[i];
      std::cout << '\n';
}

int main(){
    int arr[] = {0,1,2,3,4,5,6,7,8,9};
    int size = 10;
    int i = 1;
    printArr(arr,size);
    while(i < 1000000){
      nextPermutation(arr,size);
      printArr(arr,size);
      i++;
    }
}
