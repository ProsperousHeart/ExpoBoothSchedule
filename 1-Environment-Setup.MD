# Ensure Your Repo Is Local

Using whatever method you generally follow, ensure your repo is on your local machine.

Here is what cloning my repo ooked like as per [here](https://github.com/ProsperousHeart/cheatsheets/blob/master/Tools/git.md#clone):

![image](https://user-images.githubusercontent.com/20706498/132254282-d02e3cf5-2d89-417b-9b59-c93d6513b250.png)

If you have already created branches in GitHub, you will need to follow this procedure for downloading all of your branches - it does not automatically bring down the other branches.

At this point when I ran what was [here](https://github.com/ProsperousHeart/cheatsheets/blob/master/Tools/git.md#not-all-of-my-branches-were-cloned), I got this:

![image](https://user-images.githubusercontent.com/20706498/132255247-71d3f76a-978f-4c6c-b879-eef224f65a26.png)

Created a new issue [here](https://github.com/ProsperousHeart/ExpoBoothSchedule/issues/12).

By searching `You are in 'detached HEAD' state. You can look around, make experimental` in Google, found [this StackOverflow article](https://stackoverflow.com/a/35383761) ... Which lead me to [this aticle](https://git-scm.com/book/en/v2/Git-Branching-Remote-Branches) in the Git web space.

Here's how I fixed it:

![image](https://user-images.githubusercontent.com/20706498/132256610-5572b1e2-f953-437a-a14a-c8bc437a6baa.png)

You can confirm it was successful by running:

![image](https://user-images.githubusercontent.com/20706498/132256685-2e9b72fc-0303-46a5-823b-7519039ba406.png)

In this project I also had to set up the upstream for **main** - but ran into issues. See:  [Issue #14](https://github.com/ProsperousHeart/ExpoBoothSchedule/issues/14)

You'll just need to:
1. run `git checkout main`
2. run `git push -u origin main`

# Prepare Your Environment

Ensure you have python installed. For this project, we are using 3.6.5 versiom.

## Virtual Environment Setup

It is always best practice to complete your projects in their own virtual environment. Therefore, we will follow [this doc](https://github.com/ProsperousHeart/cheatsheets/blob/master/Processes/virtualenvs.md) - specifically:
- the [virtualenv](https://github.com/ProsperousHeart/cheatsheets/blob/master/Processes/virtualenvs.md#virtualenv) section
 - the [virtualenvwrapper](https://github.com/ProsperousHeart/cheatsheets/blob/master/Processes/virtualenvs.md#virtualenvwrapper) section, which will make things SO awesome (my favorite reason being that when you turn on the virtual machine, it takes you directly in to the folder your [project](https://github.com/ProsperousHeart/cheatsheets/blob/master/Processes/virtualenvs.md#alternative) is stored in)

*Unfortunately, the following is for Windows only. I'm not sure what it is for Linux/Mac users.*
1. Open a **_command prompt_** - your keyboard shortcut for this is:  `WINDOWS KEY + r`<br><br>It looks something like this:
    ![image](https://user-images.githubusercontent.com/20706498/132263918-2a72d502-e19a-40e5-ba99-3745df186d45.png)

2. Change into the directory where your repo is. In this example, I ran: `cd "C:\Users\Kat\Documents\Programming\repo\ExpoBoothSchedule"` 

3. As per [this](https://github.com/ProsperousHeart/cheatsheets/blob/master/Processes/virtualenvs.md#alternative), I then ran:  `mkproject ExpoBoothSchedule`

![image](https://user-images.githubusercontent.com/20706498/132264169-80194a3a-72a4-4956-9dda-a7a69250b1fa.png)
*I chose to name my project and thus virtual environment after my GitHub repo name.*

You are now in your new virtual environment!

**NOTE:**  Step 4 may be unnecessary, butI didn't realize it until after I ran it. I was basing these steps off of [old cheat sheets](https://github.com/ProsperousHeart/cheatsheets/blob/master/Processes/virtualenvs.md) of mine.

4. I then ran the following:  `setprojectdir setprojectdir "C:\Users\Kat\Documents\Programming\repo\ExpoBoothSchedule"`

  ![image](https://user-images.githubusercontent.com/20706498/132264447-e30150b5-f422-43ad-aaec-7bc4537f6b26.png)

To turn off the virtual environment, you would run:  `deactivate`

## Return To Next Step's Branch

At this point we are ready to begin creatimg bare bones.

Use git to enter into your repo. Then move into a new branch. For this project, I created the following as per [here](https://github.com/ProsperousHeart/cheatsheets/blob/master/Tools/git.md#how-do-i--create-a-new-branch):

    `git branch -b BareBones`
