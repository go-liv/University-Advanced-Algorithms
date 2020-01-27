#include <iostream>

int isArmstrong(int number)
{
    std::string numStr = std::to_string(number);
    const char* digits = numStr.c_str();
    int cube = 0;
    int total = 0;

    if(numStr.length() != 3)
    {
        std::cout << "Not a 3 digit number" << std::endl;
    }

    std::cout << digits << std::endl;

    for(int i = 0; i < numStr.length(); i++)
    {
        cube = (digits[i]-'0')*(digits[i]-'0')*(digits[i]-'0');
        total += cube;
    }

    if(total != number)
        std::cout << "Not an Armstrong number." << std::endl;
    else
        std::cout << "That is an Armstrong number!" << std::endl;

    return 0;
}

int main()
{
    int num = 0;

    std::cout <<  "Enter a number: " << std::endl;
    std::cin >> num;

    isArmstrong(num);

    return 0;
}
