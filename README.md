# CSA0805-1924260165-Assignment1

**Name:** Dev Narayan E
**Register number:** 1924260165
**Python version:** 3.15
**Libraries:** Python standard-library modules are listed in
`requirements.txt`. No third-party packages are required.

The full analysis, pseudocode, diagrams, complexity comparisons, tests and
measured evidence for all tasks are in [Assignment_Report.md](Assignment_Report.md).
Task folders contain the runnable code, sample inputs where applicable,
captured console output text, and PNG images of the captured outputs.

## Tasks

| Task | Run command | Result |
|---|---|---|
| 1 – Problem analysis | `python Task_1\task1.py` | Shows input fields, their types, constants and validation limits. |
| 2 – Values and types | `python Task_2\task2.py` | Demonstrates Python types, division, float error, Decimal, integer paise and object sizes. |
| 3 – Variables and constants | `python Task_3\task3.py` | Demonstrates named constants, dynamic typing, multiple assignment and swapping. |
| 4 – Expressions | `python Task_4\task4.py` | Demonstrates quality-step calculation, precedence, rounding and negative division. |
| 5 – Input conversion | `cmd /c "python Task_5\task5.py < Task_5\sample_input.txt"` | Validates and formats one sample milk entry. |
| 6 – Functions | `python Task_6\task6.py` | Calculates rates, payments and a Decimal ten-day total. |
| 7 – Module | `python Task_7\milkrate.py` then `python Task_7\task7.py` | Shows direct module execution and a separate module import. |
| 8 – Algorithm | `python Task_8\task8.py` | Prints the hand trace and running total for three entries. |
| 9 – Calculator and tests | `python -m Task_9.test_task9` | Runs assertion-based positive, boundary and invalid-input tests. |
| 9 – Sample calculator run | `cmd /c "python -m Task_9.calculator < Task_9\sample_input.txt"` | Calculates five entry payments; ten-day total is Rs 1,345.50. |
| 10 – Execution comparison | `python Task_10\task10.py` | Compares float/Decimal at three scales and measures cached rates. |
| 11 – Final recommendation | `python Task_11\task11.py` | Prints the selected production design. |
| 12 – Seasonal design | `python Task_12\task12.py` | Verifies regular/seasonal rates and the >500 L bonus. |

Production payment calculations use `Decimal` constructed from decimal text
and round to paisa using `ROUND_HALF_UP`; float calculations appear only in
the comparison tasks. Timings in Task 10 are specific to the machine and run;
see the report and `Task_10\output.txt`.

Repository link: https://github.com/devnarayan922009-sys/CSA0805-1924260165-Assignment1
