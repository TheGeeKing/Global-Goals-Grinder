# Global-Goals-Grinder

Grind some money on Samsung Global Goals app to donate to good causes :)

# Table of contents

1. [Installation](#1-installation)
2. [BASIC GRINDER](#2-basic-grinder)
   1. [Auto Scroll (ManualXY)](#1-auto-scroll-manualxy)
3. [ADVANCED GRINDERS (Recommended)](#3-advanced-grinders-recommended)
   1. [Auto Scroll (AutoXY)](#1-auto-scroll-autoxy)
   2. [Auto Watch Ads](#2-auto-watch-ads)
4. [Proof](#4-proof)
5. [Why?](#5-why)

## 1. Installation

1. Download files.
2. Enable developer mode and USB debugging.
3. Connect your phone to your computer with a cable.
4. Open the app and **pin it**.
5. Open cmd in the folder you want to use.
6. and run `py <filename>.py`

## 2. BASIC GRINDER

### 1. Auto Scroll (ManualXY)

#### 1.1. Stats

- 10 minutes grinded 0.95$.

Samsung double every donation so 0.95\*2 = 1.90$ in 10 minutes.

#### 1.2 Installation

1. Open the app, go in 'Updates' tab and stay at the top.
2. Run `py global_goals_auto_scroll_inputXY.py`.

#### 1.3. What it does?

1.  It asks for X and Y of different elements (money counter, back button). **/!\ You need developer mode to know X and Y of elements.**
2.  It sets brightness to 0% to save battery.
3.  It taps on the money counter.
4.  It swipe down to display ads.
5.  It taps on the back button.
6.  Repeat steps 3-5.

#### 1.4. How it works?

- It uses adb.

#### 1.5. Why?

- It's a basic grinder.
- It's cross-platform.
- It's easy to use.
- It's fast.

## 3. ADVANCED GRINDERS (Recommended)

### 1. Auto Scroll (AutoXY)

#### 1.1. Stats

- 10 minutes grinded 0.95$.

Samsung double every donation so 0.95\*2 = 1.90$ in 10 minutes.

#### 1.2 Installation

1. Open the app, go in 'Updates' tab and stay at the top.
2. Run `py global_goals_auto_scroll_autoXY.py`.

#### 1.3. What it does?

1.  It set automatically X and Y of elements.
2.  It sets brightness to 0% to save battery.
3.  It taps on the money counter.
4.  It swipe down to display ads.
5.  It taps on the back button.
6.  Repeat steps 3-5.

#### 1.4. How it works?

- It uses adb.

#### 1.5. Why?

1.  It's faster to setup than manual XY.
2.  It's more reliable.

### 2. Auto Watch Ads

#### 2.1. Stats

- 10 minutes grinded 0.61$.

Samsung double every donation so 0.61\*2 = 1.22$ in 10 minutes.

#### 2.2 Installation

1. Open the app, go in 'Updates' tab and search for a viewable ad.
2. Run `py global_goals_auto_watch_ads.py`.

#### 2.3. What it does?

1.  It finds a viewable ad and tap on it.
2.  It waits for the ad to be finished and close it.
3.  It clicks on 'OK' button.
4.  Repeat steps 1-3.

#### 2.4. How it works?

- It uses adb, pyscrcpy and opencv image recognition.

#### 2.5. Why?

- Less money/min, more complicated, but makes money.

## 4. Proof

Proof1: A screenshot of all the money I donated through this automation.
Proof2: Auto Scroll (AutoXY) doing his job for 2 minutes and grinded 0.33€(which are doubled by Samsung).

## 5. Why?

Good question. Because. GAFAM offer a way to give money to important causes. Why wouldn't you want to contribute?

Made by **MMA | TheGeeKing** with 🧀 and 🍪.
