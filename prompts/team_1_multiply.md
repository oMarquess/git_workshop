# Git Conflict Workshop - Team 1: Multiplication

Your team has been assigned to add the **multiplication** feature to the shared calculator utility.

### Task Instructions
1. **Create Branch**: Create and switch to your feature branch:
   ```bash
   git checkout -b feature/multiply
   ```
2. **Implement Code**:
   Modify `calculator.py`. Locate the instruction comment `# [INSTRUCTION] Teams: Add your new operations directly below this line!` and add the `multiply` operation directly below it:
   ```python
   elif op == "multiply":
       return a * b
   ```
3. **Add Tests**:
   Modify `test_calculator.py`. Locate the instruction comment `# [INSTRUCTION] Teams: Add your test cases directly below this line!` and add your unit test method:
   ```python
   def test_multiply(self):
       self.assertEqual(calculate("multiply", 3, 4), 12)
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
   git commit -m "feat: add multiplication operation and test"
   git push origin feature/multiply
   ```
6. **Open Pull Request**: Open a PR from `feature/multiply` to `main`.
