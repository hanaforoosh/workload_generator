import subprocess
from utils import get_powerset

def run_docker_cmds(packages:list):
    additional_packages = ' '.join(packages)
    image_name = 'red2pac/python_'+'_'.join(packages)+':latest'

    docker_build_cmd = f'docker build --build-arg ADDITIONAL_PACKAGES="{additional_packages}" -t {image_name} ./Dockerfiles/'
    docker_push_cmd = f'docker push {image_name}'

    print(docker_build_cmd)
    try:
        subprocess.run(docker_build_cmd, shell=True, check=True)
        subprocess.run(docker_push_cmd, shell=True, check=True)
        print("Docker build completed successfully!")

    except subprocess.CalledProcessError as e:
        print("Docker build failed.")
        print("Error:", e)

if __name__ == '__main__':
    packages = ['pandas','numpy']
    pset = get_powerset(packages)
    print(pset)
    for p in pset:
        run_docker_cmds(list(p))