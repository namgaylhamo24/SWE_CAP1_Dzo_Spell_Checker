# Dzongkha Spell Checker

## Project Overview
A Dzongkha Spell Checker checks if Dzongkha words are spelled correctly and suggests fixes for mistakes. It helps users write Dzongkha more accurately by using a quick dictionary and correction tools.
## Table of Contents
- [Usage]
- [Implementation Details]
- [Data Structures]
- [Algorithms]
- [Performance Analysis]
- [Challenges and Solutions]
- [Future Improvements]
- [References]

## Usage
-In schools and colleges, the Dzongkha spell checker helps students and teachers keep spelling accurate in assignments and exams, promoting standardization in educational materials.

-The Dzongkha spell checker is built into word processors and software, helping users write error-free in digital platforms, websites, and mobile apps.

-Dzongkha spell checking helps modern communication while preserving the traditional spelling of the language. It provides access only when necessary.


```bash
python dzongkha_spell_checker.py input_file.txt
 ```

## Implementation Details
-Downloaded dictionary.docx file from the given link and converted .docx to .txt file from the convertion website.

-Filtered the english word from .txt file and generated new output .txt file with their line numbers.

## Data Structure
- Set: Stores a multiple items in a single variable.
- List: stores individual words extracted from the input file.
- Tuples: Keeps track of misspelled words along with their corresponding line numbers for structured error reporting.

## Algorithms
- It reads each line of the input file and breaks it into words using punctuation and checks it against the dictionary.txt file.

## Performance Analysis  
The Dzongkha spell checker works well for small to medium-sized files. Using a set for dictionary lookups allows it to check each word very quickly, even in larger files.

## Challenges Faced
- Unicode Handling:I used utf-8 encoding to process special Dzongkha characters (་, །).
- Fast Dictionary Access:The dictionary was stored in a set for quick lookups during spell checking.
- Compound Word Detection: To manage compounded words using the ་ marker, I check word parts step by step.

**Future Improvements**
- Extended Unicode Support: Enhance support for additional Dzongkha punctuation and ligatures.
- User-Friendly Output: Provide results in a more accessible format, like highlighted files or a web interface.

## References
-Chat GPT-https://openai.com/index/chatgpt/

-W3 School-https://www.w3schools.com/

-python Document-https://docs.python.org/3/

-YouTube Videos-https://www.youtube.com/watch?v=LyymFN9t4kw&list=PPSV

-YouTube Videos-https://www.youtube.com/watch?v=IYIJmZhEiOc&list=PPSV