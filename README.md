# foxhole-stat-getter
Script for scraping activity from foxhole, and making nice graphs.

## Requirements
https://github.com/Goliaten/foxhole-stat-getter/blob/main/Requirements.md

## How to use
### Main script
1. Make sure Foxhole is on primary/left screen
2. Be loaded into the game (be able to walk and shoot)
3. Do NOT have f1 menu up, or any other menu for that matter
4. Launch main.py
5. Follow instructions
   1. Script will click on screen, where foxhole should be launched. Approximately in top-left corner (make sure nothing but foxhole is in that part).
   2. Exit any menu, map.
   3. (optional) If you are re-launching script, scroll to the top of regiment member list. After that exit the F1 menu
   4. Go back to script, click on cmd, click enter.
   5. Script will start working. It can take some time to scrape the activity, so make yourself something to eat and drink.
   6. If script didn't go through the entire regiment, go back to step i, and include step ii. 

## In case you want to stop script execution, move your mouse to top left corner of the screen.

### To make graphs:
1. Launch chart_maker.py
2. Write filename containing statistics (default output of main.py is "out.json")
3. Wait until graphs are done

