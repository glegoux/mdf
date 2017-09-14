# Competition "Meilleur Dev de France"

[![Build Status](https://travis-ci.org/glegoux/mdf.svg?branch=master)](https://travis-ci.org/glegoux/mdf)

![alt text][mdf]

## Description

Several short exercices to train its capacity to code with a limit of time.  

See at http://www.meilleurdevdefrance.com/ for more details. It is a yearly French programming competition to elect the best developer. See statements of the coding contest 2016 at http://www.isograd.com/EN/contestsolution.php.  

* The 2016 competition is availabe with my solution in Python 3.
This competition have sessions (first round, session1 or session2 with 3 exercices) then the final (final round with 2 exercices). 
Each round lasts 45 minutes.  

* The 2014 and 2015 competition are availabe with my solution in Python 3.
These competitions have 7 exercices and last 1 hour and 30 minutes.  

Each exercice matches to a folder that contains :
- `answer.py`      : your response with a script in Python 3.  
- `direction.png`  : the statements of the current exercise.  
- `input<i>.txt`   : a test from stdin.  
- `output<i>.txt`  : the expected result for `input<i>.txt`.  

* The 2013 competition is not found :(!

## Usage

Here an example of output after executing the script `./launch` (see **6.** ) :

![alt text][example]

We can write your own solution. If you have a Bourne Shell, do the following statements :

**1.** Choose your session (for instance go to `2014/`).  

**2.** Clean in running the script `./clean` to have each exercise without my solution.  

**3.** Choose the first exercise (here `ex1-trivial-pursuit/`).

**4.** Read the direction thanks to the picture `direction.png`  
(or here https://github.com/glegoux/mdf/blob/master/2014/README.md).  

**5.** Write your solution in editing the file `answer.py` in **Python 3**.

**6.** Run your exercise(s) in ascending order with the script `./launch` in the current session (here `2014/`).

**7.** If your results are correct for each `input<i>.txt`, you can go to the next exercise.

*Note :*
- The directions are in french because of it's a french competition.
- You can put your tracks with the function `local_print()` directly. It creates a file `track<i>.txt` for each `input<i>.txt` for the current exercise, if you want to see your tracks again after running.    
In reality, when you are executing `./launch`, `main.py` is running instead of `answer.py`, see `bin/` folder.  
- You can use the script `./edit`, if you want read and/or edit all exercises of the current session.
- You can run the current exercise with a test `input<i>.txt` directly with the command `./answer.py < input<i>.txt`, but without using `local_print` function. This allows to do the exercises in any order, because the script `./launch` runs the exercises in ascending order, and stop as soon as an error (false reponse or syntax error ...) is found.
- For each exercise, my solution is not the most efficient and relevant for performance. The goal of this competition is to find the solution the most quick to write, no always the most smart. 


## Test and Continous Integration

This project uses Travis CI, see `./test/test.sh`.

[example]: https://github.com/glegoux/mdf/blob/master/example.png "example"
[mdf]: https://github.com/glegoux/mdf/blob/master/mdf.png "mdf"
