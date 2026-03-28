<div align="center">

# Interpolator

A research project comparing Linear Interpolation vs Babylonian Method for square root approximation

</div>

---

## What is this?

This repository contains research on the Babylonian method (Newton-Raphson) and explores whether Linear Interpolation can serve as a faster alternative when we need to compromise on time complexity. The project includes mathematical analysis, C++ implementations, Python validation scripts, and a LaTeX research paper.

## Research Question

**Can single-pass linear interpolation provide a computationally efficient alternative to iterative methods like Newton-Raphson for square root approximation, especially when "good enough" precision is acceptable?**

---

## Project Structure

```
Interpolator/
├── research/
│   └── analysis.tex              # Full research paper (LaTeX)
├── src/
│   ├── babylonian method/
│   │   ├── main.cpp              # Newton-Raphson implementation
│   │   └── convergence.py        # Error analysis over iterations
│   └── linear-interpolation/
│       ├── interpolator.cpp      # O(1) approximation algorithm
│       └── mapping.py            # Error visualization script
└── README.md
```

---

## Mathematical Framework

### Linear Interpolation Method

For a given number `i`, we find the largest integer `a` such that `a² ≤ i`. Then:

```
β = a + (i - a²) / ((a+1)² - a²)
```

Where:
- `β` is the approximated square root
- `a` is the lower bound (floor of actual sqrt)
- The denominator represents the slope between consecutive perfect squares

### Babylonian Method (Newton-Raphson)

Iterative formula:

```
x_{n+1} = 0.5 × (x_n + S / x_n)
```

Continues until convergence: `|x_{n+1} - x_n| < ε`

---

## Key Findings

### Complexity Comparison

| Feature | Newton-Raphson | Linear Interpolation |
|---------|----------------|----------------------|
| **Time Complexity** | O(log n) per bit of precision | O(1) - Constant Time |
| **Space Complexity** | O(1) | O(1) |
| **Operations** | Iterative Division/Addition | Single-Pass Arithmetic |
| **CPU Cycles** | Variable (depends on precision) | Fixed (branchless) |

### Error Analysis Results

- **Perfect Squares**: Error = 0 (exact match)
- **Small Numbers (x < 100)**: Peak error ~0.03
- **Large Numbers (x > 500)**: Consistent error < 0.01
- **Pattern**: Sawtooth error distribution with decreasing amplitude

**Conclusion**: As x increases, the error decreases, making linear interpolation highly reliable for large numbers and mental estimation.

---

## Installation & Usage

### Prerequisites

- **C++**: GCC/G++ compiler (C++11 or later)
- **Python**: Python 3.x
- **LaTeX**: TeX distribution (for compiling research paper)

### Setup

#### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd Interpolator
```

#### 2. Install Python Dependencies

```bash
pip install numpy matplotlib
```

#### 3. LaTeX Setup (Optional)

For compiling the research paper:

- **Windows**: Install [MiKTeX](https://miktex.org/download) or [TeX Live](https://www.tug.org/texlive/)
- **Linux**: `sudo apt install texlive-full`
- **macOS**: `brew install --cask mactex`

---

## Running the Code

### Linear Interpolation (C++)

```bash
cd src/linear-interpolation
g++ interpolator.cpp -o interpolator
./interpolator
# Enter a number when prompted
```

**Example:**
```
Input: 50
Output: Approximated Square: 7.07107
```

### Babylonian Method (C++)

```bash
cd src/babylonian\ method
g++ main.cpp -o babylonian
./babylonian
# Enter a number when prompted
```

**Example:**
```
Input: 50
Output: 7.07107
```

### Error Analysis (Python)

#### Babylonian Convergence Analysis

```bash
cd src/babylonian\ method
python convergence.py
# Enter a number to see error reduction across 10 iterations
```

**Example Output:**
```
Enter number: 50
After trying 1 time, error is 0.42893
After trying 2 time, error is 0.00510
After trying 3 time, error is 0.00001
...
```

#### Linear Interpolation Error Plot

```bash
cd src/linear-interpolation
python mapping.py
# Generates sqrt_error_plot.png
```

This creates a graph showing absolute error for x values from 1 to 2000.

### Compile Research Paper (LaTeX)

```bash
cd research
pdflatex analysis.tex
pdflatex analysis.tex  # Run twice for proper references
# Generates analysis.pdf
```

Or use your LaTeX editor (Overleaf, TeXShop, etc.)

---

## Use Cases

### When to Use Linear Interpolation

 **Low-power devices** (IoT, embedded systems)  
 **Mental estimation** (quick approximations)  
 **Real-time systems** (predictable execution time)  
 **Large numbers** (x > 500, error < 0.01)  
 **Non-critical calculations** (where ±0.02 error is acceptable)

### When to Use Babylonian Method

 **High precision required** (scientific computing)  
 **Small numbers** (x < 100)  
 **Unlimited CPU cycles available**  
 **Arbitrary precision** (can continue iterating)

---

## Research Paper

The full mathematical analysis is available in `research/analysis.tex`. It includes:

- **Introduction**: Motivation and hypothetical framework
- **Mathematical Framework**: Derivation of interpolation formula
- **Complexity Analysis**: Big-O comparison
- **Results**: Error plots and observations
- **Conclusion**: Practical implications

Compile with `pdflatex` to generate the PDF.

---

## Results Visualization

The error analysis shows a distinctive **sawtooth pattern**:

- **Valleys at perfect squares** (error = 0)
- **Peaks between squares** (where √x curve diverges from linear approximation)
- **Decreasing amplitude** as x increases

For x > 500, the maximum error stabilizes below 0.01, making it suitable for most practical applications.

---

## Technical Details

### C++ Implementation Notes

- Uses `<cmath>` for `sqrt()` and `pow()` (for boundary calculation only)
- `static_cast<int>` ensures integer floor operation
- Single-pass calculation (no loops or branches)
- Suitable for embedded systems and performance-critical code

### Python Implementation Notes

- NumPy for efficient array operations
- Matplotlib for publication-quality plots
- Vectorized operations for batch error calculation

---

## Contributing

This is academic research and open for:
- Mathematical improvements
- Alternative approximation methods
- Extended error analysis
- Hardware benchmarking
- Real-world case studies

---

## License

MIT License - See LICENSE file for details

---

## Author

**Shubhankar Kumar**  
Research Date: March 27, 2026

<div align="center">

**A practical exploration of the trade-off between speed and precision**

</div>

<!-- # Interpolator
This repo is research on babylonian method and how this method can be a better alternative if we have to compromise on the time complexity -->
