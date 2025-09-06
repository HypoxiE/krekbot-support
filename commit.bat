@echo off
REM Скрипт для коммита и пуша в Git
setlocal enabledelayedexpansion
chcp 65001

REM Переход в директорию проекта (при необходимости)
cd /d "%~dp0"

set count=0

for /f "usebackq delims=" %%A in ("version.txt") do (
	set /a count+=1

	if !count! EQU 1 set "description=%%A"
	if !count! EQU 2 set "version=%%A"

	if !count! GEQ 2 goto done
)
:done

REM Получение комментария к коммиту
set commit_msg="%description% | version: %version%"

echo %description%>version.txt
set /a version+=1
echo !version!>>version.txt

REM Добавление всех изменений
git add .

REM Создание коммита
git commit -m %commit_msg%

REM Отправка в основную ветку (main или master)
git push