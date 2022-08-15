#include <iostream>
#include <cassert>

int create_matrix(int a, int b){
  int arr[a][b];
  int c = 1;
  for (int i = 0; i < a; i++){
    for (int j = 0; j < b; j++){
      arr[i][j] = c;
      c++;
      }
  }
  return arr;
}

int calcSum(int a, int b){
  int tot = 0;
  int arr = create_matrix(a,b);
  std::cout << "arr is " << arr << "\n";

  return tot;
}

int main(){
  int a,b;
  std::cin >> a >> b;
  /*std::cout << "matrix size is " << create_matrix(a,b) << "\n";*/
  std::cout << "Sum is " << calcSum(a,b) << "\n";
  /*calc sum works good */
  return 0;
}