# 1. Use a variable to store a number, then write a condition that prints 0 if the number is equal to 10, and prints -1 otherwise.

# number = 10

# if number == 10:
#     print(0)
# else:
#     print(1)

# 2. Use a variable to store a number, then write a condition that prints -1 if the number is less than 10, prints 1 if the number is greater than 10, and prints 0 if the number is equal to 10.

# number = 11

# if number < 10:
#     print(-1)
# elif number > 10:
#     print(1)
# elif number == 10:
#     print(0)

# 3. Use variables to store two numbers, then write a condition that prints 1 if the numbers are both less than 10, and prints 0 otherwise.

# number1 = 99
# number2 = 101

# if number1 and number2 < 10:
#     print(1)
# else:
#     print(0)

# 4. Use a variable to store a number, then write a condition that prints 1 if the number is over 9000, and prints -1 otherwise.

# number = 83

# if number > 9000:
#     print(1)
# else:
# print(-1)

# 5. Use a variable to store a number, then write a condition that prints 9 if the number is less than 10, prints 19 if the number is less than 20, prints 29 if the number is less than 30, and prints -1 otherwise (only one print statement should occur).

# number = 5

# if number < 10:
#     print(9)
# elif number < 20:
#     print(19)
# elif number < 30:
#     print(29)
# else:
#     print(-1)

# 6. Use variables to store two numbers, then write a condition that prints 100 if either number is greater than 10, and prints -100 otherwise.

# number1 = 3
# number2 = 4

# if number1 > 10 or number2 > 10:
#     print(100)
# else:
#     print(-100)

# 7. Use a variable to store a number, then write a condition that prints 1776 if the number is less than 0, and prints 1979 otherwise.


# number = 6

# if number < 0:
#     print(1776)
# else:
#     print(1979)

# 8. Use a variable to store a number, then write a condition that prints 100 if the number equals 100, prints 99 if the number is equal to 99, and prints 0 otherwise.

# number = 100

# if number == 100:
#     print(100)
# elif number == 99:
#     print(99)
# else:
#     print(0)

# 9. Use variables to store two numbers, then write a condition that prints 1 if the first number is less than zero and the second number is greater than 0, and prints 0 otherwise.

# number1 = -1
# number2 = 3

# if number1 < 0 and number2 > 0:
#     print(1)
# else:
#     print(0)

# 10. Use a variable to store a number, then write a condition that prints 5 if the number is greater than 80, prints 4 if the number is greater than 60, prints 3 if the number is greater than 40, prints 2 if the number is greater than 20, and prints 1 otherwise (only one print statement should occur).

# number = 88

# if number > 80:
#     print(5)
# elif number > 60:
#     print(4)
# elif number > 40:
#     print(3)
# elif number > 20:
#     print(2)
# else:
#     print(1)

# SOLUTIONS: https://gist.github.com/peterxjang/aee70f966f0f725609eee89b06e8a6c0

# 1. Write a program that uses variables to store a first and last name, then prints the full name in one line using string concatenation (the + operator).

# first_name = "Bob"
# last_name = "Larsen"

# print(first_name + " " + last_name)

# 2. Write a program that uses variables to store a first and last name, then prints the full name in one line using string interpolation (the #{} operator).

# first_name = "Bob"
# last_name = "Larsen"

# print(f'{first_name} {last_name}')

# 3. Write a program that asks the user to input a word. If the word is "marco", print "polo".


# word = input("Please type in a word ")
# if word == "marco":
#     print("polo")

# 4. Write a program that uses variables to store three different colors, then prints out a sentence using the colors with string concatenation (the + operator).

# first_color = "blue"
# second_color = "green"
# third_color = "beige"

# print("The sky is so" + " " + first_color + " " + "and the grass is so " +
#       second_color + " " + "and that building is " + third_color)

# 5. Write a program that uses variables to store three different colors, then prints out a sentence using the colors with string interpolation (the #{} operator).


# first_color = "blue"
# second_color = "green"
# third_color = "beige"

# print(
#     f'The sky is so {first_color} and the grass is so {second_color} and that building is {third_color}')

# 6. Write a program that asks the user to enter a name. If the name is not "Santa", print "You're not Santa."

# name = input("Please enter a name ")

# if name != "Santa":
#     print("Your not Santa...")

# 7. Write a program that uses variables to store a book's title and author, then prints out a sentence using that information with string concatenation (the + operator).

# title = "From Head to Toe"
# author = "Eric Carl"

# print("The book " + title + " " + "by " + author + " " + "is a great read")

# 8. Write a program that uses variables to store a book's title and author, then prints out a sentence using that information with string interpolation (the #{} operator).

# title = "From Head to Toe"
# author = "Eric Carl"

# print(f'The book {title} by {author} is a great read')

# 9. Write a program that asks the user to enter a password. If the password is "Joshua", the program responds "Shall we play a game?". For any other password, the program responds "Access denied"

# password = input("Please enter a password ")

# if password == "Joshua":
#     print("Shall we play a game?")
# else:
#     print("access denied")

# 10. Write a program that uses variables to store the names of three cities, then prints out a sentence using that information with string concatenation (the + operator).

# city_one = "New York"
# city_two = "New Jersey"
# city_three = "Connecticut"

# print(city_one + " " + city_two + " " + "and " +
#       city_three + " make up the tristate area")

# SOLUTIONS: https://gist.github.com/peterxjang/79ba5acc912a86cce2a18c2f14b1c712

# 1. Write a program that asks the user to enter a word, then prints that word with all capital letters.

# word = input("Please enter a word ")
# print(word.upper())

# 2. Write a program that asks the user to enter a number, then prints "That's a big number" if the number is greater than 100.

# number = input("Please enter a number ")
# if int(number) > 100:
#     print("That's a big number")

# 3. Write a program that asks the user to enter two numbers, then prints the numbers added together.

# number1 = input("Please enter a number ")
# number2 = input("Please enter another number ")

# print(int(number1) + int(number2))

# 4. Write a program that asks the user to enter a word, then prints that word in reverse order.

# word = input("Please enter a word ")[::-1]

# print(word)

# 5. Write a program that asks the user to enter a number, then prints the number times 10.

# number = input("Please enter a number ")

# print(int(number) * 10)

# 6. Write a program that asks the user to enter two words, then prints both words on the same line in all capital letters.

# word1 = input("Please enter a word ")
# word2 = input("Please enter another word ")

# print(f'{word1.upper()} {word2.upper()}')

# 7. Write a program that asks the user to enter a word, then prints the number of letters in the word.

# word = input("Please enter a word ")
# print(f'Your word was {len(word)} charachters long')

# 8. Write a program that asks the user to enter a number, then prints "That's a negative number" if the number is less than 0.

# number = input("Please enter a number ")

# if int(number) < 0:
#     print("Thats a negative number")

# 9. Write a program that asks the user to enter two numbers, then prints the two numbers multiplied together.

# number1 = input("Please enter a number ")
# number2 = input("Please enter another number ")

# print(
#     f'the product of {number1} and {number2} is {int(number1) * int(number2)}')

# 10. Write a program that asks the user to enter a word, then prints "That's a long word" if the word has more than 5 letters.

# word = input("Please enter a word ")

# if len(word) > 5:
#     print("Thats a long word")

# SOLUTIONS: https://gist.github.com/peterxjang/1539a3ad79728ba4fb68dd8d07279c29

# 1. Write a while loop to print the numbers 1 through 10.

# i = 1

# while i <= 10:
#     print(i)
#     i += 1

# i = 11

# for num in range(1, i):
#     print(num)

# 2. Write a while loop that prints the word "hello" 5 times.

# i = 0

# while i < 5:
#     print("hello")
#     i += 1

# i = 5

# for num in range(1, i):
#     print("hello")

# 3. Write a while loop that asks the user to enter a word and will run forever until the user enters the word "stop".

# while True:
#     word = input("Please enter a word\n")
#     if word == "stop":
#         break

# 4. Write a while loop that prints the numbers 0 through 100, increasing by 5 each time.

# i = 0

# while i <= 100:
#     print(i)
#     i += 5

# i = 100

# for num in range(0, i, 5):
#     print(num)

# 5. Write a while loop that prints the number 9000 ten times.

# i = 0

# while i < 10:
#     print(9000)
#     i += 1

# i = 11

# for num in range(1, i):
#     print(9000)

# 6. Write a while loop that asks the user to enter a number and will run forever until the user enters a number greater than 10.

# while True:
#     number = input("Please enter a number\n")
#     if int(number) > 10:
#         break

# 7. Write a while loop that prints the numbers 50 to 70.

# i = 50

# while i <= 70:
#     print(i)
#     i += 1

# 8. Write a while loop that prints the phrase "Around the world" 144 times.

# i = 1

# while i <= 144:
#     print(i, "Around the world")
#     i += 1

# 9. Write a while loop that asks the user to enter a word and will run forever until the user enters a word with more than 5 letters.

# while True:
#     word = input("Please enter a word\n")
#     if len(word) > 5:
#         break

# 10. Write a while loop that prints the even numbers from 2 to 40.

# i = 2

# while i <= 40:
#     print(i)
#     i += 2

# i = 42

# for num in range(2, i, 2):
#     print(num)

# SOLUTIONS: https://gist.github.com/peterxjang/c4ec0e0f8f6e123d65ada9bf3100068b

# 1. Create an array to store 3 words. Then add two more words to the array and print the array on one line.

# words = ["bear", "went", "over"]
# words.append("the")
# words.append("mountain")
# print(words)

# 2. Create an array to store 4 letters. Then change the second letter to a number and print the array on one line.

# letters = ["a", "b", "c", "d"]
# letters[1] = 2
# print(letters)

# 3. Create an array to store 5 numbers. Then print out each number on separate lines with a while loop.

# numbers = [1, 2, 3, 4, 5]

# i = 0
# while i < len(numbers):
#     print(numbers[i])
#     i += 1

# 4. Create an array to store 1 number. Then add three more numbers to the array and print the array on one line.

# numbers = [1]
# numbers.extend([2, 3, 4])
# print(numbers)

# 5. Create an array to store 3 strings with lower case letters. Then change the third string to have all capital letters and print the array on one line.

# letters = ["apple", "pear", "peach"]
# print(letters[2].upper())

# 6. Create an array to store 3 names. Then print out each name on separate lines with a while loop.

# names = ["Bill", "Joe", "Jay"]
# i = 0
# while i < len(names):
#     print(names[i])
#     i += 1

# for name in names:
#     print(name)

# 7. Create an array to store 2 strings. Then add one string to the array and print the array on one line.

# strings = ["It", "is"]
# strings.append("night")
# print(strings)

# 8. Create an array to store 5 numbers. Then change the first number to 10 times its original value and print the array on one line.

# numbers = [99, 98, 97, 96, 95]
# numbers[0] *= 10
# print(numbers)

# 9. Create an array to store 2 numbers. Then print out each number on separate lines with a while loop.

# numbers = [5, 999]

# i = 0
# while i < len(numbers):
#     print(numbers[i])
#     i += 1

# for number in numbers:
#     print(number)
# 10. Create an array to store names of 3 different countries. Then add one more country and print the array one line.

# countries = ["China", "India", "United States"]
# countries.append("Indonesia")
# print(countries)

# SOLUTIONS: https://gist.github.com/peterxjang/7095a2b19e1da2cc18d4a0dcd66cb8f1

# 1. Write a function that takes in a number and returns the number times two. Then run the function and print the result.

# 2. Write a function that takes in a string and returns the string with all capital letters. Then run the function and print the result.

# 3. Write a function that takes in two numbers and returns the first number subtracted by the second. Then run the function and print the result.

# 4. Write a function that takes in a number and returns the number times itself. Then run the function and print the result.

# 5. Write a function that takes in a string and returns the first letter of the string. Then run the function and print the result.

# 6. Write a function that takes in three strings and returns a string that combines all three strings with spaces in between. Then run the function and print the result.

# 7. Write a function that takes in a number and returns the number as a string. Then run the function and print the result.

# 8. Write a function that takes in a string and returns the string repeated 5 times. Then run the function and print the result.

# 9. Write a function that takes in 3 numbers and returns the average (the sum divided by 3.0). Then run the function and print the result.

# 10. Write a function that takes in a number and returns the number times 10 plus 30. Then run the function and print the result.

# SOLUTIONS: https://gist.github.com/peterxjang/6a26d3c698c651dd6e9ccb168d32648c

#  1. Start with an array of numbers and create a new array with each number times 3.
#     For example, [1, 2, 3] becomes [3, 6, 9].

#  2. Start with an array of strings and create a new array with each string upcased.
#     For example, ["hello", "goodbye"] becomes ["HELLO", "GOODBYE"].

#  3. Start with an array of hashes and create a new array of string values from each hash's :name key.
#     For example, [{name: "Alice", age: 27}, {name: "Blane", age: 16}] becomes ["Alice", "Blane"].

#  4. Start with an array of numbers and create a new array with each number plus 7.
#     For example, [1, 2, 3] becomes [8, 9, 10].

#  5. Start with an array of strings and create a new array with each string's length.
#     For example, ["hello", "goodbye"] becomes [5, 7].

#  6. Start with an array of hashes and create a new array of number values from each hash's :age key.
#     For example, [{name: "Alice", age: 27}, {name: "Blane", age: 16}] becomes [27, 16].

#  7. Start with an array of numbers and create a new array with each number divided by 2.
#     For example, [1, 2, 3] becomes [0.5, 1.0, 1.5].

#  8. Start with an array of strings and create a new array with each string's first letter only.
#     For example, ["hello", "goodbye"] becomes ["h", "g"].

# 9.  Start with an array of hashes and create a new array of number values from each hash's :age key times 2.
#     For example, [{name: "Alice", age: 27}, {name: "Blane", age: 16}] becomes [54, 32].

# 10. Start with an array of numbers and create a new array with each number converted into a string.
#     For example, [1, 2, 3] becomes ["1", "2", "3"].

# SOLUTIONS (using while loop): https://gist.github.com/peterxjang/b9ac4390aad2301a2238efc95c904f3d
# SOLUTIONS (using .each shortcut): https://gist.github.com/peterxjang/66598fd7cdbc67fe663624e217cebbaf
# SOLUTIONS (using .map shortcut): https://gist.github.com/peterxjang/23a8f8a51601e4288ba3a8aa6d1f1c98

#  1. Start with an array of numbers and create a new array with only the numbers less than 20.
#     For example, [2, 32, 80, 18, 12, 3] becomes [2, 18, 12, 3].

#  2. Start with an array of strings and create a new array with only the strings that start with the letter "w".
#     For example, ["winner", "winner", "chicken", "dinner"] becomes ["winner", "winner"].

#  3. Start with an array of hashes and create a new array with only the hashes with prices greater than 5 (from the :price key).
#     For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes [{name: "chair", price: 100}].

#  4. Start with an array of numbers and create a new array with only the even numbers.
#     For example, [2, 4, 5, 1, 8, 9, 7] becomes [2, 4, 8].

#  5. Start with an array of strings and create a new array with only the strings shorter than 4 letters.
#     For example, ["a", "man", "a", "plan", "a", "canal", "panama"] becomes ["a", "man", "a", "a"].

#  6. Start with an array of hashes and create a new array with only the hashes with names shorter than 6 letters (from the :name key).
#     For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes [{name: "chair", price: 100}, {name: "book", price: 4}].

#  7. Start with an array of numbers and create a new array with only the numbers less than 10.
#     For example, [8, 23, 0, 44, 1980, 3] becomes [8, 0, 3].

#  8. Start with an array of strings and create a new array with only the strings that don't start with the letter "b".
#     For example, ["big", "little", "good", "bad"] becomes ["little", "good"].

#  9. Start with an array of hashes and create a new array with only the hashes with prices less than 10 (from the :price key).
#     For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes [{name: "pencil", price: 1}, {name: "book", price: 4}].

# 10. Start with an array of numbers and create a new array with only the odd numbers.
#     For example, [2, 4, 5, 1, 8, 9, 7] becomes [5, 1, 9, 7].

# SOLUTIONS (using while loop): https://gist.github.com/peterxjang/7de16ed43ea506e98df3fa15074b84f8
# SOLUTIONS (using .each shortcut): https://gist.github.com/peterxjang/a702894841c7018ed8c127b647ae21f8
# SOLUTIONS (using .select shortcut): https://gist.github.com/peterxjang/b8c8fb8b77b2cae7bb9cc62a3a434761

#  1. Start with an array of numbers and compute the sum of all the numbers.
#     For example, [5, 10, 8, 3] becomes 26.

#  2. Start with an array of strings and combine them all into a single string.
#     For example, ["volleyball", "basketball", "badminton"] becomes "volleyballbasketballbadminton".

#  3. Start with an array of hashes and compute the sum of the prices (from the :price key).
#     For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes 105.

#  4. Start with an array of numbers and compute the the minumum number.
#     For example, [5, 10, 8, 3, 9] becomes 3.

#  5. Start with an array of strings and compute the total length of all the strings.
#     For example, ["volleyball", "basketball", "badminton"] becomes 29.

#  6. Start with an array of hashes and find the hash with the lowest price (from the :price key).
#     For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes {name: "pencil", price: 1}.

#  7. Start with an array of numbers and compute product of all the numbers.
#     For example, [5, 10, 8, 3] becomes 1200.

#  8. Start with an array of strings and combine them all into a single string, separated by dashes.
#     For example, ["volleyball", "basketball", "badminton"] becomes "-volleyball-basketball-badminton-".

#  9. Start with an array of hashes and find the hash with the shortest name (from the :name key).
#     For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes {name: "book", price: 4}.

# 10. Start with an array of numbers and compute the maximum number.
#     For example, [5, 10, 8, 3] becomes 10.

# SOLUTIONS (using while loop): https://gist.github.com/peterxjang/376c8931a48549889eb3c9bc091e9f43
# SOLUTIONS (using .each shortcut): https://gist.github.com/peterxjang/379c9945774f51027750c59d6e4395df
# SOLUTIONS (using .reduce shortcut): https://gist.github.com/peterxjang/b69183e2d555964ce3936893f423ef35

#  1. Convert an array of arrays into a hash.
#     For example, [[1, 3], [8, 9], [2, 16]] becomes {1 => 3, 8 => 9, 2 => 16}.

#  2. Convert an array of hashes into a hash using the :id key from the array's hashes as the keys in the new hash.
#     For example, [{id: 1, color: "blue", price: 32}, {id: 2, color: "red", price: 12}] becomes {1 => {id: 1, color: "blue", price: 32}, 2 => {id: 2, color: "red", price: 12}}.

#  3. Convert a string into a hash with keys for each letter in the string and values for the number of times the letter appears in the string.
#     For example, "bookkeeper" becomes {"b" => 1, "o" => 2, "k" => 2, "e" => 3, "p" => 1, "r" => 1}.

#  4. Convert a hash into an array of arrays.
#     For example, {"chair" => 100, "book" => 14} becomes [["chair", 100], ["book", 14]].

#  5. Convert a hash into an array of hashes using the keys from each hash as the :id key in each of the array's hashes.
#     For example, {321 => {name: "Alice", age: 31}, 322 => {name: "Maria", age: 27}} becomes [{id: 321, name: "Alice", age: 31}, {id: 322, name: "Maria", age: 27}].

#  6. Convert an array of strings into a hash with keys for each string in the array and values for the number of times the string appears in the array.
#     For example, ["do", "or", "do", "not"] becomes {"do" => 2, "or" => 1, "not" => 1}.

#  7. Convert a hash into a flat array containing all the hash???s keys and values.
#     For example, {"a" => 1, "b" => 2, "c" => 3, "d" => 4} becomes ["a", 1, "b", 2, "c", 3, "d", 4].

#  8. Combine data from a hash with names and prices and an array of hashes with names, colors, and weights to make a new hash.
#     For example, {"chair" => 75, "book" => 15} and [{name: "chair", color: "red", weight: 10}, {name: "book", color: "black", weight: 1}] becomes {"chair" => {price: 75, color: "red", weight: 10}, "book" => {price: 15, color: "black", weight: 1}}.

#  9. Convert an array of hashes into a hash of arrays, using the author as keys and the titles as values.
#     For example, [{author: "Jeff Smith", title: "Bone"}, {author: "George Orwell", title: "1984"}, {author: "Jeff Smith", title: "RASL"}] becomes {"Jeff Smith" => ["Bone", "RASL"], "George Orwell" => ["1984"]}.

# 10. Given a hash, create a new hash that has the keys and values switched.
#     For example, {"a" => 1, "b" => 2, "c" => 3} becomes {1 => "a", 2 => "b", 3 => "c"}.

# SOLUTIONS: https://gist.github.com/peterxjang/216a7a6e8411ee5c05118e78022f2bc7

#  1. Use a nested loop to convert an array of number pairs into a single flattened array.
#     For example, [[1, 3], [8, 9], [2, 16]] becomes [1, 3, 8, 9, 2, 16].

#  2. Use a nested loop with two arrays of strings to create a new array of strings with each string combined.
#     For example, ["a", "b", "c"] and ["d", "e", "f", "g"] becomes ["ad", "ae", "af", "ag", "bd", "be", "bf", "bg", "cd", "ce", "cf", "cg"].

#  3. Use a nested loop with one array of strings to create a new array that contains every combination of each string with every other string in the array.
#     For example, ["a", "b", "c", "d"] becomes ["ab", "ac", "ad", "ba", "bc", "bd", "ca", "cb", "cd", "da", "db", "dc"].

#  4. Use a nested loop to find the largest product of any two different numbers within a given array.
#     For example, [5, -2, 1, -9, -7, 2, 6] becomes 63.

#  5. Use a nested loop to compute the sum of all the numbers in an array of number pairs.
#     For example, [[1, 3], [8, 9], [2, 16]] becomes 39.

#  6. Use a nested loop with two arrays of numbers to create a new array of the sums of each combination of numbers.
#     For example, [1, 2] and [6, 7, 8] becomes [7, 8, 9, 8, 9, 10].

#  7. Use a nested loop with an array of numbers to compute an array with every combination of products from each number.
#     For example, [2, 8, 3] becomes [4, 16, 6, 16, 64, 24, 6, 24, 9].

#  8. Use a nested loop to find the largest sum of any two different numbers within an array.
#     For example, [1, 8, 3, 10] becomes 18.

#  9. Use nested loops with an array of numbers to compute a new array containing the first two numbers (from the original array) that add up to the number 10. If there are no two numbers that add up to 10, return false.
#     For example, [2, 5, 3, 1, 0, 7, 11] becomes [3, 7].

# 10. Use a nested loop to convert an array of string arrays into a single string.
#     For example, [["a", "man"], ["a", "plan"], ["a", "canal"], ["panama"]] becomes "amanaplanacanalpanama".

# SOLUTIONS: https://gist.github.com/peterxjang/af8985dc4fb07ea14b4bd6ba41cb08f8
