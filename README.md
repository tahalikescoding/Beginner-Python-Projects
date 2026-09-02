# Beginner Python Projects 🐍

A collection of beginner-friendly Python projects covering core concepts like file handling, data analysis, JSON storage, and time/date logic.

## 📂 Projects

### 1. City Time Calculator
`worldtime.py`

Calculates and displays the current time across different cities/time zones.
- Uses dictionaries, `datetime`, and `zoneinfo`

### 2. Bank Simulator (OOP)

A command-line banking system built with Python and object-oriented programming. Supports multiple account types, persistent storage, compound interest, monthly withdrawal limits, cross-account transfers, and password-protected user accounts.

## Features

- **User authentication** — registration and sign-in with password complexity rules (uppercase, lowercase, digit, special character, length bounds, no whitespace), enforced through a custom `PasswordError` exception. Includes a strong-password generator for users who don't want to pick their own.
- **Current account** — standard deposit/withdraw, no interest.
- **Savings account** — earns compound interest (monthly compounding), capped at 5 withdrawals per rolling 30-day period.
- **Premium savings account** — same mechanics as a regular savings account, but at a higher interest rate.
- **Fixed Deposit** — a locked-term account. Funds are committed for a chosen number of years at a fixed rate; withdrawal is blocked until maturity, at which point the full compounded amount is paid out and the FD closes.
- **Transfers** — move money between any two account types, with balance and withdrawal-limit checks along the way.
- **Persistent storage** — every user's account data is stored in their own JSON file, so balances, interest schedules, and withdrawal history all survive between runs.

## Class structure

| Class | Responsibility |
|---|---|
| `Bank` | User registration, sign-in, password validation and password changes. Stores credentials in `userinfo.json`. |
| `User` | Loads/writes a specific user's account data file (`<username>.json`). Also exposes convenience checks like `check_premium()` and `see_accounts()`. |
| `Account` | Base class for all account types. Handles `deposit`, `withdraw`, `get_funds`, `transfer`, and `create_account`. |
| `SavingAccount(Account)` | Adds `apply_intrest()` (compound interest, monthly, based on elapsed time since last applied) and `withdraw_limits()` / `increment_limit()` (rolling 30-day withdrawal cap). |
| `PremiumSavingAccount(SavingAccount)` | Inherits everything from `SavingAccount`; overrides only the interest rate. |
| `FixedDeposit(Account)` | Locked-term deposit. `create_fd()` funds it from an existing account; `withdraw()` blocks until maturity, then pays out principal + compound interest and closes the FD. |

## Design decisions

**Why `PremiumSavingAccount` inherits from `SavingAccount` instead of `Account` directly:**
A premium account genuinely *is* a savings account — it shares 100% of its behavior (interest calculation, withdrawal limits) and differs in exactly one number (the rate). Inheriting from `SavingAccount` means overriding one attribute instead of duplicating every method.

**Why premium and regular savings can't coexist for the same user:**
Real banks treat "premium" as a *tier* of your one savings account, not a separate account you hold alongside a regular one. Modeling it that way avoids a second, parallel set of storage keys, interest-date trackers, and withdrawal-limit trackers that would otherwise need to be kept in sync with the regular savings account's — a real source of bugs that was deliberately designed out rather than patched around.

**Why account existence is checked against the saved file, not an in-memory flag:**
An early version tracked "does this user have a savings account" with a plain Python variable (`savings = True/False`) that reset to `False` every time the program restarted — meaning a user with a real, funded savings account from a previous session would be told to "create a savings account first." The fix was to derive that fact from the actual persisted JSON (`"Saving" in details`) every time it's needed, since that's the only thing that's actually true across restarts.

**Why interest and withdrawal-limit tracking use separate date keys:**
Both features need "how much time has passed since X" logic, and an early version had them both reading and resetting the *same* stored date — meaning applying interest would silently reset the withdrawal-limit window, and vice versa. They now track independent dates (`start_saving_intrest_date` vs. `Last_resetted_date`) so the two features can't interfere with each other.


## How to run

```bash
python banksimulator.py
```

You'll be prompted to sign in or register. Once signed in, a menu lets you manage a Current account (always available) plus optionally create Savings, Premium Savings, and Fixed Deposit accounts, transfer between them, and check accrued interest.

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

### 5. Shopping App Simulator (OOP)

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
