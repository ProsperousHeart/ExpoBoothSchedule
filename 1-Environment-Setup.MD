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

# Prepare Your Environment

Ensure you have python installed. For this project, we are using 3.6.5 versiom.

It is always best practice to complete your projects in their own virtual environment. Therefore, we will follow [this doc](https://github.com/ProsperousHeart/cheatsheets/blob/master/Processes/virtualenvs.md) - specifically:
- the [virtualenv](https://github.com/ProsperousHeart/cheatsheets/blob/master/Processes/virtualenvs.md#virtualenv) section
 - the [virtualenvwrapper](https://github.com/ProsperousHeart/cheatsheets/blob/master/Processes/virtualenvs.md#virtualenvwrapper) section, which will make things SO awesome (my favorite reason being that when you turn on the virtual machine, it takes you directly in to the folder your [project](https://github.com/ProsperousHeart/cheatsheets/blob/master/Processes/virtualenvs.md#alternative) is stored in)
