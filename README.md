Smart Playlist Intelligence System

About the Project:
This program analyzes a playlist by checking the duration of songs (in seconds).
Based on certain conditions, it categorizes the playlist and gives a suitable recommendation.

The playlist can be classified as:
Too Short
Too Long
Repetitive
Balanced
Irregular
Premium Structured Playlist (Personalized)

🧠 Problem Understanding:
The task is to take a list of song durations and check whether the playlist is valid and well-structured. The program calculates total duration, checks for repetition, and categorizes the playlist accordingly. It also applies a personalized rule based on my register number.

⚙️ Logic Used:
Take song durations as input (space separated).
Check if any duration is less than or equal to 0 → mark as Invalid.

Calculate:
Total duration using sum()
Number of songs using len()
Apply conditions in order:
If number of songs is divisible by 9 → Premium Structured Playlist (Personalized rule)
If total < 300 → Too Short
If total > 3600 → Too Long
If repeated durations exist → Repetitive
If valid and balanced → Balanced
Otherwise → Irregular

Personalization Applied:

Last digit of my Register Number = 9

Personalized Logic:
If the total number of songs is divisible by 9,
the playlist is categorized as Premium Structured Playlist.

This rule makes the solution personalized based on my register number.

🧪 Test Cases:
✅ Case 1 – Balanced Playlist

Input:

180 200 220 210

Expected Output:

Total Duration: 810 seconds
Songs: 4
Category: Balanced Playlist
Recommendation: Good listening session

✅ Case 2 – Repetitive Playlist

Input:

120 120 150

Expected Output:

Total Duration: 390 seconds
Songs: 3
Category: Repetitive Playlist
Recommendation: Add variety

✅ Case 3 – Personalized Rule Applied

Input:

100 200 300 400 500 600 700 800 900

Expected Output:

Total Duration: 4500 seconds
Songs: 9
Category: Premium Structured Playlist
Recommendation: Highly organized listening pattern

📚 Learning Outcome:
Through this challenge, I learned how to:
Work with lists in Python
Validate user input
Use inbuilt functions like sum(), len(), count()
Apply logical conditions in a structured way
Add personalized logic to a program
