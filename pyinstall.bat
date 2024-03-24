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

::�����ļ��У�������õĳ��򵥶���ȡ���������಻���ļ�ȫ��ɾ��
rd /s /q build
move .\dist\BBDownG.exe .\BBDownG\

rd /s /q .\dist
del BBDownG.spec

pause