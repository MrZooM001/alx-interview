***Project:***  **0x0A. Prime Game**<br />
***Scope:***  ` Algorithm ` ` Python `<br />
## ***Task***
**<h4>Description</h4>**
For this project, you will need to leverage your understanding of prime numbers, game theory, and algorithm optimization to solve a competitive game scenario. The challenge involves determining the winner of a game based on the strategic removal of prime numbers and their multiples from a set of consecutive integers.

<h1>Concepts Needed:</h1>
<ol>
    <li><b>Prime Numbers:</b>
        <ul>
            <li>Understanding what prime numbers are.</li>
            <li>Efficient algorithms for identifying prime numbers within a range.</li>
        </ul>
    </li>
    <li><b>Sieve of Eratosthenes:</b>
        <ul>
            <li>An efficient algorithm for finding all prime numbers up to any given limit, which can be particularly useful for this task.</li>
        </ul>
    </li>
    <li><b>Game Theory:</b>
        <ul>
            <li>Basic principles of competitive games where players take turns and the concept of optimal play.</li>
            <li>Understanding win conditions and strategies that lead to a win or loss.</li>
        </ul>
    </li>
    <li><b>Dynamic Programming/Memoization:</b>
        <ul>
            <li>Using previous results to make future calculations faster, potentially necessary for optimizing the solution for multiple rounds of the game.</li>
        </ul>
    </li>
    <li><b>Python Programming</b>:
        <ul>
            <li>Loops and conditional statements for implementing game logic and algorithms.</li>
            <li>Arrays and lists for storing the integers and tracking removed numbers.</li>
        </ul>
    </li>
</ol>

<h1>Resources:</h1>
<ol>
    <li><b>Prime Numbers and Sieve of Eratosthenes:</b>
        <ul>
            <li><a href="https://intranet.alxswe.com/rltoken/IUKEfGVroNza8u37x0lEzw">Khan Academy: Prime Numbers:</a> Introduction to prime numbers.</li>
            <li><a href="https://intranet.alxswe.com/rltoken/sVjdrNQEaErO_qRYsVMTEg">Sieve of Eratosthenes in Python:</a> A step-by-step guide to implementing the sieve algorithm in Python.</li>
        </ul>
    </li>
</ol>

**<h1>Tasks</h1>**
## **0. Prime Game**

Maria and Ben are playing a game. Given a set of consecutive integers starting from `1` up to and including `n`, they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game.

They play `x` rounds of the game, where `n` may be different for each round. Assuming Maria always goes first and both players play optimally, determine who the winner of each game is.


• Prototype: `def isWinner(x, nums)` <br />
• where `x` is the number of rounds and `nums` is an array of `n` <br />
• Return: name of the player that won the most rounds <br />
• If the winner cannot be determined, return `None` <br />
• You can assume `n` and `x` will not be larger than 10000 <br />
• You cannot import any packages in this task <br />

Example:

`x` = `3`, `nums` = `[4, 5, 1]`

First round: `4`

• Maria picks 2 and removes 2, 4, leaving 1, 3 <br />
• Ben picks 3 and removes 3, leaving 1 <br />
• Ben wins because there are no prime numbers left for Maria to choose <br />

Second round: `5`

• Maria picks 2 and removes 2, 4, leaving 1, 3, 5 <br />
• Ben picks 3 and removes 3, leaving 1, 5 <br />
• Maria picks 5 and removes 5, leaving 1 <br />
• Maria wins because there are no prime numbers left for Ben to choose <br />

Third round: `1`

• Ben wins because there are no prime numbers for Maria to choose <br />
• Result: Ben has the most wins <br />

**Result: Ben has the most wins**
```bash
carrie@ubuntu:~/0x0A-primegame$ cat main_0.py
#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner


print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))

carrie@ubuntu:~/0x0A-primegame$
```
<br />

```bash
carrie@ubuntu:~/0x0A-primegame$ ./main_0.py
Winner: Ben
carrie@ubuntu:~/0x0A-primegame$
```

## ***Solution***
* **[0. Prime Game](0-prime_game.py)**
