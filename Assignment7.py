import re

dictionary = {
    "name": "root",
    "contents":
        [
            {
                "name": "boot",
                "contents":
                    [
                        {
                            "name": "boot.img"
                        },
                        {
                            "name": "kernel.img"
                        },
                        {
                            "name": "loaders",
                            "contents":
                                [
                                    {
                                        "name": "file1.txt",
                                    },
                                    {
                                        "name": "file2.py"
                                    }
                                ]
                        }
                    ]
            },
            {
                "name": "/tmp",
                "contents":
                    [
                        {
                            "name": "file2.docx",
                        },
                        {
                            "name": "file3.doc",
                        },
                        {
                            "name": "folder1",
                            "contents":
                                [
                                    {
                                        "name": "file4.txt",
                                    },
                                    {
                                        "name": "file5.py"
                                    }
                                ]
                        }
                    ]
            }
        ]
}


def print_depth(input_dict):
    for key, value in input_dict.items():
        if isinstance(value, list):
            list_itr(value)
        elif re.match(
                r"^([a-zA-Z0-9\s_\\.\-\(\):])+(.doc|.docx|.txt|.img|.py|.jpg|.jpeg|.css|.html|.zip|.pdf|.xml|.php)",
                value):
            print(value)


def list_itr(input_list):
    for i in input_list:
        if isinstance(i, dict):
            print_depth(i)
        elif re.match(r"^([a-zA-Z0-9\s_\\.\-\(\):])+(.doc|.docx|.txt|.img|.py)", i):
            print(i)


print("\nList of all the files from a dictionary : ")
print('- ' * 20)
print_depth(dictionary)
