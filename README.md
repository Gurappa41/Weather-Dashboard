# 🌦️ Weather Dashboard

A web-based Weather Dashboard developed using **Python and Django** with the **OpenWeather API**.  
The application allows users to search for a city and view current weather information or a 5-day weather forecast.

## ✨ Features

- 🌤️ View current weather information
- 📅 View 5-day weather forecast
- 🌡️ Temperature and feels-like temperature
- 💧 Humidity
- 🌬️ Wind speed
- ⏱️ Atmospheric pressure
- 👁️ Visibility
- 🌍 Country information
- 🔎 Search weather by city
- 🎨 Weather-themed and responsive user interface

## 🛠️ Technologies Used

- **Python**
- **Django**
- **HTML5**
- **CSS3**
- **OpenWeather API**
- **Requests**

## 📂 Project Structure

```text
climate_project/
│
├── climate_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── Dashboard/
│   ├── migrations/
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── static/
│   └── images/
│       └── back_clouds.jpg
│
├── templates/
│   ├── climate_forcast_base.html
│   ├── forcast.html
│   └── index.html
│
├── db.sqlite3
├── manage.py
└── README.md
```

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd climate_project
```

### 2. Install the required packages

```bash
pip install django requests
```

### 3. Configure the OpenWeather API

The application uses the OpenWeather API to retrieve weather information.

Before running the project, configure your OpenWeather API key.

### 4. Start the Django development server

```bash
python manage.py runserver
```

### 5. Open the application

Open the following address in your browser:

```text
http://127.0.0.1:8000/
```

## 🌐 Application Pages

### 🏠 Home

The home page provides navigation to:

- Current Weather
- Weather Forecast

### 🌤️ Current Weather

Displays real-time weather information for the selected city, including:

- Temperature
- Feels-like temperature
- Humidity
- Pressure
- Wind speed
- Visibility
- Country

### 📅 Weather Forecast

Displays forecast information including:

- Date and time
- Temperature
- Weather condition
- Humidity
- Wind speed

## 📸 Screenshots

Add screenshots of the following pages to the repository:

- Home Page
- Current Weather
- Weather Forecast

## 🔗 API

This project uses the **OpenWeather API** for retrieving current weather and forecast data.

## 📌 Future Improvements

- Add better error handling for invalid city names
- Display daily forecast summaries
- Add automatic location detection
- Add more weather details
- Deploy the application online

## 👨‍💻 Author

**Gurappa**

B.Tech – Computer Science & Engineering (AI & ML)

## 📄 License

This project was developed for learning and portfolio purposes.
