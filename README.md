# Git Conflict Resolution Workshop: Python Edition (Up to 4 Teams)

This directory contains the base repository code and team prompt sheets for a collaborative Git workshop. Teams of 1–4 groups will work in parallel to build features in a shared codebase, intentionally triggering merge conflicts that they must resolve collectively.

---

## Workshop Structure & Files

- **Base Code**:
  - `calculator.py`: The core implementation containing stubs.
  - `test_calculator.py`: The starting test suite.
- **Team Prompts (inside `/prompts`)**:
  - [team_1_multiply.md](file:///Users/redeemersalamiokekale/Desktop/Workspace/test-cohort/git_workshop/prompts/team_1_multiply.md): Tasked with implementing multiplication.
  - [team_2_divide.md](file:///Users/redeemersalamiokekale/Desktop/Workspace/test-cohort/git_workshop/prompts/team_2_divide.md): Tasked with implementing division (and division by zero handling).
  - [team_3_power.md](file:///Users/redeemersalamiokekale/Desktop/Workspace/test-cohort/git_workshop/prompts/team_3_power.md): Tasked with implementing exponentiation.
  - [team_4_modulo.md](file:///Users/redeemersalamiokekale/Desktop/Workspace/test-cohort/git_workshop/prompts/team_4_modulo.md): Tasked with implementing modulo (and modulo by zero handling).

---

## Step-by-Step Facilitator Playbook

### Phase 1: Preparation (10 mins)
1. **Create the Central Repo**:
   * Create a blank repository on GitHub or GitLab (e.g., `git-conflict-workshop`).
   * Add the base files (`calculator.py` and `test_calculator.py`) to the repository's `main` branch.
2. **Add Collaborators**:
   * Add all workshop participants as contributors/collaborators to the repository so they have push rights.
3. **Distribute Prompts**:
   * Divide participants into 4 groups.
   * Send each group their corresponding prompt file from the `prompts/` directory.

---

### Phase 2: Branching & Development (15 mins)
* Teams will clone the repository:
  ```bash
  git clone <repository-url>
  ```
* They will follow their prompt instructions to:
  * Create their branch (`feature/multiply`, `feature/divide`, etc.).
  * Insert their operation logic and unit tests at the specified comment placeholders.
  * Run tests locally using `python -m unittest test_calculator.py`.
  * Commit and push their branch, and open a Pull Request (PR) to `main`.

---

### Phase 3: The Merging Sequence (25 mins)

Here is where the magic (and learning) happens. Instruct the teams to merge their PRs **one at a time** in the following order:

#### 1. Merge Team 1 (`feature/multiply`)
* **Result**: Clean merge. Since it is the first PR, it merges automatically.
* **Instruction**: Approve and merge it in the GitHub/GitLab UI.

#### 2. Merge Team 2 (`feature/divide`)
* **Result**: **Merge Conflict!** Both Team 1 and Team 2 edited the same lines in `calculator.py` and `test_calculator.py`.
* **Action Plan**:
  * Tell Team 2 they must resolve this conflict.
  * In their local terminal, Team 2 runs:
    ```bash
    git checkout feature/divide
    git fetch origin
    git merge origin/main
    ```
  * In their editor, Team 2 will see conflict markers. They must combine both `multiply` and `divide` operations, keeping correct Python syntax/indentation, and combine both tests.
  * **Test Check**: Team 2 runs `python -m unittest test_calculator.py` to make sure it passes.
  * **Commit & Push**:
    ```bash
    git add calculator.py test_calculator.py
    git commit -m "Merge main and resolve conflict with multiply"
    git push origin feature/divide
    ```
  * Merge Team 2's PR.

#### 3. Merge Team 3 (`feature/power`)
* **Result**: **Merge Conflict!** They conflict with the merged `multiply` and `divide` changes.
* **Action Plan**:
  * Team 3 follows the same merge-resolve workflow. They must integrate `power` alongside `multiply` and `divide`.
  * Ensure they check syntax and run the tests before pushing.
  * Merge Team 3's PR.

#### 4. Merge Team 4 (`feature/modulo`)
* **Result**: **The Ultimate Conflict!**
* **Action Plan**:
  * Team 4 has to merge the combined updates from Team 1, 2, and 3 into their local branch.
  * This is a great test of patience and careful attention to Python blocks.
  * Run tests, resolve any issues, push, and merge.

---

## Cheat Sheet for Troubleshooting

* **IndentationError / SyntaxError**:
  * Since Python is whitespace-sensitive, resolving conflicts manually often breaks indentation. Emphasize running the tests (`python -m unittest test_calculator.py`) *before* committing their resolution.
* **Abort a Messy Merge**:
  * If a team gets lost in conflict markers and wants to start the merge resolution over:
    ```bash
    git merge --abort
    ```
* **Enable 3-way Diff**:
  * Instruct participants to run this beforehand to see the common ancestor version inside conflict markers:
    ```bash
    git config --global merge.conflictstyle diff3
    ```
