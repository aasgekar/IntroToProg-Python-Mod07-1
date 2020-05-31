## Fantasy Baseball Wish List

### Introduction
This is a script that will allow a user to keep a wish list of players they hope to draft for a Fantasy Baseball league.  The file will be stored as a Binary file on the hard drive.  While a binary file is not the same as an encrypted file, it will not be printed in plain text, so that if someone were to open the script, they would have difficulty in reading what is contained.
This assignment is making use of the Pickle module and Try and Except blocks.

### Drafting the Script
As will the past several assignments, this script is divided according to Separation of Concerns.  The sections include Data, Processing, Presentation, and the Main Body of the Script.  First in the processing section is an Exception class (figure 7.1) ![](figures/figure71.png)

The positions in Baseball are numbered 1 through 9.  A range function (figure 7.2) has been created to check if the user enters a number outside of 1 up to, but not including, 10.
![](https://github.com/jaytreelove/IntroToProg-Python-Mod07/blob/master/figures/figure72.png)

If the user enters an integer outside of this range, the exception is raised, and an error message is returned.  There is more detail about this and Try and Except in the Main Body of the Script.
Next are two functions to create and read a binary file using Python’s Pickle module.  Pickling is one of three modules that Python uses for serialization.  This process can take a complex object structure and transform it so that it can be saved or sent over a network as a stream of bytes.  The Pickle module serializes and deserializes object in a binary format.  More about Pickling and the other serialization methods can be found on this article [The Python pickle Module: How to Persist Objects in Python (external link)](https://realpython.com/python-pickle-module/) from Real Python.
First is the function to create or add to the file (figure 7.3).   This function is very similar to function used in early assignments with 2 differences.  First, when opening the file (line 36) instead of just an ‘a’ to append, ‘ab’ is used to append binary.  Also, the dump function (line 37) is what creates the file containing the serialization result.
![](https://github.com/jaytreelove/IntroToProg-Python-Mod07/blob/master/figures/figure73.png)


You can use the [editor on GitHub](https://github.com/jaytreelove/IntroToProg-Python-Mod07/edit/master/README.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](https://github.com/jaytreelove/IntroToProg-Python-Mod07/blob/master/figures/figure71.png)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/jaytreelove/IntroToProg-Python-Mod07/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
