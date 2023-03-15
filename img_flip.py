import os
import sys
import subprocess
import time

start_time = time.time()
sys.stdout.write('\nstarting img flip script\n')

if len(sys.argv) < 2:
    sys.stderr.write('insufficient arguments\n\n')
    exit(-1)

folderPath = sys.argv[1]
folderPath = os.path.abspath(folderPath)
sys.stdout.write('folder path: ' + folderPath + '\n')

filePathList = []
for path in os.listdir(folderPath):
    filePath = os.path.join(folderPath, path)
    if os.path.isfile(filePath):
        if filePath.endswith('.jpg') or filePath.endswith('.png'):
            filePathList.append(filePath)

executablePath = 'D:\\IVI_MISC\\Apps\\IrfanView\\App\\IrfanView64\\i_view64.exe'
for filePath in filePathList:
    sys.stdout.write('processing file: ' + filePath + '\n')
    command = [executablePath, filePath, '/hflip', '/convert=' + filePath]
    subprocess.run(command)

exec_time = str(round(time.time() - start_time, 2))
sys.stdout.write('\ndone; execution time: ' + exec_time + ' seconds\n')
