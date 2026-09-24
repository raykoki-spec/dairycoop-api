# File: README.md

# API Script 
An API script with a fetch function, a process function, and an output function.
Applied on simulated readings of a dairy farm cooperative, it makes requests, transforms data, and presents the results.

## What It Does

- Process simulated readings from farm collection
- Flags farms with daily produce that are below the set target (10 L)
- Returns a summary report clearly indicating number of  farms  collected and total litres collected


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