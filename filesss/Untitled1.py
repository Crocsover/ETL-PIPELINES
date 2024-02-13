#!/usr/bin/env python
# coding: utf-8

# In[61]:


def decode(messaged_file):
    # Read the contents of the text file
    with open(messaged_file, 'r') as file:
        lines = file.readlines()

    # Parse the lines into a dictionary
    my_dict = {}
    for line in lines:
        key, value = line.strip().split(' ')
        my_dict[int(key)] = value

    # Sort the dictionary by keys in ascending order
    sorted_dict = dict(sorted(my_dict.items()))

    # Initialize an empty list to store the values associated with the end of each row
    row_values_list = []

    # Get the end of each row in the half pyramid
    current_key = 1
    while current_key in sorted_dict:
        end_key = current_key
        for key in range(current_key, current_key * 2):
            if key in sorted_dict:
                end_key = key
        row_values_list.append(sorted_dict[end_key])
        current_key *= 2

    # Concatenate the list of row values into a single string with spacing
    row_values_str = " ".join(row_values_list)

    return row_values_str


# In[62]:


filename = r'message_file.txt'
print(decode(filename))



# In[ ]:




