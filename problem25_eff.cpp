/* this problem can be solved using pen and paper , what an easy solution
fibonacci number always converges to F(n)
where

      f(n) = [phi^n/sqrt(5)]
    number will always converge to this for any value of n,

where phi = 1.6180. however it is an irretional number so we can't use its actual
value. thus for finding number that has 1000 numbers in it. we can do this
following relation

      [phi^n]
      -------  > 10^999
      sqrt(5)

  thus taking log on both sides

  log(phi)*n - log(5)/2 > 999*log(10)

  isolating n on left side we will have following relation

            log(10)*999 + log(5)/2
      n >   ---------------------
              log(phi)

   this will give us an index for first fibonacci that has more than 1000 degits
   and result for above solution will 4781.859. As n > greater than  this result
   we can use ceil function to find the greatest closses number
   ans = 4782
*/


#include<bits/stdc++.h>
using namespace std;

int main(){

      double phi_with_log = 0.20897851727;
      double result = (999 + log10(5)/2)/(phi_with_log);
      int number = int(result);
      std::cout << "index for 1000 digit number is: " << number << '\n';
}
