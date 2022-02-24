import pyfiglet
from pyfiglet import Figlet
from lolpython import lol_py
import subprocess
from time import sleep
from random import randrange
from datetime import datetime

class config:

    def __init__(self):
        self.cname = self.cname_init()
    

    def cname_init(self):
        cname = "resume.jnapolitano.io"
        return cname



class dependency_pipeline: 

    def __init__(self):
        self.dependencies_log = self.install_dependencies()

    def install_dependencies(self):
        print(pyfiglet.figlet_format("Dependency Check", font = 'big'))
        utility_functions.seperator()
        #subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'my_package'])
        result = subprocess.run(['pip', 'install', '-r', 'requirements.txt'], capture_output=True, text=True)
        print(result.stdout)

        print(result.stderr)

        print(pyfiglet.figlet_format("DependenCies INstalled", font = 'big'))
        utility_functions.seperator()

        return(result)

class build_pipeline:

    def __init__(self):

        self.clean_log=self.make_clean()
        self.make_log=self.make_html()
        self.add_log=self.add()
        self.commit_log=self.commit()
        self.push_log=self.push()

    def make_clean(self):
        
        print(pyfiglet.figlet_format("Now i'm cleaning the old build", font = 'big'))

        
        #subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'my_package'])
        result = subprocess.run(['make', 'clean'], capture_output=True, text=True)
        print(result.stdout)
        print(result.stderr)

        print(pyfiglet.figlet_format("ClEAN", font = 'big'))

        return result


    def make_html(self):
        print(pyfiglet.figlet_format("Making dE HTML BUIld", font = 'big'))
        #subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'my_package'])
        result = subprocess.run(['make', 'html'], capture_output=True, text=True)
        print(result.stdout)
        print(result.stderr)
        print(pyfiglet.figlet_format("i make it", font = 'big'))

        return result

    def commit(self):
        time_stamp=utility_functions.timestamp()
        print(pyfiglet.figlet_format("commiting !!!", font = 'big'))

        
        #subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'my_package'])
        result = subprocess.run(['git', 'commit', '-m', 'autocommit on' + time_stamp], capture_output=True, text=True)
        print(pyfiglet.figlet_format("Output", font = 'big'))

        print(result.stdout)
        print(pyfiglet.figlet_format("Errors", font = 'big'))

        print(result.stderr)
    

        print(pyfiglet.figlet_format("committed", font = 'big'))
        return result


    def push(self):
        time_stamp=utility_functions.timestamp()
        print(pyfiglet.figlet_format("PUshing", font = 'big'))
        #subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'my_package'])
        result = subprocess.run(['git', 'push',time_stamp], capture_output=True, text=True)
        print(pyfiglet.figlet_format("Output", font = 'big'))

        print(result.stdout)
        print(pyfiglet.figlet_format("Errors", font = 'big'))

        print(result.stderr)
    

        print(pyfiglet.figlet_format("pushed it", font = 'big'))

        return result


    def add(self):
        
        print(pyfiglet.figlet_format("Adding CHanges!!!", font = 'big'))

        
        #subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'my_package'])
        result = subprocess.run(['git', 'add', '.'], capture_output=True, text=True)
        print(pyfiglet.figlet_format("Output", font = 'big'))

        print(result.stdout)
        print(pyfiglet.figlet_format("Errors", font = 'big'))

        print(result.stderr)
    

        print(pyfiglet.figlet_format("changes added", font = 'big'))

        return result


class deploy_pipeline:

    def __init__(self,cname):
        self.deploy_log = self.deploy(cname)

    def deploy(self,cname):
        
        print(pyfiglet.figlet_format("DEPLOYING!!!", font = 'big'))

        
        #subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'my_package'])
        result = subprocess.run(['ghp-import', '-n', '-p', '-f', '-c', cname, 'build/html' ], capture_output=True, text=True)
        print(pyfiglet.figlet_format("Output", font = 'big'))

        print(result.stdout)
        print(pyfiglet.figlet_format("Errors", font = 'big'))

        print(result.stderr)
        

        print(pyfiglet.figlet_format("i deployz it", font = 'big'))

        return result



def introduction():
    fig = Figlet(font='standard')
    print(fig.renderText("INstalling Depenedencies"))
    fig = Figlet(font='Standard')
    print(fig.renderText("B4 we begin"))
    print(fig.renderText("you Should read the requirements.txt file"))
    print(fig.renderText("If you don't trust me press ctr-c now to stop this program.   Then, read the file."))


def command():
    result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)



class utility_functions:

    def thinking():
        think = '-------------'
        i=0
        j=0
        end=randrange(3,9)
        think = pyfiglet.figlet_format(think, font = 'standard')
        #sleep(10)
        print(think)


    def timestamp():
        dt = datetime.now()
        ts = datetime.timestamp(dt)
        ts = str(ts)
        return ts
    
    def seperator():
        seperator = '-------------'
        sep = pyfiglet.figlet_format(seperator, font = 'standard')
        #sleep(10)
        print(sep) 




def main():
    conf = config()
    introduction()
    #install_dependencies()
    dependency_log = dependency_pipeline()
    build_log = build_pipeline()
    deploy_log = deploy_pipeline(conf.cname)


if __name__ == "__main__":
    main()
