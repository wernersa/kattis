import os
import sys
import argparse
import subprocess
import json
from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen, Request

SOLUTIONS_FOLDER = 'sample_solutions/'


######################################################
# TODO: Add link to solution submission.
#           - Suggest doing this automatically?
# TODO: Format Output & Input



# Check if the sample solutions directory exists
if not os.path.isdir(SOLUTIONS_FOLDER):
    os.makedirs(SOLUTIONS_FOLDER)

class Kattis_Problem(object):
    """docstring for Kattis_Problem."""
    def __init__(self, problem_id):
        super(Kattis_Problem, self).__init__()
        self.id = problem_id
        self.solution_folder = f'{SOLUTIONS_FOLDER}/{self.id}/'
    
    
    def download(self):
        #Check if problem has been downloaded before:
        if not os.path.isdir(self.solution_folder):
            os.makedirs(self.solution_folder)
        elif len(os.listdir(self.solution_folder)) > 0:
            # Directory is not empty
            print("Solution samples already downloaded")
            return
        
        url = f'https://open.kattis.com/problems/{self.id}/file/statement/samples.zip'
        #print("Dowloading: ", url)
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        resp = urlopen(req)

        zip_ref = ZipFile(BytesIO(resp.read()))
        zip_ref.extractall(self.solution_folder)
        zip_ref.close()

    def solve(self):
        
        names = set([filename.split('.')[-2] for filename in os.listdir(self.solution_folder)])
        for filename in sorted(names):
            filepath = self.solution_folder + filename

            print(f"\nRunning test case #{filename}:")

            file_in = open(filepath + '.in')
            out = []
            with subprocess.Popen(["python", f"{self.id}.py"], stdin=file_in, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1, universal_newlines=True) as p:
                for line in p.stdout:
                    out.append(line.rstrip('\n'))
                    print("Out:    ", line, end='')
                for error in p.stderr:
                    print("Error: ", error, end='')

            if p.returncode != 0:
                raise subprocess.CalledProcessError(p.returncode, p.args)

            # Output
            file_out = filepath + '.ans'
            with open(file_out, "r") as f: solution = f.read().splitlines()
            
            print("Solution:", solution)
            assert out == solution

        return True

# For testing purposes. Will only run if this file is executed:
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Utility functions for solving problems on kattis')
    parser.add_argument('id',help='The problem id found on kattis', nargs='?', default="different")
    args = vars(parser.parse_args())

    if args['id']:
        problem_id = args['id']
        # Test using "different" if not argument is used
    
    problem = Kattis_Problem(problem_id)
    problem.download()
    problem.solve()