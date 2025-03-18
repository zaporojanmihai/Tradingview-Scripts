//@version=5
strategy("MACD Strategy", overlay=true)

// MACD settings
fastLength = 12
slowLength = 26
signalSmoothing = 9

// Calculate MACD
[macdLine, signalLine, _] = ta.macd(close, fastLength, slowLength, signalSmoothing)

// Plot MACD and Signal line
plot(macdLine, color=color.blue, title="MACD Line")
plot(signalLine, color=color.orange, title="Signal Line")

// Buy and Sell signals
buySignal = ta.crossover(macdLine, signalLine)
sellSignal = ta.crossunder(macdLine, signalLine)

// Plot buy and sell signals on the chart
plotshape(buySignal, color=color.green, style=shape.labelup, location=location.belowbar, text="BUY", size=size.small)
plotshape(sellSignal, color=color.red, style=shape.labeldown, location=location.abovebar, text="SELL", size=size.small)

// Strategy execution
strategy.entry("Buy", strategy.long, when=buySignal)
strategy.close("Buy", when=sellSignal)

// ------------------------------------------------------

//@version=5
strategy("Premium Bollinger Bands Strategy", overlay=true)

// Bollinger Bands settings
length = 20
src = close
mult = 2.0

// Bollinger Bands calculations
basis = ta.sma(src, length)
dev = mult * ta.stdev(src, length)
upper = basis + dev
lower = basis - dev

// Plot Bollinger Bands
plot(upper, color=color.red, title="Upper Band")
plot(lower, color=color.green, title="Lower Band")
plot(basis, color=color.blue, title="Middle Band (SMA)")

// Buy and Sell signals
buySignal = ta.crossover(close, lower)  // Price crosses above the lower band (buy signal)
sellSignal = ta.crossunder(close, upper)  // Price crosses below the upper band (sell signal)

// Plot buy and sell signals
plotshape(buySignal, color=color.green, style=shape.labelup, location=location.belowbar, text="BUY", size=size.small)
plotshape(sellSignal, color=color.red, style=shape.labeldown, location=location.abovebar, text="SELL", size=size.small)

// Strategy execution
strategy.entry("Buy", strategy.long, when=buySignal)
strategy.close("Buy", when=sellSignal)

// ------------------------------------------------------
