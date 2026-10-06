# Travel & Commute Weather Planner

A practical Python application that determines whether a daily commute is possible based on travel distance, current weather conditions, and available transportation methods.

This project focuses on writing clean conditional logic and utilizing nested control flows to evaluate dynamic real-world scenarios.

## 🚀 Features
* Evaluates commute possibility based on critical variables (`distance_mi`, `is_raining`, `has_bike`, etc.).
* Implements short-circuit conditional structures (`if-elif-else`) to classify distance categories.
* Combines boolean flags with logical operators (`and`, `or`, `not`) to enforce strict safety constraints (e.g., preventing cycling/walking in rainy weather).
* Safely handles edge cases like zero distance values (`falsy` evaluation).

## 🧠 Concepts Practice
* **Control Flow:** Designing nested conditional logic and chained `elif` blocks.
* **Logical Operators:** Structuring complex statements using `and` for dual requirements and `or` for multiple alternatives.
* **Falsy Evaluation:** Identifying empty or zero numeric values efficiently without extra comparisons.

## 🛠️ How to Run
Ensure you have Python installed, then run the script using your terminal:
```bash
python main.py
```
