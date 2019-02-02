import os


def print_directory_contents(sPath):
    """
    This function takes the name of a directory
    and prints out the paths files within that
    directory as well as any files contained in
    contained directories.

    This function is similar to os.walk. Please don't
    use os.walk in your answer. We are interested in your
    ability to work with nested structures.
    """

    print(sPath)
    allPaths = list()
    try:
        for sChild in os.listdir(sPath):
            sChildPath = os.path.join(sPath, sChild)
            if os.path.isdir(sChildPath):
                print_directory_contents(sChildPath)
            else:
                allPaths.append(sChildPath)
    except PermissionError as e:
        print("Cant open because of this error [%s]." % e)
    return allPaths


if __name__ == '__main__':
    print_directory_contents(".")
