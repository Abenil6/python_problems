def list_numbers():
    numbers=[1,2,3,4,5,6]
    print(f"Original Numbers: {numbers}")


    new_number=7
    numbers.append(new_number)

    print(f"The new List after ading a number;{numbers}")

    numbers.remove(3)

    print(f"The List after removing number 3 :{numbers}")

    max_value=max(numbers)
    min_value=min(numbers)

    print(f"the maximum value from the list :{max_value}")
    print(f"the minimum value from the list :{min_value}")

list_numbers()