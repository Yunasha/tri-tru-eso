# tri-tru-eso
## Esolang

Tri-tru-eso is a esolang with one goal in mind: to allow all keyboard sizes to code. Let me elaborate

## Why?
Keyboard is an essential part of a computer. Because of that, it is packed with features to allow users to do all tasks with ease.
But then, computers became more available to average households. Then the need for feature-packed keyboards started to vanish as people didn't really need all of the keys on them.

So, keyboards started to shrink and shrink.
- F13 - F24 got killed
- Numpad followed
- Home, end, page up, and page down
- Insert, delete, print screen, scroll lock, pause, and break
- F1 - F12 fell victim

And soon, more will fall
all of the symbols... all of the numbers...
everyone has _tabbed_ out. There is no _escape_, I have no _control_. I can't _shift_ the balance back to what it was. There is no _alternative_ either. Only screaming and letters left.

This esolang is my response to this growing trend. I want to make sure that all people can code, regardless of their keyboard size. And I've done it in a more artistic way, inspired by Assembly and BASIC. I've managed to create a one-of-a-kind esolang, a masterpiece of a language. It's simple, easy to understand, symmetric, and consistent, not straining for the eyes.

# Guide

## Keywords
| Key | Action |
|-----|--------|
| `OUT` | Output variable, string, or number |
| `RED` | Input string, or number to a variable |
| `VAR` | Declare a variable |
| `TXT` | Indicate a sting |
| `NUM` | Indicate a number |
| `END` | End the program |
| `ENL` | Mark an end of line |
| `NWL` | Mark a new line for string |
| `FLG` | Create a flag |
| `JPT` | Jump to a flag |
| `JPP` | Jump to a flag if positive |
| `JPN` | Jump to a flag if negative |
| `SPC` | additional space for string |
| `ADD` | Perform an addition between two variables |
| `SUB` | Perform a subtraction between two variables |
| `MUL` | Perform a multiplication between two variables |
| `DIV` | Perform a division between two variables |
| `MOD` | Perform a modulo between two variables |
| `CPY` | Copy a value of a variable to another variable |

## Numbers
| Key | Number |
|-----|--------|
| `ZRO` | 0 |
| `ONE` | 1 |
| `TWO` | 2 |
| `THR` | 3 |
| `FUR` | 4 |
| `FVE` | 5 |
| `SIX` | 6 |
| `SVN` | 7 |
| `EGH` | 8 |
| `NNE` | 9 |
| `NEG` | - |

## Syntax

all key and names must be 3 characters long. no more, no less. This include the string and number

- `argument` without paranthesis is optional
- `[argument]` with paranthesis is required
- `[argument 1 | argument 2]` with `|` is option
- `ADD` `SUB` `MUL` `DIV` `MOD` `CPY` will save the result to the first variable

| Key | Syntax |
|-----|--------|
| `OUT` | `[OUT]` `[TXT \| NUM \| VAR]` `[VALUE \| VARIABLE NAME]` |
| `RED` | `[RED]` `[TXT \| NUM]` `[VARIABLE NAME]` `MESSAGE` |
| `VAR` | `[VAR]` `[TXT \| NUM]` `[VALUE]` |
| `FLG` | `[FLG]` `[FLAG NAME]` |
| `JPT` | `[JPT]` `[FLAG NAME]` |
| `JPP` | `[JPP]` `[FLAG NAME]` `[TARGET VARIABLE]` |
| `JPN` | `[JPN]` `[FLAG NAME]` `[TARGET VARIABLE]` |
| `ADD` | `[ADD]` `[FIRST VARIABLE]` `[SECOND VARIABLE]` |
| `SUB` | `[SUB]` `[FIRST VARIABLE]` `[SECOND VARIABLE]` |
| `MUL` | `[MUL]` `[FIRST VARIABLE]` `[SECOND VARIABLE]` |
| `DIV` | `[DIV]` `[FIRST VARIABLE]` `[SECOND VARIABLE]` |
| `MOD` | `[MOD]` `[FIRST VARIABLE]` `[SECOND VARIABLE]` |
| `CPY` | `[CPY]` `[SOURCE VARIABLE]` `[TARGET VARIABLE]` |

You can find all example in `.\example\`
