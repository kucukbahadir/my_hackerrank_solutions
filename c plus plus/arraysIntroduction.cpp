/////////////////////// my code ///////////////////////
int main() {
    int numberOfElements;
    cin >> numberOfElements;
    int numberArray[numberOfElements];
    
    for(int i = 0; i < numberOfElements; ++i) {
        int tmp;
        cin >> tmp;
        numberArray[i] = tmp;
    }

    for(int i = numberOfElements - 1; i >= 0; --i) {
        cout << numberArray[i] << " ";
    }

    return 0;
}
//////////////////// end of my code ///////////////////