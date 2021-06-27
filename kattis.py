import os
import sys
import argparse
import subprocess
import json
from shutil import copyfile
from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen, Request
from submit import submit
from helpers import *

PROBLEMS_FOLDER = 'problems'
template_file = os.path.join(PROBLEMS_FOLDER, "_template.py")
SOLUTIONS_FOLDER = 'solutions'


######################################################
# TODO: Add link to solution submission.
#           - Suggest doing this automatically?
# TODO: Format Output & Input
# TODO: Check if script exist in PROBLEMS_FOLDER, else: create from template

# Check if the sample solutions directory exists
if not os.path.isdir(SOLUTIONS_FOLDER):
    os.makedirs(SOLUTIONS_FOLDER)

class Kattis_Problem(object):
    """docstring for Kattis_Problem."""

    def __init__(self, problem_id):
        super(Kattis_Problem, self).__init__()
        self.id = problem_id
        self.solution_folder = os.path.join(SOLUTIONS_FOLDER, self.id, '')
        self.script_file = os.path.join(PROBLEMS_FOLDER, f"{self.id}.py")
        
        # To run
        if self._script_exist():
            self.download()
            self.solve()
        else:
            self.create()
    
    def _script_exist(self):
        return os.path.isfile(self.script_file)

    def create(self):
        copyfile(template_file, self.script_file)
        print(f"Created {self.script_file}")
    
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
        
        #Get the filename without extension from sample solutions folder
        names = set([os.path.splitext(os.path.basename(filename))[0] for filename in os.listdir(self.solution_folder)])
        
        for filename in sorted(names):

            filepath = self.solution_folder + filename

            # Answer from current local script:
            file_in = open(filepath + '.in')
            script_result = []

            with subprocess.Popen(["python", self.script_file], stdin=file_in, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1, universal_newlines=True) as p:
                for error in p.stderr:
                    print("Error: ", error, end='')
                for line in p.stdout:
                    script_result.append(line.rstrip('\n'))
                if len(script_result) == 0:
                    print("No actual output from current script!")
                    return
                else:
                    #Print the output
                    print(f"\nRunning test case #{filename}:")
                    for out in script_result:
                        print("Out:    ", out)
            


            if p.returncode != 0:
                raise subprocess.CalledProcessError(p.returncode, p.args)

            # Answer to compare against (Sample solutions)
            file_answer = filepath + '.ans'
            with open(file_answer, "r") as f: solution = f.read().splitlines()
            
            for i, line in enumerate(script_result):
                print("")
                print("{:10}#{:>2}: {:<6}".format("Input line", i, script_result[i])) 
                print("{:10}#{:>2}: {:<6}".format("Output line", i, solution[i])) 
                print("-------------")
            print("Solution:", solution)
            assert script_result == solution
            print("Problem solved correctly!")

        return True

    def upload(self):
        with subprocess.Popen(["python", "submit.py", self.script_file, "--force"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=4096, universal_newlines=True, start_new_session=True) as p:
            for line in p.stdout.read():
                print(line, end='')
            for error in p.stderr.read():
                print(error, end='')

# For testing purposes. Will only run if this file is executed:
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Utility functions for solving problems on kattis')
    parser.add_argument('id', help='The problem id found on kattis', nargs='?', const=True, default="")
    parser.add_argument("-u", "--upload", help="Upload to kattis.com if problem solved successfully.", type=str2bool, nargs='?', const=True, default=False)
    args = vars(parser.parse_args())

    if not args['id']:
        print("Problem id not given as first argument.")
        print("https://open.kattis.com/problems/")
        print("\nusage: kattis.py [problem id]")
    elif args['id']:
        problem_id = args['id']
        print("Opening kattis problem: {}".format(problem_id))
        print("https://open.kattis.com/problems/{}/\n".format(problem_id))
        problem = Kattis_Problem(problem_id)

        if args['upload']:
            problem.upload()