# copyDecomposedCase

copy from `case/processor*/timeDir` and `case/processor*/constant` to **respective** current directories `processor*/` (as far as I know, `rsync` cannot create respective processor folders and put the files in the right place)

# usage
0. put the script in the target directory   
1. modify hardcoded source directory name
2. specify the number of processors used in source diretory and the string for targeting timeDir
3. make sure in target directory there's no `processor*` folder, if not those directories are going to be removed
4. let the script copy both `field data` and constant(or `mesh data`) to the right place. Depending on existence of processor direcotories.

# limit
cannot copy `constant` and `system` to current dir using `shutil.copytree`
