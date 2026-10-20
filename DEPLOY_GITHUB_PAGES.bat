@echo off
title Deploy to GitHub Pages
echo ========================================================
echo   Deploying Environmental Science & Technology Study Suite to GitHub Pages
echo ========================================================
echo.
echo Step 1: Committing all files locally...
git add index.html Study_Material Research_Papers_Study README.md
git commit -m "Update ES1.101 Interactive Study Suite"
echo.
echo Step 2: Push to your GitHub repository:
echo   If using GitHub CLI:
echo     gh repo create es1101-study-suite --public --source=. --push
echo.
echo   Or manual push:
echo     git branch -M main
echo     git push -u origin main
echo.
echo Check repository Settings -^> Pages to confirm deployment!
pause
