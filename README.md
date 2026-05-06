# ⚡ Smart Appliances Energy Monitoring and Alert System

> An IoT-based system that monitors real-time energy consumption of home appliances and generates alerts when abnormal or excessive power usage is detected.

---

## 📌 Project Overview

The **Smart Appliances Energy Monitoring and Alert System** helps homeowners track and manage electricity usage at the appliance level. By combining IoT hardware with a web-based dashboard, it provides actionable insights to reduce wastage and improve energy efficiency.

**Key goals:**
- Reduce electricity wastage
- Monitor appliance-level energy usage in real time
- Generate instant alerts on abnormal consumption
- Provide a clean, browser-based dashboard for insights

---

## ⚙️ Features

- 📡 Real-time energy monitoring via IoT sensors
- 🏠 Appliance-wise power tracking
- 🔔 Alert system for high or abnormal energy usage
- 🌐 Web-based dashboard interface
- 📱 Responsive frontend design
- 🔌 Full hardware + software integration

---

## 🧰 Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python (Flask) |
| Hardware | Arduino, ACS712 Current & Voltage Sensors |

---

## 📁 Project Structure

```
smart-energy/
│
├── backend/
│   └── app.py                # Flask(backend server)
│
├── frontend/
│   ├── index.html            # Main dashboard page
│   ├── style.css             # Styling
│   └── script.js             # Frontend logic & API calls
│
├── hardware/
│   └── arduino_code.ino      # Arduino sensor code
│
├── requirements.txt          # Python dependencies
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Arduino IDE (for hardware setup)
- A browser (Chrome/Firefox recommended)

### 1. Clone the Repository

```bash
git clone https://github.com/DishaB-07/Smart-appliances-energy-mointoring-and-alert-system-.git
cd Smart-appliances-energy-mointoring-and-alert-system-
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Backend

```bash
python backend/app.py
```

### 4. Open the Frontend

Open `frontend/index.html` in your browser.

> ⚠️ Make sure the backend server is running before opening the dashboard.

---

## 🔔 Alert System

Alerts are triggered when:

- ⚠️ Power usage **exceeds a safe threshold**
- ⚡ A **sudden spike** in energy consumption is detected
- ⏱️ An appliance **runs for too long** without stopping

---

## 📊 How It Works

```
[IoT Sensors] → [Arduino] → [Backend (Python)] → [Alert Engine] → [Web Dashboard]
```

1. Current and voltage sensors collect real-time energy data
2. Arduino reads and transmits sensor data to the backend
3. Backend processes and analyzes power usage
4. Alerts are triggered if thresholds are exceeded
5. Live data and alerts are displayed on the web dashboard

---

## 🚀 Future Improvements

- ☁️ Cloud integration for remote monitoring
- 📱 Mobile application support
- 🤖 AI-based energy consumption prediction
- 📧 WhatsApp / Email alert notifications
- 📈 Advanced analytics and reporting dashboard

---

## 🏁 Conclusion

This project provides an efficient, low-cost solution to monitor and control home energy usage using IoT and modern web technologies — helping users save electricity, reduce bills, and contribute to smarter energy management.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
