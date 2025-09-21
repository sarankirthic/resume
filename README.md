# resume
My resume in a flask server

---

## Features

- Serves a single PDF file (`sarankirthic.pdf`) on the `/` route.
- Uses Waitress for a production-grade WSGI server.
- Easy to deploy on Ubuntu or any Linux-based headless server.
- Can be managed with systemd as a service.

---

## Requirements

- Python 3.13
- Flask
- Waitress

---

## Installation

1. Clone or copy the project files to your server.
2. Create and activate a Python virtual environment (optional but recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Install dependencies:
    ```bash
    pip isntall -r requirements.txt
    ```
4. Place your resume in ```pdf/``` folder in the project directory

---

## Usage

Run the application locally (for development):

```bash
python app.py
```

Your app should be reachable at `http://localhost:8000/`.

---

## Deployment (Ubuntu Server)

- Use systemd service to manage the application:
  - Update `/etc/systemd/system/resume.service` to point to your app and virtual environment.
- Start and enable the service:

```bash
sudo systemctl daemon-reload
sudo systemctl start flaskapp.service
sudo systemctl enable flaskapp.service
```
- Use `nginx` as a reverse proxy for HTTPS and better performance (optional).

---

## Systemd Service Example
```bash
[Unit]
Description=Flask Resume Server
After=network.target

[Service]
User=your_username
WorkingDirectory=/home/your_username/app_directory
ExecStart=/home/your_username/app_directory/venv/bin/python /home/your_username/app_directory/app.py
Restart=always

[Install]
WantedBy=multi-user.target
```

---

## License

This project is licensed under the MIT License.

---