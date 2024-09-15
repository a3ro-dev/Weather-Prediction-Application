import numpy as np

class WeatherModel:
    def __init__(self, prev_temps, current_temps, prev_weather, current_weather):
        self.prev_temps = np.array(prev_temps)
        self.current_temps = np.array(current_temps)
        self.prev_weather = prev_weather
        self.current_weather = current_weather
        self.trends = [
            (0.2, "Gradual increase in temperature."),
            (-0.1, "Slight decrease in temperature."),
            (0.05, "Stable temperature with minor fluctuations."),
            (0.3, "Steady increase followed by rain."),
            (-0.2, "Gradual cooling and possible clouds."),
            (0.1, "Slight increase and sunny weather."),
            (0.15, "Increase with humidity rising."),
            (-0.25, "Cooler with chances of frost."),
            (0.0, "Stable weather without significant changes."),
            (-0.05, "Slight cooling with intermittent clouds.")
        ]
    
    def get_last_three_times(self, time_of_day):
        if time_of_day == "morning":
            return ["night", "evening", "afternoon"]
        elif time_of_day == "afternoon":
            return ["morning", "night", "evening"]
        elif time_of_day == "evening":
            return ["afternoon", "morning", "night"]
        elif time_of_day == "night":
            return ["evening", "afternoon", "morning"]
        else:
            raise ValueError("Invalid time of day")

    def exponential_smoothing(self, data, alpha=0.3):
        smoothed = np.zeros_like(data)
        smoothed[0] = data[0]
        for t in range(1, len(data)):
            smoothed[t] = alpha * data[t] + (1 - alpha) * smoothed[t - 1]
        return smoothed
    
    def predict_temperature(self, num_days, time_of_day):
        past_avg = np.mean(self.prev_temps)
        curr_avg = np.mean(self.current_temps)
        trend = (curr_avg - past_avg) / len(self.prev_temps)
        
        predictions = []
        for i in range(num_days):
            next_temp = curr_avg + trend * (i + 1)
            if time_of_day == "morning":
                next_temp -= 2
            elif time_of_day == "afternoon":
                next_temp += 2
            elif time_of_day == "evening":
                next_temp -= 1
            elif time_of_day == "night":
                next_temp -= 3
            predictions.append(next_temp)
        smoothed_predictions = self.exponential_smoothing(np.array(predictions))
        return smoothed_predictions

    def predict_weather_type(self, num_days, time_of_day):
        last_times = self.get_last_three_times(time_of_day)
        combined_weather = self.prev_weather + self.current_weather
        predicted_weather = []
        
        for _ in range(num_days):
            # Select a random trend index
            trend_idx = np.random.choice(len(self.trends))
            trend_value, trend_description = self.trends[trend_idx]

            if last_times[0] in trend_description and time_of_day == "morning":
                next_weather = "foggy"
            elif last_times[1] in trend_description and time_of_day == "afternoon":
                next_weather = "sunny"
            elif last_times[2] in trend_description and time_of_day == "evening":
                next_weather = "cloudy"
            elif time_of_day == "night":
                next_weather = "clear"
            else:
                next_weather = max(set(combined_weather), key=combined_weather.count)
            predicted_weather.append(next_weather)
        return predicted_weather

    def predict(self, num_days, time_of_day):
        predicted_temps = self.predict_temperature(num_days, time_of_day)
        predicted_weather = self.predict_weather_type(num_days, time_of_day)
        return predicted_temps, predicted_weather

    def display_predictions(self, predicted_temps, predicted_weather):
        print(f"Predicted Temperatures: {predicted_temps}")
        print(f"Predicted Weather Types: {predicted_weather}")

# Example usage
if __name__ == "__main__":
    prev_temps = [25, 26, 27]  # Previous temperatures
    current_temps = [28, 29, 30]  # Current temperatures
    prev_weather = ['sunny', 'cloudy', 'rainy']  # Past weather types
    current_weather = ['sunny', 'rainy', 'cloudy']  # Current weather types

    num_days_to_predict = int(input("How many days to predict? "))
    time_of_day = input("Enter the time of day (morning, afternoon, evening, night): ").strip().lower()

    weather_model = WeatherModel(prev_temps, current_temps, prev_weather, current_weather)
    predicted_temps, predicted_weather = weather_model.predict(num_days_to_predict, time_of_day)
    weather_model.display_predictions(predicted_temps, predicted_weather)
