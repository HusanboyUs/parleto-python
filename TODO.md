1. SETUP PROJECT

   Requirements:
   - python >= 3.10
   - django >= 4
   - sqlite
   
   python manage.py migrate
   python manage.py loaddata fixtures.json

2. Create git repository and add all files.
3. Create new branch in format `firstName-lastName`.
4. TASKS

   1. In `expenses.ExpenseList` allow searching by date (from and/or to).                      -done
   2. In `expenses.ExpenseList` allow searching by multiple categories.                        -done
   3. In `expenses.ExpenseList` add sorting by category or date (ascending and descending)     -done
   4. In `expenses.ExpenseList` add total amount of money spent.                               -done
   5. In `expenses.ExpenseList` add table with total summary per year-month.                   -done
   6. Add update view for `expenses.Category`.                                                 -done
   7. Add number of expenses per category row in category list.

5. By the end of seventh calendar day (even if it is incomplete), please:
   1. Commit all changes.
   2. Create patch using git with filename in format `firstName-lastName.patch`.
   3. Make sure patch contains only source code you have added/changed.
   4. Send us only patch file.
