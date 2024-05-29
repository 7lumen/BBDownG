#!/bin/bash



if [ -d ./dist ];then
    rm -rf ./dist &>/dev/null
fi

if [ -d ./build ]; then
    rm -rf ./build &>/dev/null
fi

pyinstaller -w -F -n BBDownG --icon='./UI/icon.ico' ./main.py --clean -y

mkdir BBDownG &>/dev/null

rm -rf ./build &>/dev/null
mv ./dist/BBDownG ./BBDownG/

rm -rf ./dist

read -p '按回车退出！'
exit
