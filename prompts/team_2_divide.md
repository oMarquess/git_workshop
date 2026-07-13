# Git Conflict Workshop - Team 2: Division

Your team has been assigned to add the **division** feature to the shared calculator utility.

### Task Instructions
1. **Create Branch**: Create and switch to your feature branch:
   ```bash
   git checkout -b feature/divide
   ```
2. **Implement Code**:
   Modify `calculator.py`. Locate the instruction comment `# [INSTRUCTION] Teams: Add your new operations directly below this line!` and add the `divide` operation directly below it (raise a `ValueError` if the denominator `b` is `0`):
   ```python
   elif op == "divide":
       if b == 0:
           raise ValueError("Cannot divide by zero")
       return a / b
   ```
3. **Add Tests**:
   Modify `test_calculator.py`. Locate the instruction comment `# [INSTRUCTION] Teams: Add your test cases directly below this line!` and add your unit test methods:
   ```python
   def test_divide(self):
       self.assertEqual(calculate("divide", 8, 2), 4)

   def test_divide_by_zero(self):
       with self.assertRaises(ValueError):
           calculate("divide", 5, 0)
   ```
4. **Verify Locally**:
   Run the tests locally to verify your code behaves correctly:
   ```bash
   python -m unittest test_calculator.py
   ```
5. **Commit & Push**:
   Commit your changes and push the branch to the remote repository:
   ```bash
   git add calculator.py test_calculator.py
   git commit -m "feat: add division operation and tests"
   git push origin feature/divide
   ```
6. **Open Pull Request**: Open a PR from `feature/divide` to `main`.
