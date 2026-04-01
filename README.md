# DataLoader Debug Exercise

## Overview

In this exercise, you will debug a PyTorch DataLoader that crashes during training. One corrupted data file was accidentally added to the training set, and your task is to:

1. **Find the bug**: Identify which sample causes the crash and why
2. **Find the bad commit**: Use `git bisect` to identify when the corrupted file was introduced


## Setup

```bash
git clone <repository-url>
cd dataloader_debug
uv sync
```

Verify the problem exists:

```bash
uv run python train.py
```

You should see an error during training.



## Task 1: Identify the Bug

Run `train.py` and examine the error. Your goal is to answer:

1. Which line in `dataset.py` raises the error?
2. What is the filename of the corrupted sample?
3. Why does this file cause an error? (Hint: open the file and look at its contents)


### Debugging Strategy

Use VS Code's exception breakpoint to catch the error and inspect the problematic sample:

1. Open the Run and Debug panel in VS Code
2. In the Breakpoints section, enable "Uncaught Exceptions"
3. Run `train.py` with the debugger (F5)
4. When the error occurs, VS Code pauses at the exact line. Inspect the local variables to see which sample index and filename caused the error.


## Task 2: Automated Git Bisect

Someone added the corrupted file to `filelist.txt` in a past commit. Use `git bisect` with an automated test script to find exactly which commit introduced the bug.

### Step 1: Write a test script

Create `bisect_test.py` that:

- Loads every sample in the dataset
- Exits with code 0 if all samples load successfully
- Exits with code 1 if any sample fails

```python
# bisect_test.py
import sys
from dataset import WaveformDataset

def test_dataset():
    # TODO: Implement this function
    pass

if __name__ == "__main__":
    success = test_dataset()
    sys.exit(0 if success else 1)
```

### Step 2: Run automated bisect

```bash
# View commit history to find the initial commit hash
git log --oneline

# Start bisect
git bisect start
git bisect bad HEAD
git bisect good <initial-commit-hash>

# Run automated bisect
git bisect run uv run python bisect_test.py

# When finished, examine the bad commit
git show

# End bisect session
git bisect reset
```


## Submission

Submit your answers on Blackboard.

**Task 1**: Answer the following questions in Blackboard:

1. Which line in `dataset.py` raises the error?
2. What is the filename of the corrupted sample?
3. Why does this file cause an error? (Hint: open the file and look at its contents)

**Task 2**: 

4. Upload a screenshot showing the `git bisect run` process and results
5. Provide the commit hash that introduced the corrupted file