# ChangeLog {pre-4.0.0 -> 4.0.0}
**Stable beta update**

## Pc-Stat-Bot {pre-4.0.0 -> 4.0.0}:

### Main:
* 🎯 **!the program is now working stably!** 🎯
* Run is now smooth 
* The translation system is completely redone:
  * about 150+ if-else were removed
  * All translations are now contained in 1 file
* 60 FPS limit was added 
* The animations were accelerated
* Fixed a bug with Tab-System because of which it was impossible to switch Tab quickly (otherwise the program did not respond to pressing Tab zone)
* fixed a bug where the program interface did not appear
* the button for closing and minimizing the program has been combined (LB - close, RB - minimizing) 
* minimized RAM usage* (~100MB -> ~35MB) `* only on Windows`
  * this is done by clearing the already loaded logo and data in the memory of the video card
  * practically does not affect the performance of the program 
  * does not affect the performance of Windows
* fixed spelling of Russian and English
* Fixed the problem in moving the window of the Y coordinate (the problem met with 2+ monitors)
* License update: now the license in the program and on GITHUB corresponds
* Config file is now saved correct
* Fixed the display of Russian symbols
* other minor fixes
  
### The interface has been changed:  
* the top panel of the program has been changed
* the tab-bar of the program has been changed
* the terminal was redesign
* added animation when opening the program (experimental)
  
### Telegram-Bot:
* fixed keyboard movement
* translate fixed
* add emoji for actions
* fixed switching to a keyboard with mouse control
* other minor fixes

## Installer {v.1.0.1 -> v.1.1.0}:
* added animation when opening the program (experimental)
* The zip file is now unzipping correctly
* other minor fixes 
