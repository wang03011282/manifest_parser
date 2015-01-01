import os
import sys
import time
import xml.etree.ElementTree as ET


# print username and current work dir for test
#print os.getlogin()
#print os.getcwd()
print(os.getlogin())
print(os.getcwd())

top_dir = os.getcwd()

def load_xml_file(fileName):
    # check that whether the manifest.xml exist
    if os.path.exists(fileName):
        #print fileName+' exists'
        print(fileName, ' exists')
    else:
        #print r"  'manifest.xml' does not exists, please check"
        print(r"  'manifest.xml' does not exists, please check")
        sys.exit(1)
    
    # load manifest.xml and parse the 'dest' and 'src' element of every 'project'
    root = ET.parse(fileName).getroot()
    all_projects = root.findall('project')
    #print '  projects total: ',len(all_projects)
    print('  projects total: ', len(all_projects))
    
    i=0;
    for project in all_projects:
        print(i)
        i+=1
        name = project.get('name')
        print('name: ', name)
        path = project.get('path')
        print('path: ', path)
        # test to create new dir of each 'project'
        dest_path = os.path.join(top_dir, path)
        print('dest_path: ', dest_path)
        if not os.path.exists(dest_path):
            os.makedirs(dest_path)
        os.chdir(dest_path)
        print('******** change dir: ', os.getcwd())
        os.system('echo '+dest_path+' >readme.txt')
        os.chdir(top_dir)
        print('######## recover dir: ', os.getcwd())
        

    
if __name__ == "__main__":
    load_xml_file(r'./manifest.xml')