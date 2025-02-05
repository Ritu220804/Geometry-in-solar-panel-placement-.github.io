import numpy as np
import matplotlib.pyplot as plt

# Function to calculate optimal tilt angle for different seasons
def seasonal_tilt_angle(latitude, day_of_year):
    if day_of_year < 80 or day_of_year > 355:  # Winter
        return latitude + 15
    elif 172 <= day_of_year <= 265:  # Summer
        return latitude - 15
    else:  # Spring/Fall
        return latitude

# Set parameters
latitude = 15.8497  # Latitude of Belgavi city
days_of_year = np.arange(1, 366)  # Days of the year

# Calculate optimal tilt angle for each day
tilt_angles = [seasonal_tilt_angle(latitude, day) for day in days_of_year]

# Daily mean tilt example for June 21st
day_of_year = 172  # June 21st
daily_mean_tilt = seasonal_tilt_angle(latitude, day_of_year)

# Seasonal mean tilt
spring_days = np.arange(80, 172)   # Spring: March 21 to June 21
summer_days = np.arange(172, 266)  # Summer: June 21 to Sep 21
fall_days = np.arange(266, 355)    # Fall: Sep 21 to Dec 21
winter_days = np.concatenate((np.arange(1, 80), np.arange(355, 366)))  # Winter: Dec 21 to March 21

spring_mean_tilt = np.mean([seasonal_tilt_angle(latitude, day) for day in spring_days])
summer_mean_tilt = np.mean([seasonal_tilt_angle(latitude, day) for day in summer_days])
fall_mean_tilt = np.mean([seasonal_tilt_angle(latitude, day) for day in fall_days])
winter_mean_tilt = np.mean([seasonal_tilt_angle(latitude, day) for day in winter_days])

# Yearly mean tilt
yearly_mean_tilt = np.mean(tilt_angles)

# Plotting
fig, ax = plt.subplots(3, 1, figsize=(10, 15))

# Plot 1: Daily mean tilt
ax[0].plot([day_of_year], [daily_mean_tilt], 'bo', label=f"Daily Mean Tilt: {daily_mean_tilt:.2f}° (June 21)")
ax[0].set_title("Daily Mean Tilt (June 21st)", fontsize=14)
ax[0].set_ylabel("Tilt Angle (degrees)", fontsize=12)
ax[0].legend(fontsize=10)
ax[0].grid(True)

# Plot 2: Seasonal mean tilt
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
season_means = [spring_mean_tilt, summer_mean_tilt, fall_mean_tilt, winter_mean_tilt]
ax[1].bar(seasons, season_means, color=['green', 'orange', 'brown', 'blue'])
ax[1].set_title("Seasonal Mean Tilt", fontsize=14)
ax[1].set_ylabel("Tilt Angle (degrees)", fontsize=12)
ax[1].grid(True)

# Rotate x-axis labels to prevent overlap
for label in ax[1].get_xticklabels():
    label.set_rotation(30)

# Plot 3: Yearly mean tilt
ax[2].plot(days_of_year, tilt_angles, label="Daily Optimal Tilt Angle")
ax[2].axhline(y=yearly_mean_tilt, color='r', linestyle='--', label=f"Yearly Mean Tilt: {yearly_mean_tilt:.2f}°")
ax[2].set_title("Yearly Optimal Tilt Angle with Mean", fontsize=14)
ax[2].set_xlabel("Day of the Year", fontsize=12)
ax[2].set_ylabel("Tilt Angle (degrees)", fontsize=12)
ax[2].legend(fontsize=10)
ax[2].grid(True)

# Adjust layout to reduce overlap
plt.tight_layout(pad=3.0)
plt.show()

# Output the mean tilt angles
print(f"Daily Mean Tilt (June 21st): {daily_mean_tilt:.2f}°")
print(f"Spring Mean Tilt: {spring_mean_tilt:.2f}°")
print(f"Summer Mean Tilt: {summer_mean_tilt:.2f}°")
print(f"Fall Mean Tilt: {fall_mean_tilt:.2f}°")
print(f"Winter Mean Tilt: {winter_mean_tilt:.2f}°")
print(f"Yearly Mean Tilt: {yearly_mean_tilt:.2f}°")
