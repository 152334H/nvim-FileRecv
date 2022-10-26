#!/bin/bash
current_file="$1"

dirOf() {
    if ! [ -f "$1" ]
    then exit 1
    fi
    dirname "$(readlink -f "$1")"
}
cwd="$(dirOf "$current_file")"
proj_dir="$(dirOf "$0")"

pushd "$proj_dir" || exit 1
python3 app.py "$cwd" | tee /tmp/nvim-file-recv
popd || exit 1
