import subprocess
from utils import get_powerset


def run_docker_cmds(packages: list):
    packages.sort()
    additional_packages = " ".join(packages)
    image_name = "red2pac/python-" + "-".join(packages) + ":latest"

    docker_build_cmd = f'docker build --build-arg ADDITIONAL_PACKAGES="{additional_packages}" -t {image_name} ./Dockerfiles/'
    docker_push_cmd = f"docker push {image_name}"
    docker_rm_cmd = f"docker rmi -f {image_name}"

    print(docker_build_cmd)
    try:
        print(docker_build_cmd)
        subprocess.run(docker_build_cmd, shell=True, check=True)
        print(docker_push_cmd)
        subprocess.run(docker_push_cmd, shell=True, check=True)
        print(docker_rm_cmd)
        subprocess.run(docker_rm_cmd, shell=True, check=True)

    except subprocess.CalledProcessError as e:
        print("Docker build failed.")
        print("Error:", e)


if __name__ == "__main__":
#    packages = [
#        "requests",
#        "numpy",
#        "pandas",
#        "matplotlib",
#        "flask",
#        "scikit-learn",
#        "tensorflow",
#        "keras",
#        "pytest",
#        "django",
#    ]
    packages = [
        "numpy",
        "flask",
        "pytest",
        "fastapi",
    ]
    pset = get_powerset(packages)
    for p in pset:
        run_docker_cmds(list(p))
