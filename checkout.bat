@echo off
setlocal enabledelayedexpansion
chcp 65001

git log --oneline --graph --all

set /p user_input=Введите хэш: 

git checkout %user_input% -- .