#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <vector>
using namespace std;

int main()
{
   int sizeofarray;
   cin >> sizeofarray;
   int arr[sizeofarray];
   for (int i =0; i<sizeofarray ;i++)
   {
       cin >> arr[i];
   }
   
   reverse(arr , arr+sizeofarray);
   for (int i =0; i<sizeofarray ;i++)
       cout << arr[i] << " "; 
   
   return 0;
}
