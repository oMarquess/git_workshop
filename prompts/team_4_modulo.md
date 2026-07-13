# Git Conflict Workshop - Team 4: Modulo

Your team has been assigned to add the **modulo** feature to the shared calculator utility.

### Task Instructions
1. **Create Branch**: Create and switch to your feature branch:
   ```bash
   git checkout -b feature/modulo
   ```
2. **Implement Code**:
   Modify `calculator.py`. Locate the instruction comment `# [INSTRUCTION] Teams: Add your new operations directly below this line!` and add the `modulo` operation directly below it (raise a `ValueError` if `b` is `0`):
   ```python
   elif op == "modulo":
       if b == 0:
           raise ValueError("Cannot modulo by zero")
       return a % b
   ```
3. **Add Tests**:
   Modify `test_calculator.py`. Locate the instruction comment `# [INSTRUCTION] Teams: Add your test cases directly below this line!` and add your unit test methods:
   ```python
   def test_modulo(self):
       self.assertEqual(calculate("modulo", 7, 3), 1)

   def test_modulo_by_zero(self):
       with self.assertRaises(ValueError):
           calculate("modulo", 5, 0)
   ```
4. **Verify Locally**:
   Run the tests locally to verify your code behaves correctly:
   ```bash
   git add calculator.py test_calculator.py
   python -m unittest test_calculator.py
   ```
5. **Commit & Push**:
   Commit your changes and push the branch to the remote repository:
   ```bash
   git commit -m "feat: add modulo operation and tests"
   git push origin feature/modulo
   ```
6. **Open Pull Request**: Open a PR from `feature/modulo` to `main`.
