#include <iostream>

int *swap(int first, int sub, int array[])
//This function swaps two members from an array
{
    int swap1 = array[first];
    int swap2 = array[sub];

    array[first] = swap2;
    array[sub] = swap1;   

    return array;
}

int *selectionSort(int arg[], int length)
{
    //This will loop through the array
    for(int i = 0; i < length; i++) 
    {
        int indexMin = i;                                                                                                       //  Use first element as minimum
        int j = i + 1;                                                                                                          //  j as next element

        /*
            When we get the value that we are testing as the min value we need to check if it is smaller than the 
        elements in front of it, if a smaller value is found then it needs to be put before the value tested.
        */
        for(j; j < length; j++)
        {
            if(arg[j] < arg[indexMin])                                                                                          // If j is less than the minimum
            {
                indexMin = j;                                                                                                   // j is now the minimum value
            }
        }
        
        /*
            After checking the array the smaller value needs to be swaped with the value tested
        if the minimum value is i itself it will just stay the same
        */
        swap(i, indexMin, arg);                                                                                                // Call swap funtion to rearrange array 

    }
    return arg;
}

int main()
{ 
    int array[6] = {11, 22, 14, 67, 2, 9};
    int length = (int)std::distance(std::begin(array), std::end(array));
    /* 
        We need to get the size of the array in order to loop through it, it is a bit tricky to do it
    with c style arrays that's why I used std::distance, if a vector was used this would be able to be done
    in an easier way since vectors have a size property
    */
    int *a = selectionSort(array, length);

    /*
        In order to print the array after sorting we need a pointer that can point to each element.
        A way to surpass this would also be the use of a vector instead of a C style array.
    */

    std::cout << "Sorted array: ";
    for(int i = 0; i < length; i++)
    {
        if(i == length - 1)                                                                                                   // Checking where the full stop will be
            std::cout << a[i] << ". "; 
        else
            std::cout << a[i] << ", ";                                                                                        // If i is different then the last element use comma
    }
    std::cout << std::endl;

    return 0;
}