# Extract the value from a sol file line.
# Returns a float.
def extractVal(line):
    return tuple(map(eval, line.split('    ')))[1]

# Parse the contents of a sol file into time-series components
def parse(solFile):
    # NOTE: Data for each day contains hours [0,24]. Thus, the last hour 
    # in the data is ignored, as it is already encompassed by the first
    # hour of the next day.

    # Solar data is on lines [11,34]
    SOLAR_FLUX  = list(map(extractVal, solFile[10:34]))
    # Density data is on lines [46,69]
    AIR_DENSITY = list(map(extractVal, solFile[45:69]))
    # Horizontal wind speed  data is on lines [81,104]
    WIND_SPEED  = list(map(extractVal, solFile[80:104]))
    return SOLAR_FLUX, AIR_DENSITY, WIND_SPEED


# Interpolate a series over the given interval.
def interpolate(series, START_HOUR, END_HOUR, SMOOTHING_RANGE):
    # Woe to ye who enter these arcane depths.
    # The idea is to slowly incorporate an increasing amount of the
    # terminal data-point into the current data-point over the course 
    # of the range. After every 24 hours, the hours count is reset and 
    # factor by which the terminal data-point is being incorporated increments.
    
    factor = float(1.0 / SMOOTHING_RANGE)
    diff   = factor
    hour   = 0 
    for t in range(START_HOUR, END_HOUR+1):
        hour += 1
        if hour == 24:
            hour = 0
            factor += diff
        series[t] = (1.0-factor)*series[t] + factor*series[END_HOUR+hour]
    return series

def smooth(series):
    # Range of days over which to smooth data
    smoothingRange = 10

    # Interpolate the storm's formation.
    # Dust storm begins on Sol 371, times 24 hours
    endForm   = 24*371
    startForm = 24*(371-smoothingRange)
    series = interpolate(series, startForm, endForm, smoothingRange)

    # Interpolate the storm's dissipation.
    # Dust storm ends on Sol 668, times 24 hours
    smoothingRange = 60
    endDis   = 24*668
    startDis = 24*(668-smoothingRange)
    series = interpolate(series, startDis, endDis, smoothingRange)

    return series

# Fetch all data for the given climate synthetic scenario
def getScenario(scenario):
    # Initialize time-series to empty lists
    SOLAR_FLUX, AIR_DENSITY, WIND_SPEED = [],[],[]
    # Parse every sol file and add to the lists
    for sol in range(1, 670):
        with open('data/' + scenario + '/' + str(sol).zfill(3) + '.txt') as f:
            # Strip each line of whitespace and pass it to the parser
            S,A,W = dataparser.parse([x.strip() for x in f.readlines()])
            # Concatenate the new components to each time-series
            SOLAR_FLUX  += S
            AIR_DENSITY += A
            WIND_SPEED  += W

    # Smooth transition data if the scenario is dust-storm
    if scenario == 'dust-storm':
        SOLAR_FLUX  = smooth(SOLAR_FLUX)
        AIR_DENSITY = smooth(AIR_DENSITY)
        WIND_SPEED  = smooth(WIND_SPEED)
        
    # Return the time-series
    return SOLAR_FLUX, AIR_DENSITY, WIND_SPEED

# Plot the solar flux at the Dena site versus the two different scenarios
def sunnyPlot():
    SOLAR_FLUX_DUST, AIR_DENSITY_DUST, WIND_SPEED_DUST = getScenario('dust-storm')
    SOLAR_FLUX_NORM, AIR_DENSITY_NORM, WIND_SPEED_NORM = getScenario('avg-climate')
    import matplotlib.pyplot as plt
    plt.title('How sunny is the Dena skylight? (-6.084°N 239.061°E)')
    plt.xlabel('Hours into the Martian year')
    plt.ylabel('Maximum solar flux to surface ($W/m^2$)')
    plt.plot(SOLAR_FLUX_NORM, label='Average stormless year')
    plt.plot(SOLAR_FLUX_DUST, label='Average year with global dust storm')
    plt.legend()
    plt.grid()
    plt.show()