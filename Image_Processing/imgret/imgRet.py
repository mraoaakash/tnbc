import shutil # for copying files
import os # for checking if file exists
import numpy as np # for image processing
import fnmatch # for matching file names
exclude = ['benchmark','segments', 'ex_datasets', 'tSNE', 'newseg', '224:224', 'send_og', 'clusters']
def imgRet(key='hne'):
    for subdir, dirs, files in os.walk("/storage/tnbc"):
        dirs[:] = [d for d in dirs if d not in exclude]
        for file in files:
            if fnmatch.fnmatch(file, '*.tif'):
                if key in file.lower() and (("cropped" in file.lower())==False):
                    prpath=str(os.path.join(subdir, file))
                    print(file)
                    shutil.copy(prpath, "/storage/tnbc/segments/224:224/send_og")
					#call yout preferred function here
					#can be	randcrop or imgcrop or any
					#custom function

imgRet('hne')