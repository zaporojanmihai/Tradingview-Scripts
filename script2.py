//@version=6
strategy("Gaussian Channel + StochRSI Long Only", overlay=true, default_qty_type=strategy.percent_of_equity, default_qty_value=100, commission_type=strategy.commission.percent, commission_value=0.1, slippage=0, initial_capital=10000)

// Date filter
startDate = timestamp("2018-01-01 00:00")
endDate = timestamp("2069-01-01 00:00")
inDateRange = time >= startDate and time <= endDate

// Gaussian Channel Calculation
length = input.int(20, title="Gaussian Channel Length")
gaussian_upper = ta.ema(high, length)
gaussian_lower = ta.ema(low, length)

// Plot Gaussian Channel
plot(gaussian_upper, color=color.blue, linewidth=2, title="Gaussian Upper Channel")
plot(gaussian_lower, color=color.orange, linewidth=2, title="Gaussian Lower Channel")

// Stochastic RSI Calculation
stoch_length = input.int(14, title="Stoch RSI Length")
smoothK = input.int(3, title="Stoch RSI K")
smoothD = input.int(3, title="Stoch RSI D")

// Calculate RSI first
rsi = ta.rsi(close, stoch_length)

// Calculate Stochastic RSI
k = ta.stoch(rsi, rsi, rsi, stoch_length)
d = ta.sma(k, smoothD)

// Plot Stochastic RSI (in separate pane)
plot(k, title="Stoch RSI K", color=color.green)
plot(d, title="Stoch RSI D", color=color.red)
hline(80, color=color.gray)
hline(20, color=color.gray)

// Entry Conditions
price_above_gaussian = close > gaussian_upper
stoch_up = k > d and k < 80  // Stochastic RSI trending up and not overbought

// Exit Conditions
price_below_gaussian = close < gaussian_upper

// Long Entry
if (price_above_gaussian and stoch_up and strategy.position_size <= 0 and inDateRange)
    strategy.entry("Long", strategy.long)

// Long Exit
if (price_below_gaussian and strategy.position_size > 0)
    strategy.close("Long")

// No shorting
