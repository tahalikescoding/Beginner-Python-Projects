# Beginner Python Projects 🐍

A collection of beginner-friendly Python projects covering core concepts like file handling, data analysis, JSON storage, and time/date logic.

## 📂 Projects

### 1. City Time Calculator
`worldtime.py`

Calculates and displays the current time across different cities/time zones.
- Uses dictionaries, `datetime`, and `zoneinfo`

### 2. Banking System (JSON-based)
`betterbank.py`

A simple banking system that stores account data using JSON files.
- Sign-in and registration system with password validation
- Deposit, withdraw, and delete account operations
- Stores all data in JSON files

### 3. Timer
`timer2.py`

A countdown/stopwatch timer built with core Python logic.
- Uses the `time` module

### 4. Ballon d'Or Data Analysis
`balondoranalysis.py` + `balonwinners.csv`

Analyzes historical Ballon d'Or winner data — reads from a CSV and generates insights/stats.
- Winners by country
- Winners by club
- Player frequency
- Winner by year
- Country-wise stats
- Club-wise stats
- Search a specific club
- Search a specific country
- Search a specific player/season
- Sort seasons by goals/assists/goal contributions per game, trophies
- Compare two Ballon d'Or winning seasons
- Sort based on a custom grading system

# 5. Shopping App Simulator (OOP)

A command-line shopping cart simulator built with core Python and object-oriented design. Includes a shop-owner mode for stocking inventory and a customer mode for browsing, cart management, checkout, and order history.

## Features

- **Store owner mode** — protected by a pin, lets the owner add items (name, price, category) to build up the shop's inventory before customers can shop.
- **Customer mode** — a menu-driven flow to:
  1. Add items to cart
  2. Remove items from cart
  3. Add an item to a wishlist
  4. Checkout (validates payment amount against cart total)
  5. Search for an item by name
  6. Browse items by category
  7. View order history
  8. Exit

## Class structure

| Class    | Responsibility |
|----------|-----------------|
| `Store`  | Owns the shop's inventory (`{item: (price, category)}`). Handles adding items, searching, category lookup, and display. |
| `Cart`   | Holds a single user's in-progress cart as a list of items. |
| `User`   | Represents a customer — owns a `Cart`, a wishlist, and references the shared `Store`. Handles add/remove-from-cart, wishlist, and checkout. |
| `Orders` | Represents a completed order — takes the checked-out items and builds an order history string. |
| `Bill`   | Calculates the total amount owed for a user's cart against the store's prices. |

You'll be asked whether you're the shop owner or a customer:
- **Owner** — enter the pin (`1234`), then add items one at a time until you choose to stop.
- **Customer** — skips straight to the shopping menu.


## 🛠️ Tech Stack
- Python 3
- JSON (for data persistence)
- CSV (for data analysis)

## 🚀 How to Run
```bash
python <filename>.py
```
Each project is self-contained — just run the corresponding file.

## 📌 Status
Actively adding new beginner projects as I learn.
