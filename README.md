# Comcast Service Project

This project provides a service for managing Comcast-related operations. It includes a Python-based implementation with modular components for service logic and a main entry point for execution.

## Insights on Website Protection

The website being interacted with in this project is protected by Akamai's advanced anti-bot firewall. This adds an additional layer of security, making it challenging to perform automated tasks without proper handling. Below is a proof image showcasing the Akamai anti-bot firewall in action:

![Akamai Anti-Bot Firewall Proof](https://i.ibb.co/7dqDQzW/Screenshot-2025-08-19-at-19-26-37.png)



## Project Structure

- `comcast_service.py`: Contains the core logic and functionality of the Comcast service.
- `main.py`: The main entry point for running the service.
- `README.md`: Documentation for the project.

## Prerequisites

- Python 3.12 or higher (a test on 3.12 was made)
- Required Python packages (see below for installation)

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd comcast
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` file includes the following dependencies:

   - `botasaurus==4.0.74`: A library for browser automation, used extensively in this project for web scraping and interaction.
   - `python-dotenv==1.0.1`: A library for loading environment variables from a `.env` file, ensuring sensitive information like usernames and passwords are securely managed.

   To install these dependencies, run:
   ```bash
   pip install -r requirements.txt
   ```

3. You also need to set these ENVs in your `.env` file:

- `RESIDENTIAL_PROXY`: The proxy server address for residential IPs.
- `USERNAME`: Your username for authentication.
- `PASSWORD`: Your password for authentication.

## Usage

Run the service using the `main.py` file:
```bash
python ./main.py
```

## Features

- Modular design for Comcast service logic.
- Easy-to-use entry point for running the service.
- Anti Bot systems aware

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Feel free to reach out for any questions or issues!