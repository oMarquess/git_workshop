# Git Conflict Workshop - Team 3: Exponentiation (Power)

Your team has been assigned to add the **exponentiation (power)** feature to the shared calculator utility.

### Task Instructions
1. **Create Branch**: Create and switch to your feature branch:
   ```bash
   git checkout -b feature/power
   ```
2. **Implement Code**:
   Modify `calculator.py`. Locate the instruction comment `# [INSTRUCTION] Teams: Add your new operations directly below this line!` and add the `power` operation directly below it:
   ```python
   elif op == "power":
       return a ** b
   ```
3. **Add Tests**:
   Modify `test_calculator.py`. Locate the instruction comment `# [INSTRUCTION] Teams: Add your test cases directly below this line!` and add your unit test method:
   ```python
   def test_power(self):
       self.assertEqual(calculate("power", 2, 3), 8)
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
   git commit -m "feat: add power operation and test"
   git push origin feature/power
   ```
6. **Open Pull Request**: Open a PR from `feature/power` to `main`.
