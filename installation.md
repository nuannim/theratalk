# how to run uvicorn
```bash
uvicorn main:app --reload
```

<br>

# 1. install requirements.txt
```bash
pip install -r requirements.txt
```
<br>

# 2. install chocolatey
install requirements.txt เสร็จ ลง choco ต่อ (https://docs.chocolatey.org/en-us/choco/setup/)

## install with cmd
```bash
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[System.Net.ServicePointManager]::SecurityProtocol = 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
```
## install with powershell
```bash
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

<br>

# 3. install torch cuda
install torch cuda แทน torch ตัวเก่า  
torch cuda ทำให้รันเอไอบน gpu ได้ (https://pytorch.org/get-started/locally/)
```bash
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```


<br>


---


<br>

# how to install node & express

download node.js (LTS version recommended)  
https://nodejs.org/en/download

เช็ค node.js version

```bash
node -v
```

or

```bash
node --version
```

ติดตั้ง express ที่มาจาก node package manager (npm)

```bash
npm init -y
npm install express
```

- express ช่วยให้ไม่ต้องเขียน server.js เอง เหมือน fastapi ใน python
- จะสร้าง project ใหม่ก็ลง express ใหม่
- ไม่ต้องอัพ node_module ขึ้น github เพราะมันลงเครื่องใครเครื่องมันได้ ผลลัพธ์เหมือนกัน
    
    ```bash
    my-project/
    ├── package.json
    ├── package-lock.json
    ├── server.js
    ├── public/
    │   ├── index.html
    │   ├── styles.css
    │   └── script.js
    ├── views/
    │   └── template.ejs
    ├── .gitignore
    ```
    

รัน js แบบไม่ต้องกดปิดเปิดใหม่ ให้ลง `nodemon`

เช็คว่ามีในเครื่องยัง(+เช็ค version)

```bash
nodemon -v
```

install nodemon

```bash
npm install -g nodemon
```
---
<br>

# how to install express ejs sqlite3
```bash
npm init -y
npm install express ejs sqlite3
```

```bash
npm init -y
npm install express ejs sqlite3 express-session cookie-parser
```
