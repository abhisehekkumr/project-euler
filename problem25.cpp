#include<bits/stdc++.h>
using namespace std;


int MAX = 1000;


void addArr(int a[], int b[], int c[]){

      int carry = 0;
      for(int i = MAX - 1; i >= 0; i--){
          c[i] = (a[i] + b[i])%10 + carry;
          carry = (a[i] + b[i])/10;

      }
}

void replaceArr(int a[], int b[], int c[]){

      for(int i = MAX - 1; i >= 0; i--){
          a[i] = b[i];
          b[i] = c[i];
      }


}

void print(int c[]){

        bool flag = false;
        for(int i = 0; i < MAX; i++){

              std::cout << c[i] << " ";
        }



        std::cout  << '\n';
}
int main(){

    int a[MAX] = {0};
    int b[MAX] = {0};
    int c[MAX] = {0};

    a[MAX - 1] = 1;
    b[MAX - 1] = 1;

    int i = 2;
    while(true){


          if(c[0] > 0)
            break;
          addArr(a,b,c);
          replaceArr(a,b,c);
        //  print(c);

          i++;
    }

    std::cout << i << '\n';
}
