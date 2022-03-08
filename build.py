import os
import subprocess

# runs = [22, 23, 24, 26, 27, 28, 29, 30, 34, 36, 37, 38, 39, 43, 44, 45, 53, 54, 55, 56, 57, 58, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104]
runs = [73,74,75,81,82,93, 94,95,102]
directories = ['/home/otteflor/Git/euxfel_reduction/config/2699_{:0>3d}'.format(r) for r in runs]

for directory in directories:
    subprocess.Popen(["make"], cwd=directory)