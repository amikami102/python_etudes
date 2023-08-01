# Python études

This repository holds my Python practice codes except for the yearly set of solutions to Advent of Code, which are stored in [a separate repository](https://github.com/amikami102/AdventOfCode). The folders are named after websites and books from which the exercises are taken. 

I do these exercises in [Thonny](https://thonny.org/), which I love for having the right amount of minimal interface and supports the latest version of Python interpreter unlike [Mu Editor](https://codewith.mu/).

## [Python morsels](https://www.pythonmorsels.com) by Trey Hunner

(Currently active since 2021)

I've been subscribed to Python morsels since 2020 except for a brief pause in 2021. I owe to Trey Hunner's Python Morsels for improving my coding skills and knowledge of Python (and non-Python specific) concepts such as iterators and duck typing. Even though all of my solutions to the exercises I've solved are saved on my Python morsels account and I don't really need to keep them on file, I find a lot of code used in the solutions very helpful. I've even used some of them in real life (and for solving other exercises in this repository).


## [*Classic Computer Science Problems in Python*](https://www.manning.com/books/classic-computer-science-problems-in-python) by David Kopec

(Finished in June 2023)

The scripts in this folder are refactored versions of Kopec's codes and include solutions to some of the end-of-the-chapter exercises.

I think this is a good book for non-computer science, intermediate-level Python learners to practice writing Python. Kopec's code only uses the standard libraries even for implementation of k-means clustering and neural network (obviously not recommended for actual use). There is a lot of refactoring you can do to make the code more up to date (especially with the recent update on `typing` module) and Pythonic (e.g. constructing lists with comprehension instead of `for` loop). I can't speak for the computer science side of this book, but I found it accessible and enough to give me a foothold to read the next level of material.

## [Object-Oriented Python: Master OOP by Building Games and GUIs](https://nostarch.com/object-oriented-python) by Irv Kalb

(Finished in June 2023)

I ended up skimming this book because it turns out I knew ninety-nine percent of the material already. The most valuable portion of the book was the first few chapters showing what procedural (as opposed to object oriented) programming looks like and how they break down as you try to add more layers of complexity. (It turns out procedural programming is the kind of Python code my coworkers were writing.) What was left for me to gain from the rest of the book was the abstract concepts and the design philosophy behind OOP. 

I wouldn't recommend picking up this book to learn the nuts and bolts of doing OOP in Python. You'll naturally learn the pragmatics if you bother to study beyond the basics, for which I highly recommend Python Morsels (not sponsored).

## [Automate the Boring Stuff with Python: Practical Programming for Total Beginners](https://automatetheboringstuff.com/) by Al Sweigart 

(Finished July 2023)

The subtitle says the book is for total beginners, and that pretty much completes my review of the book. 

This textbook is very beginner-friendly: it's good if *and only if* you've never written a line of code before. Al Sweigart will hold your hand line-by-line and shield your eyes from any details that will go over a novice's head at this level. With that said, a lot of the code in this book is not Pythonic, so beginners should consider other resources to brush up their skills.

I was looking forward to part 2 where the chapters get more task-specific in hopes of finding something for more intermediate learners. Unfortunately, most of them ended up reading like Medium articles that you can google online. If you're a Python beginner or new to programming automation, I would recommend the chapters on regular expression (ch.7); file management (ch.10); working with file-like objects (ch.9 and parts of other chapters that deal with specific types of files) and webscraping (ch. 12) although Sweigart omits to mention the fuzzy ethicality and legality surrounding this practice. 

