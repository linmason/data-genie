## Contributing Guidelines

1. All changes should be done on a branch separate from main.
    * This ensures that the main branch always maintains a stable version, 
    and that any major mistakes stay isolated to a branch and not the entire codebase.
2. All changes should include tests.
    * This will help us ensure our code works (outside of end-to-end testing) and will
    prevent simple bugs so we don't waste time looking for them later.
3. All changes should be reviewed by at least one person before being merged to main.
    * It is good to get a fresh pair of eyes on all code just to double check for
    any bugs or forgotten edge cases.

---

## Git 'How to' Guides

### Committing changes

1. Add the changes files to git's staging area
   ```
   git add file_1 file_2 file_3
   ```
   * It is common to just add all the files by running this line
   from the project's root dir:
   ```
   git add .
   ```
2. (Optional) Do `git status` to check that you added the correct files

3. Run `git commit`. In the window that appears, write a concise message
describing the changes you are committing. At this point, if you changed your
mind about committing, you should make this file empty to abort the commit.
Saving and closing the window will finish the commit.

4. (Optional) If you are ready to upload your changes to github, run `git push`

#### Creating a new branch and pushing it to github

1. Pull latest changes from the branch you want to make changes to (in this case, main)
    ```
    git checkout main
    git pull
    ```

2. Make and switch to a new branch
    ```
    git switch -c new_branch_name
    ```

3. Create files, write code (don't forget tests!)

4. Commit changes and push them. Write a concise commit message

5. Push the changes to git. Do `git push` and then copy/paste the corrected version it gives
you in order to write the new branch to git

6. Follow the link it gives you and make a new pull request

Now any changes you make while on this branch can be committed and pushed like
normal and the pull request will update upon each push. 
Use `git checkout branch_name` to switch to a different branch (like main)