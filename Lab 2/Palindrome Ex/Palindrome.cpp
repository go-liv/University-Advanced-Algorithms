#include <iostream>
#include <vector>

//Check if the array vector given is a palindrome
bool isPalindrome(std::vector<int> array)
{
    //If the array size is 1 then it means it is a palindrome
    if(array.size() < 2)
        return true;

    //if the last and first element of the vector are different
    //it will not be a palindrome
    if(array[0] != array[array.size()-1])
        return false;

    //if we check that the last and first element of the vector
    //are in fact equal then we remove them to check the rest
    array.erase(array.begin(), array.end());


    //recursive function keeps checking with smaller arrays
    return isPalindrome(array);
}


int main()
{
    //retrieving user input
    int len = 0;
    std::cout <<  "Enter the lenght of the array: " << std::endl;
    std::cin >> len;

    std::vector<int> array;
    const char* num; 
    std::cout << "Enter an array: ";
    for(int i = 0; i < len; i++)
    {
        int num = 0;
        std::cin >> num;
        array.push_back(num);
    }
    //

    //managing the outputs
    if(isPalindrome(array) == true)
        std::cout << "Yes" << std::endl;
    else
        std::cout << "No" << std::endl;        

    return 0;
}
