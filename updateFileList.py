# Program by AKR
# copyleft,free to use

import os
import shutil

marker = "----------------------------"
def main():
    update_proj_dir()

def update_proj_dir():
    """ Updates project dir uses copy,remove and print_file methods """
    cwd = os.getcwd()
    srcf_dir = cwd
    i = 0                # Flag
    flg_cpy = True       # Flag to cpy func
    flg_rm = True        # Flag to rm func
    file_uc_list = []    # Files unchanged
    file_c_list = []     # Files changed
    file_r_list = []     # Files to be removed
    # Project dir
    dstf_dir = r"C:\Users\ajiteshr7\Dropbox\python_proj"
    file_srclist = os.listdir(srcf_dir)
    file_dstlist = os.listdir(dstf_dir)
    file_uc_list, file_c_list = chk_chng(file_srclist, file_dstlist)
    # Display files unchanged
    if file_uc_list:
        print marker
        print "File List"
        print "No of files : %d" %(len(file_uc_list))
    print_file(file_uc_list)
    # Display files changed
    if file_c_list:
        print "Files added"
        print "No of files added: %d" %(len(file_c_list))
        print_file(file_c_list)
    else:
        print "No files added"
        print "No of files added: 0"
        flg_cpy = False
    # Copy files..
    i = cpy_c_files(file_c_list, srcf_dir, dstf_dir,flg_cpy)
    # Remove files...
    file_list, file_r_list = chk_chng(file_dstlist,file_srclist)
    if not file_r_list:
        flg_rm = False
    rm_f(file_r_list,dstf_dir,flg_rm)
    # Display result updated or didn't....
    if flg_cpy == False and flg_rm == False:
        print "Directory is up-to-date..."
    elif i == len(file_c_list):
        print "Sucessfully Updated the project directory :)"
    else:
        print "Didn't updated the folder.... =("
        return False
    return True

def print_file(f):
    """Prints the filename in the provided list"""
    print marker
    for files in f:
        print files
    print marker


def cpy_c_files(c_fl, src, dst, flg = True):
    """ Copies files and directories to the project folder
        Usage: (files list,sorce dir,destination dir, flag)
        flag can be true or false (optional argument) """
    if flg == False:
        return 0
    print "Do you want to copy files...(Y/N):"
    choice = raw_input()
    if choice.lower() == 'y':
        print "Copying files......."
        i = 0
        print marker
        for files in c_fl:
            print "Adding %s to project dir" %(files)
            f_src = os.path.join(src, files)
            f_dst = os.path.join(dst, files)
            if os.path.isdir(f_src):
                # Copy directory
                shutil.copytree(f_src, f_dst)
            else:
                # Copy files
                shutil.copy(f_src, f_dst)
            i += 1
        print "Copied %d files" %(i)
    else:
        i = 0
    return i

def rm_f(f_l, path, flg = True):
    """rm files in the list provided Usage:(file list, path , flag)
        flag can be true or false.(optional argument)"""
    if flg == False:
        return
    print marker
    print "These files will be removed"
    print_file(f_l)
    print "Proceed (Y/N):"
    choice = raw_input()
    if choice.lower() == 'y':
        i = 0
        print marker
        for files in f_l:
            print "Removing %s from the project dir" %(files)
            f_path = os.path.join(path, files)
            if os.path.isdir(f_path):
                # Remove directory
                shutil.rmtree(f_path)
            else:
                # Remove files
                os.remove(f_path)
            i += 1
        print "Removed %d files" %(i)
    else:
        pass

def chk_chng(src_flist,dst_flist):
    """ Returns unchanged file list and changed file list
        Accepts source file list and dsetination file list"""
    uc_flist = []
    c_flist = []
    for files in src_flist:
        if files in dst_flist:
            uc_flist.append(files)
        else:
            c_flist.append(files)
    return uc_flist,c_flist


if __name__ == "__main__":
    main()
