# Day 03 Practice Assignments: Mutable Sequences — Working with Lists

## Objective
Practice list declarations, indexing, slicing, modification methods, list operators, list comprehensions, and nested lists through interactive, scenario-based problems.

---

## Part A: Easy Complexity (3 Exercises)
Scenario: A wizard has a magic bag containing a sequence of items: ["staff", "potion", "spellbook"]. When the wizard steps through a magic portal, two things happen:

A new item enters the bag (prompts the user to input the item name to append to the end).
The oldest item in the bag (at index 0) is dissolved and ejected. Write a program to simulate this portal transition and print the final bag contents.

**Sample Input**: (User inputs "amulet")
**Sample Output**:
Portal transition activated!
Ejected oldest item: staff
Current items in the magic bag: ['potion', 'spellbook', 'amulet']

---

## Exercise 2: Movie Night Playlist

Scenario: You are organizing a movie marathon. You start with a playlist: ["Inception", "The Matrix", "Interstellar"]. Prompt the user to enter the name of a movie they want to add.

If the movie is already in the list, print "Already added!" and do not insert it.
If it is not in the list, append it to the end of the list. Finally, sort the movie list alphabetically and print the updated playlist.
**Sample Input**: "Interstellar"
**Sample Output**:
Already added!
Alphabetical Playlist: ['Inception', 'Interstellar', 'The Matrix']
**Sample Input**: "Avatar"
**Sample Output**:
Added Avatar!
Alphabetical Playlist: ['Avatar', 'Inception', 'Interstellar', 'The Matrix']

---

## Exercise 3: The Cargo Train Scanner

Scenario: A train has wagons carrying different resources: ["coal", "iron", "gold", "coal", "timber", "coal"]. The train conductor wants to inspect the cargo. Write a program that prompts the user to enter a resource type (e.g., "coal" or "gold").

Print the total number of wagons carrying that resource (using .count()).
If the resource is on the train, print the index of the very first wagon carrying it (using .index()). If it is not found, print "Resource not found on train!".
**Sample Input**: "coal"
**Sample Output**:
Number of coal wagons: 3
First coal wagon is at index: 0
**Sample Input**: "oil"
**Sample Output**: "Resource not found on train!"
