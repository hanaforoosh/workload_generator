createfn() {
    if [ $# -ne 2 ]; then
        echo "Usage: fission_create_function <function_name> <environment> <code_file>"
        return 1
    fi
    local function_name=$1
    local environment=$2

    fission fn create --code "$function_name".py --name "$function_name" --env "$environment" --ft 9000
}

delfn() {
    if [ $# -ne 1 ]; then
        echo "Usage: fission_create_function <function_name> <environment> <code_file>"
        return 1
    fi

    local function_name=$1

    fission fn delete --name "$function_name"
}

testfn() {
    if [ $# -ne 1 ]; then
        echo "Usage: fission_create_function <function_name> <environment> <code_file>"
        return 1
    fi

    local function_name=$1

    fission fn test --name "$function_name"
}

followfn() {
    if [ $# -ne 1 ]; then
        echo "Usage: fission_create_function <function_name> <environment> <code_file>"
        return 1
    fi

    local function_name=$1

     fission fn logs -f --name "$function_name"
}

getfn() {
    if [ $# -ne 1 ]; then
        echo "Usage: fission_create_function <function_name> <environment> <code_file>"
        return 1
    fi

    local function_name=$1

    fission fn get --name "$function_name"
}

listfn() {
    if [ $# -ne 0 ]; then
        echo "Usage: fission_create_function <function_name> <environment> <code_file>"
        return 1
    fi

    fission fn list
}



createenv() {
    if [ $# -ne 1 ]; then
        echo "Usage: fission_create_function <function_name> <environment> <code_file>"
        return 1
    fi
    local environment=$1

    fission env create --name "$environment" --image red2pac/"$environment"
}

delenv() {
    if [ $# -ne 1 ]; then
        echo "Usage: fission_create_function <function_name> <environment> <code_file>"
        return 1
    fi

    local env_name=$1

    fission env delete --name "$env_name"
}

getenv() {
    if [ $# -ne 1 ]; then
        echo "Usage: fission_create_function <function_name> <environment> <code_file>"
        return 1
    fi
    local environment=$1

    fission env get --name "$environment"
}

listenv() {
    if [ $# -ne 0 ]; then
        echo "Usage: fission_create_function <function_name> <environment> <code_file>"
        return 1
    fi

    fission env list
}