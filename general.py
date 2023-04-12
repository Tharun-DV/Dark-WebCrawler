import os

# Creating s Project Directory for the Entered Website
def project_dir(folder):
    if not os.path.exists(folder):
        print(f"Creating Project {folder} ...")
        os.makedirs(folder)

# Create crawled and needtobecralwed

def create_datafile(project_name,base_url):

    # Paths of the project files
    crawled = os.path.join(project_name , "crawled.txt")
    notyetcrawled = os.path.join(project_name,"notyetcrawled.txt")

    # checks the project files exists
    if not os.path.isfile(crawled):
        write_file(crawled,"")
    if not os.path.isfile(notyetcrawled):
        write_file(notyetcrawled,base_url)

# Function to create and write to a file
# Create a new file
def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)
# Function to append data to file
def append_file(path,data):
    with open(path,'a') as fp:
        fp.write(data+"\n")

# Function to remove all line in a file
def remove_file_content(path):
    with open(path,'w') as fp:
        pass

# Function to convert each line from the line to elements of set
def convert_file_to_set(file_name):
    converted = set()
    with open(file_name,'rt') as fp:
        for i in fp:
            converted.add(i.replace('\n',''))
    return converted

# Function to convert elements of set into file
def convert_set_to_file(file_name,converted):
    with open(file_name,"w") as fp:
        for _ in sorted(converted):
            fp.write(f"{_}\n")
