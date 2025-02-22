# Inheritance with cats!

"""
Here's the animal/pet classes!
"""
# <include prob/topics/oop/animal.py>
#
# #Implement q1 Here!
#
# <include prob/topics/oop/easy/cat.py>
class Keyboard:
    """A Keyboard takes in an arbitrary amount of buttons, and has a
    dictionary of positions as keys, and Buttons as values.

    >>> b1 = Button(0, "H")
    >>> b2 = Button(1, "I")
    >>> k = Keyboard(b1, b2)
    >>> k.buttons[0].key
    'H'
    >>> k.press(1)
    'I'
    >>> k.typing([0, 1])
    'HI'
    >>> k.typing([1, 0])
    'IH'
    >>> b1.pressed
    2
    >>> b2.pressed
    3
    """

    def __init__(self, *args):
        self.buttons = {}
        for arg in args:
            self.buttons[arg.pos]=arg

    def press(self, info):
        """Takes in a position of the button pressed, and
        returns that button's output"""
        self.buttons[info].pressed += 1
        return self.buttons[info].key

    def typing(self, typing_input):
        """Takes in a list of positions of buttons pressed, and
        returns the total output"""
        sum = ''
        for pos in typing_input:
            sum+= self.press(pos)
        return sum

class Button:
    def __init__(self, pos, key):
        self.pos = pos
        self.key = key
        self.pressed = 0


# T88ble

simple_table_rows = [['chocolate',2], ['vanilla', 1]]
simple_table_labels = ['Flavor', 'Price']
longer_table_rows = [[1990, 1, 1.5, 12, 7], [2000, 2, 2.5, 25, 10], [2010, 5, 4, 70, 36]]
longer_table_labels = ['Year', 'Bread price', 'Eggs price', 'Average tank of gas', 'Rent per day']

class T88ble():
    """
    T88ble is an object similar to the Data 8 Table object.
    Here the internal representation is a list of rows.
    """
    def __init__(self, rows=[], labels=[]):
        self.rows = rows
        self.column_labels = labels
    #DO NOT CHANGE THE __repr__ functions
    def __repr__(self):
        result = ""
        result += str(self.column_labels) + "\n"
        for row in self.rows:
            result += str(row) + "\n"
        return result
    def num_rows(self):
        """
        Compute the number of rows in a table.

        >>> simple_table = T88ble(simple_table_rows, simple_table_labels)
        >>> simple_table.num_rows()
        2
        >>> longer_table = T88ble(longer_table_rows, longer_table_labels)
        >>> longer_table.num_rows()
        3
        """
        return len(self.rows)
        

    def num_cols(self):
        """
        Compute the number of cols in a table.

        >>> simple_table = T88ble(simple_table_rows, simple_table_labels)
        >>> simple_table.num_cols()
        2
        >>> longer_table = T88ble(longer_table_rows, longer_table_labels)
        >>> longer_table.num_cols()
        5
        """
        return len(self.column_labels)  
        

    def labels(self):
        """
        Lists the column labels in a table.

        >>> simple_table = T88ble(simple_table_rows, simple_table_labels)
        >>> simple_table.labels()
        ['Flavor', 'Price']
        >>> longer_table = T88ble(longer_table_rows, longer_table_labels)
        >>> longer_table.labels()
        ['Year', 'Bread price', 'Eggs price', 'Average tank of gas', 'Rent per day']
        """
        return self.column_labels
        

    def column(self, label):
        """
        Returns the values of the column represented by label.

        >>> simple_table = T88ble(simple_table_rows, simple_table_labels)
        >>> simple_table.column("Flavor")
        ['chocolate', 'vanilla']
        >>> longer_table = T88ble(longer_table_rows, longer_table_labels)
        >>> longer_table.column("Eggs price")
        [1.5, 2.5, 4]
        >>> longer_table
        ['Year', 'Bread price', 'Eggs price', 'Average tank of gas', 'Rent per day']
        [1990, 1, 1.5, 12, 7]
        [2000, 2, 2.5, 25, 10]
        [2010, 5, 4, 70, 36]
        """
        index_of_label = self.column_labels.index(label)
        return [x[index_of_label] for x in self.rows]
        

    def with_column(self, label, values):
        """
        Returns a new table with an additional or replaced column.
        label is a string for the name of a column, values is an list

        >>> longer_table = T88ble(longer_table_rows, longer_table_labels)
        >>> longer_table.with_column('Inflation rate', [i for i in range(longer_table.num_rows())])
        ['Year', 'Bread price', 'Eggs price', 'Average tank of gas', 'Rent per day', 'Inflation rate']
        [1990, 1, 1.5, 12, 7, 0]
        [2000, 2, 2.5, 25, 10, 1]
        [2010, 5, 4, 70, 36, 2]
        >>> longer_table
        ['Year', 'Bread price', 'Eggs price', 'Average tank of gas', 'Rent per day']
        [1990, 1, 1.5, 12, 7]
        [2000, 2, 2.5, 25, 10]
        [2010, 5, 4, 70, 36]
        """
        new_labels = self.column_labels + [label]
        new_rows = [self.rows[x]+ [(values[x])] for x in range(len(self.rows))]
        return T88ble(new_rows,new_labels)
        

    def select(self, labels):
        """
        Create a copy of a table with only some of the columns,
        reffered to by the list of labels.

        >>> simple_table = T88ble(simple_table_rows, simple_table_labels)
        >>> simple_table.select(["Flavor"])
        ['Flavor']
        ['chocolate']
        ['vanilla']
        >>> simple_table
        ['Flavor', 'Price']
        ['chocolate', 2]
        ['vanilla', 1]

        >>> longer_table = T88ble(longer_table_rows, longer_table_labels)
        >>> longer_table.select(['Year', 'Average tank of gas'])
        ['Year', 'Average tank of gas']
        [1990, 12]
        [2000, 25]
        [2010, 70]
        >>> longer_table
        ['Year', 'Bread price', 'Eggs price', 'Average tank of gas', 'Rent per day']
        [1990, 1, 1.5, 12, 7]
        [2000, 2, 2.5, 25, 10]
        [2010, 5, 4, 70, 36]
        """
        indicies_of_labels = [self.column_labels.index(label) for label in labels]
        rows = [[x[y] for y in indicies_of_labels] for x in self.rows]
        return T88ble(rows, labels)
        
    def sort(self, label, descending=True):
        """
        Create a copy of a table sorted by the values in a column.
        Defaults to ascending order unless descending = True is included.

        >>> longer_table = T88ble(longer_table_rows, longer_table_labels)
        >>> longer_table.sort("Year")
        ['Year', 'Bread price', 'Eggs price', 'Average tank of gas', 'Rent per day']
        [2010, 5, 4, 70, 36]
        [2000, 2, 2.5, 25, 10]
        [1990, 1, 1.5, 12, 7]
        >>> longer_table
        ['Year', 'Bread price', 'Eggs price', 'Average tank of gas', 'Rent per day']
        [1990, 1, 1.5, 12, 7]
        [2000, 2, 2.5, 25, 10]
        [2010, 5, 4, 70, 36]

        >>> simple_table = T88ble(simple_table_rows, simple_table_labels)
        >>> simple_table.sort("Price", descending=False)
        ['Flavor', 'Price']
        ['vanilla', 1]
        ['chocolate', 2]
        >>> simple_table
        ['Flavor', 'Price']
        ['chocolate', 2]
        ['vanilla', 1]

        """
        rows_copy = self.rows[:]
        index_of_column = self.column_labels.index(label)
        if descending:
            sorted_rows = sorted(rows_copy, key = lambda n: n[index_of_column] , reverse = True)
        else:
            sorted_rows = sorted(rows_copy, key = lambda n: n[index_of_column] , reverse = False)
        return T88ble(sorted_rows, self.column_labels)


        
        


    def where(self, label, filter_fn):
        """
        Create a copy of a table with only the rows that match a filter function.

        >>> def above(x):
        ...     return lambda y: y > x
        ...
        >>> longer_table = T88ble(longer_table_rows, longer_table_labels)
        >>> longer_table.where('Eggs price', above(2))
        ['Year', 'Bread price', 'Eggs price', 'Average tank of gas', 'Rent per day']
        [2000, 2, 2.5, 25, 10]
        [2010, 5, 4, 70, 36]
        >>> longer_table
        ['Year', 'Bread price', 'Eggs price', 'Average tank of gas', 'Rent per day']
        [1990, 1, 1.5, 12, 7]
        [2000, 2, 2.5, 25, 10]
        [2010, 5, 4, 70, 36]
        """
        rows_copy = self.rows[:]
        index_of_column = self.column_labels.index(label)
        new_rows= []
        for row in rows_copy:
            if filter_fn(row[index_of_column]):
                new_rows += [row]
            else:
                new_rows = new_rows
        return T88ble(new_rows, self.column_labels)
        


