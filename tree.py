# tree.py
# Jonathan Grant - 4/30/2016
# This program implements the methods of a binary
# search tree. A text file is read, and individual words
# are inserted into the tree in alphabetical order.

class Tree_node():
    """ Creates a node with a name and amount. """

    # self.name - the word that will be inserted to the node
    # self.amount - number of times the word comes up
    # self.left - points to the left child
    # self.right - points to the right child

    def __init__(self, word):
        """ Initializes the node. """

        self.value = word
        self.left = None
        self.right = None
        self.amount = 1

    def print(self):
        """ Prints the node and its frequency. """

        print(self.value, ': ', self.amount, sep = '')

class Tree():
    """ Contains the methods of a binary search tree.

    Methods include:

    Inserting a new node
    In order traversal
    """

    def __init__(self):
        """ Initializes an empty binary search tree. """

        # self.root - Points to the root of the tree
        # self.number_of_words - Number of words in the tree
        # self.total_words - Number of total words in the file

        self.root = None
        self.number_of_words = 0
        self.total_words = 0

    def in_order_traversal_rec(self, pointer):
        """ Recursively prints the tree in order.

        pointer - points to the root of the tree, and
                  then the root of each branch/sub-branch
        """

        if (pointer is not None):

            self.number_of_words += 1
            self.total_words += pointer.amount

            # Print the left branch
            self.in_order_traversal_rec(pointer.left)

            # Print the node
            pointer.print()

            # Print the right branch
            self.in_order_traversal_rec(pointer.right)

    def in_order_traversal(self):
        """ Performs a traversal and prints the number of words."""

        print()
        print('Word: Number of Occurences')

        self.in_order_traversal_rec(self.root)

        print()
        print('Number of words in tree:', self.number_of_words)
        print('Number of words in file:', self.total_words)
        print()

    def insert_node_rec(self, pointer, word):
        """ Recursively inserts a new node in alphabetical order.

        word - name of the node that will be inserted
        """

        # Insert into an empty tree
        if self.root is None:

            self.root = Tree_node(word)

        # If the node already exists, increment its amount.
        elif word == pointer.value:

            pointer.amount += 1

        # For words lower in the alphabet, move them to the
        # left child
        elif (word < pointer.value):

            if (pointer.left is None):

                pointer.left = Tree_node(word)

            else:

                self.insert_node_rec(pointer.left, word)

        # For words higher in the alphabet, move them to the
        # right child
        else:

            if (pointer.right is None):

                pointer.right = Tree_node(word)

            else:

                self.insert_node_rec(pointer.right, word)

def process_file():
    """ Translates the words from a .txt into a tree.

    Requires the user to input a filename, then
    puts the words into a tree.
    """

    # text_file_tree - The tree that the words are inserted into
    # file_name - name of the .txt file the user inputs
    # f - Name given to open the filename

    binary_search_tree = Tree()

    file_name = input('What is the filename? ')

    # Open the .txt file and insert its words into the list

    f = open(file_name)

    for line in f:

        for word in line.split():

            binary_search_tree.insert_node_rec(
                                   binary_search_tree.root, word)

    f.close()

    # Print the list in alphabetical order

    binary_search_tree.in_order_traversal()

def display_program_info():
    """ Displays information on the program functionality. """

    print()
    print('tree.py')
    print('This program implements the methods of a binary')
    print('search tree. A text file is read, and individual')
    print('words are inserted into the tree in alphabetical')
    print('order. They are displayed, along with how many')
    print('times they show up in the text file.')
    print()

def Main():
    """ Implements a binary search tree from a text file. """

    display_program_info()

    process_file()

Main()
