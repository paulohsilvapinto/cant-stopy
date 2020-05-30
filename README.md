# Cant-Stopy

## About

Can't-Stopy is a Python implementation of a board game called Can't Stop. It was built using Python 3.8.3

![Can't Stop original board](/images/board.png)

You can play it by cloning this repository and running on a terminal:

    > cd PATH\TO\THE\GAME
    > python main.py

**Hope you enjoy it!**

## Game Rules

### Goal

The goal of this game is to “claim” three of the game board’s numbered columns. You claim a column if you can move one of your cubes from the bottom of that column to the top, according to the rules of the game. As soon as any player claims three columns, they win the game.

### On your turn

Your goal during your turn is to advance as far as you can **up to one, two, or three columns.** After every roll you’ll need to decide whether to **stop and keep your progress, or try to advance even further – at the risk of losing your progress.**

### Rolling

Roll all four dice, then combine them into two pairs, any way you wish.
**Example**
If you roll 3, 4, 2, 6, then you can make these combinations:
    * 3+4 and 2+6 (7 and 8)
    * 3+2 and 4+6 (5 and 10)
    * 3+6 and 4+2 (9 and 6)
(Yes, if you roll doubles / triples / quadruples, you’ll have fewer combinations to choose from.)

Having thus chosen two sums between 2 and 12, you will advance in those columns, according to these rules:
    * If you have already advanced this turn in that column (on an earlier roll during this same turn), advance it one space.
    * If you have not already advanced this turn in that column, advance in that column following these rules:
        * If you have advanced in that column on a previous turn, start advancing one space ahead of your last position.
        * Otherwise, start advancing from the bottom space of that column.

Other players’ cubes, if already on a space, can share that space with other players.

Once you advance in a column, you cannot undo your advancement in that column.

As the game progresses, you’ll often find that you can only legally make one move, rather than two. This is OK. However, you must always play to as many columns as your roll allows; you can’t choose to ignore a dice that allow a legal move.

If your roll allows it, you can play twice in a single column. For example, if you roll 2, 4, 4, 6, you could make two
moves in column 8 (4+4 and 2+6), if available.

### Going bust

To continue your turn, you **must use at least one dice pair** to advance on the board, according to the rules above.

**If you cannot legally advance** on any column using your roll, either because the columns you rolled are already claimed or because you cannot choose another column anymore (if you've already chosen three different columns)**, you have gone bust. You do not get to advance on this turn.** Your turn’s over.

### Choosing to stop

After you finish advancing, you can choose to end your turn, or roll again. If you choose to end your turn, you will persist your progress and the next player start his turn.

**Each player can keep playing and rolling as much as they want until they either go bust or choose to stop.**

### Claiming a column

If you have moved onto a column’s top space when you choose to end your turn, then you have claimed that column.
This column now is blocked and **no one can move on this column anymore**. For the rest of the game, that column’s number has effectively ceased to exist.

**If you end your turn with three columns claimed, then you have won the game!**
