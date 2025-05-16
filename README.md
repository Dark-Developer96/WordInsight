📚 WordInsight
WordInsight is a Python command-line tool that analyzes a text file to provide word frequency statistics. It filters out common stop words and allows users to interactively explore the top words, search for word counts, visualize the data, and find words of a specific length.

🚀 Features
✅ Reads a text file and processes its words.

✅ Removes punctuation and common stop words.

✅ Displays the top 10 most frequent words.

✅ Allows you to search for any word and get its frequency.

✅ Visualizes the top 10 words in a bar graph using matplotlib.

✅ Lists all words of a specific character length.

🧾 Requirement
Python 3.6+

matplotlib (install via pip)

bash
Copy
Edit
pip install matplotlib
📁 Usage
Save your script (e.g., wordinsight.py) and place your .txt file in the same directory.

Run the script:

bash
Copy
Edit
python wordinsight.py
Enter the filename when prompted (e.g., sample.txt).

Use the menu to explore the data.

📌 Menu Options
Option	Description
1	Show the top 10 most frequent words
2	Search for a specific word's frequency
3	View a bar graph of the top 10 words
4	List all words of a specific length
0	Exit the program

🧹 Stop Words Filtered
Words like the, a, is, to, in, etc., are automatically removed from analysis for better insights.

📊 Example Output
bash
Copy
Edit
Welcome to WordInsight
Enter 1 to get the top 10 most appeared words
Enter 2 to search a word and get its number of appearance
Enter 3 to show a graphical representation of top 10 words
Enter 4 to check all the words of a specific length
Enter 0 to exit
📦 File Structure
bash
Copy
Edit
project-folder/
│
├── wordinsight.py     # Main Python script
├── sample.txt         # Your input text file
└── README.md          # Project documentation
📌 Notes
Make sure the file exists in the same directory or provide the full path.

Words are case-insensitive (all converted to lowercase).

Punctuation is removed before analysis.

🧑‍💻 Author
Made with ❤️ using Python
