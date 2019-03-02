import os
import subprocess
import json
from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen, Request

SOLUTIONS = 'sample_solutions'

# Check if the sample solutions directory exists
if not os.path.isdir(SOLUTIONS):
    os.makedirs(SOLUTIONS)

def kattis_download(problem_id):
    folder = f'{SOLUTIONS}/{problem_id}/'

    #Check if problem has been downloaded before:
    if not os.path.isdir(folder):
        os.makedirs(folder)
    elif len(os.listdir(folder)) > 0:
        # Directory is not empty
        return
    
    url = f'https://open.kattis.com/problems/{problem_id}/file/statement/samples.zip'
    #print("Dowloading: ", url)
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    resp = urlopen(req)

    zip_ref = ZipFile(BytesIO(resp.read()))
    zip_ref.extractall(folder)
    zip_ref.close()

def kattis_solve(problem_id):
    folder = f'{SOLUTIONS}/{problem_id}/' # TODO: This is repeated, make class?
    names = set([folder + filename.split('.')[-2] for filename in os.listdir(folder)])
    print(names)
    for filename in sorted(names):
        # Input
        file_in = open(filename + '.in')
        out = subprocess.run(["python", f"{problem_id}.py"], stdin=file_in, stdout=subprocess.PIPE)
        file_in.close()
        out = out.stdout.decode("utf-8").splitlines()

        # Output
        file_out = filename + '.ans'
        with open(file_out, "r") as f: solution = f.read().splitlines()
        
        print("Solved:", out == solution)
        assert out == solution

    return True

# For testing purposes. Will only run if this file is executed:
if __name__ == "__main__":
    #main(sys.argv[1])
    kattis_solve("different")