# File Objects

# Context Managers
# Printing the entire file
with open('/Users/pmcorrea/Notebooks/Resources/The Crazy Ones.txt', 'r') as f:
    f.contents = f.read()
    print(f.contents)

# Printing line by line
with open('/Users/pmcorrea/Notebooks/Resources/The Crazy Ones.txt', 'r') as f:
    f.contents = f.readline()
    print(f.contents)

    f.contents = f.readline()
    print(f.contents)

# Iterating over lines
with open('/Users/pmcorrea/Notebooks/Resources/The Crazy Ones.txt', 'r') as f:
    for line in f:
        print(line, end='')

# Printing specified amount with loops
with open('/Users/pmcorrea/Notebooks/Resources/The Crazy Ones.txt', 'r') as f:

    size_to_read = 100
    f.contents = f.read(size_to_read)

    while len(f.contents) > 0:
        print(f.contents, end='*')
        f.contents = f.read(size_to_read)

# Display current position
#f.tell()

# Move to a specific position
# Moves to the beginning
#f.seek(0)

# Writing to files
with open('writing_to_file_test', 'w') as f:
    f.write('Writing to a new file!')
