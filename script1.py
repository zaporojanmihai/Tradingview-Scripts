//@version=6
strategy("Gaussian Channel with Stochastic RSI Strategy", overlay=true, initial_capital=10000, default_qty_type=strategy.percent_of_equity, default_qty_value=100, commission_type=strategy.commission.percent, commission_value=0.1)

// Strategy date range
startDate = timestamp(2018, 1, 1, 0, 0)
endDate = timestamp(2069, 1, 1, 0, 0)
timeInRange = time >= startDate and time <= endDate

// Gaussian Channel parameters
length = input.int(20, "Gaussian Channel Length", minval=1)
mult = input.float(2.0, "Gaussian Channel Multiplier", minval=0.1, step=0.1)

// Stochastic RSI parameters
stochLength = input.int(14, "Stochastic Length", minval=1)
rsiLength = input.int(14, "RSI Length", minval=1)
kSmooth = input.int(3, "K Smoothing", minval=1)
dSmooth = input.int(3, "D Smoothing", minval=1)

// Gaussian Channel calculation
basis = ta.sma(close, length)
dev = ta.stdev(close, length)
upper = basis + mult * dev
lower = basis - mult * dev

// Stochastic RSI calculation
rsi1 = ta.rsi(close, rsiLength)
k = ta.sma(ta.stoch(rsi1, rsi1, rsi1, stochLength), kSmooth)
d = ta.sma(k, dSmooth)
stochUp = k > d

// Plotting
plot(basis, "Gaussian Channel Basis", color=color.blue)
plot(upper, "Gaussian Channel Upper", color=color.green)
plot(lower, "Gaussian Channel Lower", color=color.red)

// Entry and exit conditions
entryCondition = close > upper and stochUp and timeInRange
exitCondition = close < upper and timeInRange

// Strategy
if (entryCondition)
    strategy.entry("Buy", strategy.long)

if (exitCondition)
    strategy.close("Buy")

// Plot Stochastic RSI on a separate pane
indicator_name = "Stochastic RSI"
indicator_section = "StochRSI"
plotStochK = plot(k, "Stoch RSI K", color=color.blue, linewidth=2, display=display.pane)
plotStochD = plot(d, "Stoch RSI D", color=color.red, linewidth=2, display=display.pane)
hline(80, "Overbought", color=color.gray, linestyle=hline.style_dashed)
hline(20, "Oversold", color=color.gray, linestyle=hline.style_dashed)