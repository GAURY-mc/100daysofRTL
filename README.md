# 100daysofRTL

Welcome to **100daysofRTL**!  
This repository is a collection of Verilog RTL (Register Transfer Level) design examples and testbenches, created as part of a "100 Days of RTL Coding" challenge. It aims to help learners and enthusiasts understand digital design concepts by providing simple, practical examples.

## Repository Structure

The repo contains various Verilog modules and related testbenches, such as:

<!-- MODULE LIST START -->
<!-- MODULE LIST END -->

## Getting Started

To run/test any module:

1. Make sure you have a Verilog simulator (e.g., ModelSim, Icarus Verilog).
2. Clone the repository:
   ```bash
   git clone https://github.com/GAURY-mc/100daysofRTL.git
   cd 100daysofRTL
   ```
3. Compile and simulate the desired module and its testbench. For example:
   ```bash
   iverilog -o sr_latch_tb sr_latch_tb.v SR_latch.v
   vvp sr_latch_tb
   ```

## Contribution

Feel free to fork this repository and submit pull requests with new modules, improvements, or bug fixes.  
Issues and suggestions are always welcome!

## Author

- [GAURY-mc](https://github.com/GAURY-mc)

---

> This project is intended for learning and demonstration purposes.  
> For any queries, please open an issue in the repository.
