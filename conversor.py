#Celsius para Fahrenheit: F = C * 1.8 + 32
def celsiusFahrenheit(Celsius):
    return Celsius * 1.8 + 32

#Fahrenheit para Celsius: C = 5 / 9 * (fahrenheit - 32)
def fahrenheitCelsius(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)

#Celsius para Kelvin K = C + 273.15
def celsiusKelvin(celsius):
    return celsius + 273.15

#Kelvin para Celsius C = K - 273,15
def kelvinCelsius(kelvin):
    return kelvin - 273.15

#Kelvin para Fahrenheit (K - 273.15) * 9 / 5 + 32
def kelvinFahrenheit(kelvin):
    return (kelvin - 273.15) * 9 / 5 + 32

#Fahrenheit para Kelvin (F - 32) * 5 / 9 + 273.15
def fahrenheitKelvin(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 + 273.15

#Celsius para Rankine C * 9 / 5 + 491.67
def celsiusRankine(celsius):
    return celsius * 9 / 5 + 491.67

#Rankine para Celsius (R - 491.67) * 5 / 9
def rankineCelsius(rankine):
    return (rankine - 491.67) * 5 / 9

#Rankine para Fahrenheit R - 459.67
def rankineFahrenheit(rankine):
    return rankine - 459.67

#Fahrenheit para Rankine F + 459,67
def fahrenheitRankine(fahrenheit):
    return fahrenheit + 459.67

#Rankine para Kelvin R * 5 / 9
def rankineKelvin(rankine):
    return rankine * 5 / 9

#Kelvin para Rankine K * 1.8
def kelvinRankine(kelvin):
    return kelvin * 1.8

#Celsius para Réaumur Re = C * 4 / 5
def celsiusReaumur(celsius):
    return celsius * 4 / 5

#Réaumur para Celsius C = Re * 5 / 4
def reaumurCelsius(reaumur):
    return reaumur * 5 / 4

#Kelvin para Réaumur Re = (K - 273.15) * 4 / 5
def kelvinReaumur(kelvin):
    return (kelvin - 273.15) * 4 / 5

#Réaumur para Kelvin K = Re * 5 / 4 + 273.15
def reaumurKelvin(reaumur):
    return reaumur * 5 / 4 + 273.15

#Fahrenheit para Réaumur Re = (F - 32) * 4 / 9
def fahrenheitReaumur(fahrenheit):
    return (fahrenheit - 32) * 4 / 9

#Réaumur para Fahrenheit F = Re * 9 / 4 + 32
def reaumurFahrenheit(reaumur):
    return reaumur * 9 / 4 + 32

#Rankine para Réaumur Re = (R - 491.67) * 4 / 9
def rankineReaumur(rankine):
    return (rankine - 491.67) * 4 / 9

#Réaumur para Rankine Ra = Re * 9 / 4 + 491.67
def reaumurRankine(reaumur):
    return reaumur * 9 / 4 + 491.67