#!/usr/bin/env bash

# yodo install script

cd
update=false

case "$OSTYPE" in
	darwin*)  echo 'export PATH="~/.yodo:$PATH"'  >> ~/.bash_profile; source ~/.bash_profile ;;
	linux*)   echo 'export PATH="~/.yodo:$PATH"'  >> ~/.bashrc; source ~/.bashrc; echo 'linux' ;;
esac

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

hash git >/dev/null 2>&1 || {
    echo "Error: git is not installed"
    exit 1
}

git clone --depth=1 https://github.com/sergiouve/yoDo.git || {
	echo 'Error: git clone failed.'
	exit 1
}
mkdir .yodo
cp yoDo/. .yodo/ -R
chmod a+x -R .yodo

rm -rf ~/yoDo

if [ "$update" = true ]; then
	rm ~/.yodo/settings
	cp ~/yodo_settings_bk ~/.yodo/settings
	rm ~/yodo_settings_bk
fi

yodo whoareyou

if [ "$update" = true ]; then
	echo 'yodo was successfully updated!'
else
	echo 'yodo was successfully installed!'
fi
