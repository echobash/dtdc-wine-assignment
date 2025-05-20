# Wine Assignment Solver

This project solves a wine distribution optimization problem where each person provides a list of wines they are interested in. The goal is to assign wines to people while maximizing the total number of bottles distributed, subject to the following constraints:

* Each wine can be assigned to **at most one person**
* Each person can receive **up to 3 wines** from their preference list

The solution reads a TSV file (tab-separated) and outputs a list of assignments.

---

## 🚀 Setup Instructions

1. Clone the repository:

   ```bash
    git clone git@github.com:echobash/dtdc-wine-assignment.git
    cd dtdc-wine-assignment 
   ```

2. Make sure you have Python 3 installed.


## 📦 How to Run
```bash
python wine_assignment_solver.py test.txt
```

## 📦 How to Run locally with sample file
```bash
python wine_assignment_solver.py test.txt
```

I've the sample input file with 5 people, each having 10 wine preferences test.txt— perfect for verifying your logic locally:


### Example:

```bash
python wine_assignment_solver.py examples/test.txt
```

---

## 📄 Input Format

Input should be a TSV (tab-separated) file with the format:

```
person0	wineA
person0	wineB
person0	wineC
person0	wineD
person0	wineE
person0	wineF
person0	wineG
person0	wineH
person0	wineI
person0	wineJ

person1	wineB
person1	wineC
person1	wineD
person1	wineK
person1	wineL
person1	wineM
...
```

Each line represents a wine preference: a person ID and a wine ID.

---

## 🧾 Output Format

* First line: total number of bottles distributed
* Each following line: `<person_id> <TAB> <wine_id>`

### Example Output:

```
15
person0 wineA
person0 wineB
person0 wineC
person1 wineD
person1 wineK
```

---

## ⚙️ Assumptions

* Each person provides at most 10 wine preferences
* Input file can scale to several GBs; the script is optimized for large files
* No preference ranking is considered (greedy assignment based on availability)

---

## ✅ Dependencies

This project only requires the Python standard library:

* `sys`
* `collections`

No external libraries are used.
