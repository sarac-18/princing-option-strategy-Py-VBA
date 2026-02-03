# Option Pricing with Monte Carlo Simulation  
## Bull Put Spread with Asian Options

## Project Overview
This project focuses on the pricing of an options trading strategy known as a **Bull Put Spread**, composed of **Asian put options**.  
The implementation is developed using **Python and VBA** and follows a standard and reusable framework for option pricing.

The pricing methodology is based on **Monte Carlo simulation**, allowing the valuation of the strategy under multiple simulated market scenarios.

## Strategy Description
The **Bull Put Spread** is constructed by combining two Asian put options with different strike prices:

- **Long one out-of-the-money (OTM) Put option**
- **Short one in-the-money (ITM) Put option**

The overall payoff of the strategy is obtained by summing the payoffs of the individual options strike by strike.

### Asian Option Payoff
For an Asian option, the payoff depends on the average value of the underlying asset over the life of the option:

- Put option payoff: max(K - S(T), 0)

where:
- K = average price of the underlying during the option's lifetime
- S(T) = underlying price at maturity

## Input Data
- **Trade date:** 20-12-2021  
- **Underlying price:** 4,568.02 points  
- **Option maturity date:** 21-12-2018  
- **Risk-free interest rate:** 0.19%  
- **Implied volatility:** 24% (assumed constant)  
- **Value per point (futures contract):** 50 USD  

For the construction of the **risk graph**, underlying prices are generated at intervals of **10 points**, with lower and upper bounds set at **±20% of the current underlying price**.

## Methodology
The project applies a **Monte Carlo simulation approach** with \( N \) simulations and multiple scenarios to estimate the expected payoff of the options strategy.  
The framework is modular and can be easily extended to price different option strategies or alternative payoff structures.

### Python Implementation
- `numpy`  
- `datetime`  
- `scipy`  
- `math`  
- `matplotlib.pyplot`

### Project Structure Python
- Read.me is important beacause there are the input to price the options strategy  : input datasets  
- `Bull-put-spread-python.ipynb`  : Jupyter Notebook containing the analysis

### VBA Implementation
## Requirements
- Microsoft Excel  
- Macros enabled  


## How to Run
1. Open the `.xlsm` file  
2. Enable macros  
4. Run the VBA procedures from the interface or VBA editor  


## Results
The project produces:
- The **value of the Bull Put Spread strategy at maturity**
- A **payoff diagram** illustrating the strategy’s behavior at expiration

## Notes
This project is designed as a **general-purpose option pricing framework** and can be adapted to evaluate a wide range of derivative strategies.
