#include <iostream>
#include <cassert>
int calcSum(int a, int b){
    int arr1[a][b];
    int arr2[b][a];
    int tot = 0;
    /*constructing arr 1 */
    int c = 1;
    for(int i = 0; i < a; i++){
        /*std::cout << "\n";*/
        for(int j = 0; j < b; j++){
            arr1[i][j] = c;
            /*std::cout << c << " ";*/
            c++;
        }
    }
    int d = a * b;
    for(int i =0; i < b; i ++){
        /*std::cout << "\n";*/
        for (int j = 0; j < a; j++){
            arr2[i][j] = d;
            /*std::cout << d << " ";*/
            d--;
        }
    }

    /* multiplying */
    for(int i = 0; i < a; i++){
        for (int j = 0; j < a; j++){
            for (int k = 0; k< b; k++){
                tot += arr1[i][k] * arr2[k][j];
            }
        }
    }


    return tot;
}

int main(){
    assert (calcSum(2, 3) == 131);
    assert (calcSum(3, 3) == 621);
    std::cout << "passed all " << "\n";
    return 0;
}
