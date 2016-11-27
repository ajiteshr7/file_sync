import filecmp
import updateFileList
import os

def main():
    if updateFileList.update_proj_dir():
        chk_ver()
    else:
        exit()


def chk_ver():
    srcf_dir = os.getcwd()
    dstf_dir = r"C:\Users\ajiteshr7\Dropbox\python_proj"
    i = 0      # Flag
    cf_list = []
    f_list = os.listdir(srcf_dir)
    # Check if files updated (content changed)
    match, mismatch, error = filecmp.cmpfiles(srcf_dir, dstf_dir, f_list)
    print updateFileList.marker
    # Only update files i.e skip dirs
    for files in mismatch:
        if '.' in files:
            cf_list.append(files)

    if cf_list:
        print "These files changed(content):"
        updateFileList.print_file(cf_list)
        # Copy files that changed
        i = updateFileList.cpy_c_files(cf_list, srcf_dir, dstf_dir)
        if i :
            print "Successfully updated.. :)"
        else:
            print "Didn't updated =("
    else:
        print "Files already up-to-date!!"

if __name__ == "__main__":
    main()
