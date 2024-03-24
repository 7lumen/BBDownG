@echo off
pushd "%CD%"
CD /D "%~dp0"

set appname=BBDownG

if exist dist (
    rd dist /s /q 
 )

if exist build (
    rd build /s /q 
 )

pyinstaller -w -F -n %appname% --icon=".\UI\icon.ico" .\main.py  --clean -y

mkdir BBDownG

::整理文件夹，将打包好的程序单独提取出来，其余不用文件全部删除
rd /s /q build
move .\dist\BBDownG.exe .\BBDownG\

rd /s /q .\dist
del BBDownG.spec

pause