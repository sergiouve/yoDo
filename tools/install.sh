#!/usr/bin/env bash

# yodo install script

cd
update=false

python -c 'import sys; print(".".join(map(str, sys.version_info[:3])))' || {
    echo 'Python not detected'
    echo 'Python is required for running yodo'
    echo 'Do you want to install it now?'
}

case "$OSTYPE" in
    darwin*)  echo 'export PATH="~/.yodo:$PATH"'  >> ~/.bash_profile; source ~/.bash_profile ;;
    linux*)   echo 'export PATH="~/.yodo:$PATH"'  >> ~/.bashrc; source ~/.bashrc; echo 'linux' ;;
esac

if [ -n "$ZSH_VERSION" ]; then
    echo 'export PATH=~/.yodo:$PATH' >> ~/.zshrc; source ~/.zshrc;
fi

echo 'Checking previous installation...'

if [ -d .yodo ]; then
    update=true
    cp ~/.yodo/settings ~/yodo_settings_bk
    rm -rf ~/.yodo
fi

if [ "$update" = true ]; then
    echo 'Previous installation found. Updating...'
else
    echo 'No previous installation found. Installing...'
fi

echo '-------------------------------'

hash git >/dev/null 2>&1 || {
    echo "Error: git is not installed"
    exit 1
}

git clone --depth=1 https://github.com/sergiouve/yodo.git || {
    echo 'Error: git clone failed.'
    exit 1
}

mkdir .yodo
cp -R yodo/. .yodo/
chmod a+x -R .yodo

rm -rf ~/yoDo

if [ "$update" = true ]; then
    rm ~/.yodo/settings
    cp ~/yodo_settings_bk ~/.yodo/settings
    rm ~/yodo_settings_bk
fi

echo 'Sleeping just for the laughs...'
sleep 1
echo 'ha...'
sleep 1
echo 'ha...'
sleep 1
echo 'ha.'
sleep 2

yodo whoareyou

if [ "$update" = true ]; then
    echo 'yodo was successfully updated!'
else
    echo 'yodo was successfully installed!'
fi
