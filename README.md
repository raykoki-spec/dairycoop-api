# File: README.md

# API Script 
An API script configuration at the top, a fetch function that only makes the request, a process function that only transforms data, and an output function that only presents results. Keeping them separate makes the code easier to test, debug, and extend. Day 25 is the Week 5 project: combining everything into a multi-endpoint API dashboard

## What It Does

- Flag farms with minimum  produce of 10L per day
- Process simulated readings from farm collection
- Returns a summary report clearly indicating number of farms collescted and total litres collected


## Setup

```bash
pip install -r requirements.txt
```

## Usage

```python
def process_readings(readings, min_litres):
    total = sum(r["litres"] for r in readings)
    top = max(readings, key=lambda r: r["litres"])

    
    print(f"  Total litres:      {summary['total_litres']:.1f} L")
    print(f"  Top farm:          {summary['top_farm']} ({summary['top_litres']} L)")
```

## Sample Output

```
 Total litres:      142.0 L
 Top farm:          Koki's farm (33 L) 
```

## Stack

Python

Built-in Modules: `json`