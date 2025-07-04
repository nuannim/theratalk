# how to run uvicorn
```bash
uvicorn main:app --reload
```

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


# ข้อตกลงในการใช้ซอฟต์แวร์
### ข้อตกลงในการใช้ซอฟต์แวร์ 
ซอฟต์แวร์นี้เป็นผลงานที่พัฒนาขึ้นโดย นางสาว อินทิรา ธนัพประภัศร์ นางสาว ปนัสยา บุญประกอบ และ นาย สรวิชญ์ กาญจนสันติศักดิ์ จากสถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง ภายใต้การดูแลของ ดร. ศิรสิทธิ์ โล่ห์ชนะจิต ภายใต้โครงการ เทอร่า ทอล์ก ซึ่งสนับสนุนโดย สำนักงานพัฒนาวิทยาศาสตร์และเทคโนโลยีแห่งชาติ โดยมีวัตถุประสงค์เพื่อส่งเสริมให้นักเรียนและนักศึกษาได้เรียนรู้และฝึกทักษะในการพัฒนาซอฟต์แวร์ ลิขสิทธิ์ของซอฟต์แวร์นี้จึงเป็นของผู้พัฒนา ซึ่งผู้พัฒนาได้อนุญาตให้สำนักงานพัฒนาวิทยาศาสตร์และเทคโนโลยีแห่งชาติ เผยแพร่ซอฟต์แวร์นี้ตาม “ต้นฉบับ” โดยไม่มีการแก้ไขดัดแปลงใด ๆ ทั้งสิ้น ให้แก่บุคคลทั่วไปได้ใช้เพื่อประโยชน์ส่วนบุคคลหรือประโยชน์ทางการศึกษาที่ไม่มีวัตถุประสงค์ในเชิงพาณิชย์ โดยไม่คิดค่าตอบแทนการใช้ซอฟต์แวร์ ดังนั้นสำนักงานพัฒนาวิทยาศาสตร์และเทคโนโลยีแห่งชาติ จึงไม่มีหน้าที่ในการดูแล บำรุงรักษา จัดการอบรมการใช้งาน หรือพัฒนาประสิทธิภาพซอฟต์แวร์ รวมทั้งไม่รับรองความถูกต้องหรือประสิทธิภาพการทำงานของซอฟต์แวร์ ตลอดจนไม่รับประกันความเสียหายต่าง ๆ อันเกิดจากการใช้ซอฟต์แวร์นี้ทั้งสิ้น

### License Agreement 
This software is a work developed by Indira Thanabpraphas, Panatsaya Boonprakob and Sorawit Kanjanasantisak from King Mongkut's Institute of Technology Ladkrabang under the provision of Dr. Sirasit Lochanachit under TheraTalk Project, which has been supported by the National Science and Technology Development Agency (NSTDA), in order to encourage pupils and students to learn and practice their skills in developing software. Therefore, the intellectual property of this software shall belong to the developer and the developer gives NSTDA a permission to distribute this software as an “as is” and non-modified software for a temporary and non-exclusive use without remuneration to anyone for his or her own purpose or academic purpose, which are not commercial purposes. In this connection, NSTDA shall not be responsible to the user for taking care, maintaining, training, or developing the efficiency of this software. Moreover, NSTDA shall not be liable for any error, software efficiency and damages in connection with or arising out of the use of the software.”
