check_env() {
    if [ -z $2 ]; then
        echo "Please set $1"
fi
}


export PYTHON_ROOT=
export PYTHON_VERSION=3.7

export CC=

check_env PYTHON_ROOT ${PYTHON_ROOT}
check_env PYTHON_VERSION ${PYTHON_VERSION}
check_env CC ${CC}

export LDSHARED=${CC}