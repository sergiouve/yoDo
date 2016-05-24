#!/usr/bin/env bash

# yodo install script

cd
update=false

case "$OSTYPE" in
	darwin*)  echo 'export PATH="~/.yodo:$PATH"'  >> ~/.bash_profile; source ~/.bash_profile ;;
	linux*)   echo 'export PATH="~/.yodo:$PATH"'  >> ~/.bashrc; source ~/.bashrc; echo 'linux' ;;
esac

if [ -d .yodo ]; then
	update=true
	cp ~/.yodo/settings ~/yodo_settings_bk
	rm -rf ~/.yodo
fi

git clone https://github.com/sergiouve/yoDo.git
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
