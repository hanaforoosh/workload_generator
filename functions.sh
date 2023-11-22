createfn() {
    if [ $# -ne 3 ]; then
        echo "Usage: fission_create_function <function_name> <environment> <code_file>"
        return 1
    fi

    local code_file=$1
    local function_name=$2
    local environment=$3

    fission fn create --code "$code_file" --name "$function_name" --env "$environment" --ft 600
}

deletefn() {
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

listfn() {
    if [ $# -ne 0 ]; then
        echo "Usage: fission_create_function <function_name> <environment> <code_file>"
        return 1
    fi

    fission fn list
}

listenv() {
    if [ $# -ne 0 ]; then
        echo "Usage: fission_create_function <function_name> <environment> <code_file>"
        return 1
    fi

    fission env list
}