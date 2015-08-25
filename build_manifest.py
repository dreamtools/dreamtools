import glob
import os


directories = glob.glob('dreamtools' + os.sep + 'dream*')
directories = sorted(directories)


print("include README.rst setup.cfg")
print("recursive-include dreamtools *.R")
print("recursive-include dreamtools *.csv")
print("recursive-include dreamtools *.pyx")
print("recursive-include dreamtools *.pl")


for directory in directories:

    sub_directories = glob.glob(directory + os.sep + 'D*')
    if len(sub_directories) == 0:
        continue

    for that in sub_directories:

        contents = glob.glob(that + '/' + '*')
        #print contents
        # identify templates/data/goldstandard


        for this in contents:
            if this.endswith('data') or this.endswith('goldstandard') or this.endswith('templates'):
                if len(glob.glob(this + os.sep + '*'))>0:
                    print("recursive-include %s *" % this)

print("""
recursive-include dreamtools/dream8/D8C1/data *.csv *.json *dat
recursive-exclude dreamtools/dream6/D6C4/codeanddata *
""")

# exclude D7C2, D6C1
