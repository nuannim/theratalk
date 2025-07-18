# install requirements.txt
```bash
pip install -r requirements.txt
```

# how to run uvicorn
```bash
uvicorn main:app --reload
```

---

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
