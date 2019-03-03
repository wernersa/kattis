import os
import sys
import argparse
import subprocess
import json
from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen, Request

SOLUTIONS = 'sample_solutions'

# TODO:
# parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('integers', metavar='N', type=str, nargs='+',
#                     help='an integer for the accumulator')

# Check if the sample solutions directory exists
if not os.path.isdir(SOLUTIONS):
    os.makedirs(SOLUTIONS)


class Kattis_Problem(object):
    """docstring for Kattis_Problem."""
    def __init__(self, problem_id):
        super(Kattis_Problem, self).__init__()
        self.id = problem_id
        self.folder = f'{SOLUTIONS}/{self.id}/'
    
    
    def download(self):
        #Check if problem has been downloaded before:
        if not os.path.isdir(self.folder):
            os.makedirs(self.folder)
        elif len(os.listdir(self.folder)) > 0:
            # Directory is not empty
            return
        
        url = f'https://open.kattis.com/problems/{self.id}/file/statement/samples.zip'
        #print("Dowloading: ", url)
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        resp = urlopen(req)

        zip_ref = ZipFile(BytesIO(resp.read()))
        zip_ref.extractall(folder)
        zip_ref.close()

    def solve(self):
        
        names = set([self.folder + filename.split('.')[-2] for filename in os.listdir(self.folder)])
        for filename in sorted(names):
            
            out = []
            with subprocess.Popen(["python", f"{self.id}.py"], stdin=file_in, stdout=subprocess.PIPE, bufsize=1, universal_newlines=True) as p:
                for line in p.stdout:
                    out.append(line)
                    print(line, end='') # process line here

            if p.returncode != 0:
                raise subprocess.CalledProcessError(p.returncode, p.args)

            # Input
            # file_in = open(filename + '.in')
            # out = subprocess.run(["python", f"{self.id}.py"], stdin=file_in, stdout=subprocess.PIPE)
            # file_in.close()
            # out = out.stdout.decode("utf-8").splitlines()

            # Output
            file_out = filename + '.ans'
            with open(file_out, "r") as f: solution = f.read().splitlines()
            
            print("Out:\n", out, "\nSolution:\n", solution)
            assert out == solution

        return True

# For testing purposes. Will only run if this file is executed:
if __name__ == "__main__":
    # If running the file directly, it is a test case:
    problem_id = "different"
    
    if sys.argv[1] is not None:
        problem_id = sys.argv[1]

    problem = Kattis_Problem("different")
    problem.download()
    problem.solve()