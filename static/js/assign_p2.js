    console.log("===== assign_p2.js is working =====")


// ##### จับ activityid ใส่ list
    document.getElementById("but-next2").addEventListener("click", () => {
    console.log("===== assign_p2.js - getElementById(\"but-next2\") is working =====")
        const checkboxes = document.querySelectorAll('input[name="lesson"]');
        const selectedIds = [];

        checkboxes.forEach(checkbox => {
            if (checkbox.checked) {
            selectedIds.push(checkbox.id); // เช่น "s1", "s2"
            }
        });

        // แปลง "s1" → 1, "s2" → 2
        const mappedIds = selectedIds.map(id => {
            const match = id.match(/\d+/);
            return match ? parseInt(match[0], 10) : null;
        }).filter(n => n !== null);

        console.log("Mapped IDs:", mappedIds);

        // จัดการแสดงผลเฉพาะ dropdown ที่ตรงกับ mappedIds
        const allTemplates = document.querySelectorAll('.each-tem');
        allTemplates.forEach((tem, index) => {
            if (mappedIds.includes(index + 1)) {
            tem.style.display = "flex"; // หรือ "block" ตาม layout ที่ใช้
            } else {
            tem.style.display = "none";
            }
        });
    });

// ##### description เปลี่ยนไปตามที่เลือก dropdown (template)
    const templateDetails = {
        // * t[เลข templateid] กราบขออภัยมันต้องใส่มือ โอ้ย
        "s1-1": {
            t1: { text: "อะ อิ อึ อุ เอะ แอะ เออะ โอะ เอาะ เอียะ เอือะ อัวะ ", img: "/static/img/maxresdefault.jpg" },
            t2: { text: "อา อี อือ อู เอ แอ โอ ออ เออ เอีย เอือ อัว ฤๅ ฦๅ", img: "/static/img/maxresdefault.jpg" },
            t3: { text: "อะ อา อิ อี อึ อือ อุ อู เอะ เอ แอะ แอ โอะ โอ เอาะ ออ เออะ เออ เอียะ เอีย เอือะ เอือ อัวะ อัว ฤ ฤๅ ฦ ฦๅ อำ ใอ ไอ เอา", img: "/static/img/maxresdefault.jpg" }
        },
        "s1-2": {
            t4: { text: "คำกิริยา: กิน อาบ หิว ดู เดิน วิ่ง ฟัง ร้อน นอน ตื่น", img: null },
            t5: { text: "คำนาม: ขา มือ โต๊ะ เตียง หนัง ขวด จาน ชาม ไฟ บ้าน", img: null },
            t6: { text: "คำ 2 พยางค์: ดินสอ ยางลบ กระเป๋า รองเท้า สมุด หมอนข้าง ตู้เย็น สบู่ ขนม ไฟฟ้า", img: null }
        },
        "s1-3": {
            t7: { text: "คำคล้าย: ตา ปลา กา หมา", img: null },
            t8: { text: "คำคล้าย: ไก่ ไข่ ไม่ ใจ", img: null },
            t9: { text: "คำคล้าย: หมู หู ปู งู", img: null }
        },
        "s1-4": {
            t10: { text: "ป้าแสงเป็นคนที่รักต้นไม้มาก ทุกเช้าเธอจะรดน้ำต้นไม้หน้าบ้าน ไม่ว่าจะฝนตกหรือแดดออก วันหนึ่งต้นมะลิของป้าแสงออกดอกสวยมากจนเพื่อนบ้านเดินผ่านก็ต้องชม ป้าแสงยิ้มอย่างมีความสุข เธอเด็ดดอกมะลิไปใส่แจกันในบ้าน และพูดกับต้นไม้ว่า “ขอบใจนะ ที่เติบโตให้ป้าดูทุกวัน”", img: null },
            t11: { text: "วันนั้นพยากรณ์อากาศแจ้งว่าฝนจะตก ลุงแม้นกำลังจะไปตลาด แต่ลืมร่มไว้ในบ้าน พอเดินไปถึงหน้าซอย ฝนก็ตกหนัก ลุงแม้นเลยวิ่งกลับมาหลบใต้ชายคาบ้านเพราะไม่มีร่ม เขานั่งรอจนฝนซา แล้วจึงเดินไปตลาดใหม่ ถึงแม้จะเปียกนิดหน่อย แต่ลุงแม้นก็ยังอารมณ์ดี", img: null },
            t12: { text: "พี่แป้งตื่นเช้ามาทำกับข้าวให้แม่ พี่แป้งคิดไม่ออกว่าจะทำอะไรดี เลยเปิดตู้เย็นเจอไข่ 2 ฟองกับต้นหอมเล็กน้อย พี่แป้งเลยตอกไข่ ใส่ต้นหอม แล้วทอดเป็นไข่เจียวหอมกรุ่น แม่เดินออกมาจากห้องและพูดว่า “หอมจังเลยลูก น่ากินมาก” พี่แป้งยิ้มด้วยความภูมิใจ", img: null }
        },
        "s1-5": {
            t14: { text: "ตา หู จมูก ปาก มือ แขน ขา เท้า นิ้ว ฟัน เล็บ ข้อศอก เข่า ผม คิ้ว ลิ้น", img: null },
            t16: { text: "จาน ชาม ช้อน ส้อม มีด แก้วน้ำ หม้อ กระทะ ตู้เย็น ถังขยะ แปรงสีฟัน ยาสีฟัน แชมพู โถส้วม ฝักบัว เก้าอี้ โต๊ะ", img: null },
            t17: { text: "ตื่น แปรงฟัน ล้างหน้า อาบน้ำ แต่งตัว หวีผม กินข้าว ใส่รองเท้า ซักผ้า ล้างจาน เดิน วิ่ง ยืน นั่ง นอน เล่นโทรศัพท์", img: null }
        },
        "s1-6": {
            t19: { text: "ประโยคในชีวิตประจำวัน เช่น กินข้าวแล้ว ไปอาบน้ำ ล้างมือก่อน ตื่นได้แล้ว และอื่น ๆ", img: null },
            t20: { text: "ประโยคในชีวิตประจำวันที่ยาวขึ้น เช่น ไปทานข้าวกันไหม วันนี้เป็นยังไงบ้าง อากาศดีจังเลย กลับบ้านดี ๆ นะ และอื่น ๆ", img: null },
            t21: { text: "ประโยคคล้องจอง เช่น สาวแสนสวยใส่สร้อยสามสิบสองเส้น และอื่น ๆ", img: null }
        },
        "s1-7": {
            t1: { text: "-", img: null },
            t2: { text: "-", img: null },
            t3: { text: "-", img: null }
        },
        "s1-8": {
            t22: { text: "ประโยคในชีวิตประจำวัน เช่น ไปทานข้าวกันไหม วันนี้เป็นยังไงบ้าง", img: null },
            t23: { text: "ประโยคในชีวิตประจำวันที่ยาวขึ้น เช่น เมื่อเช้านี้ฉันตื่นสาย ฉันกำลังจัดห้องทำงานใหม่", img: null },
            t24: { text: "ประโยคในชีวิตประจำวันที่ยาวขึ้นอีก เช่น ฉันวางแผนว่าจะเริ่มเรียนภาษาที่สามในปีหน้า", img: null }
        },
        "s1-9": {
            t1: { text: "-", img: null },
            t2: { text: "-", img: null },
            t3: { text: "-", img: null }
        },
    };

    function updateTemplateInfo(select) {
        const selectId = select.id;
        const selectedValue = select.value;
        console.log(`Updating info for select ID: ${selectId}, selected value: ${selectedValue}`);
        const content = templateDetails[selectId]?.[selectedValue];
        console.log('Content from templateDetails:', content);

        const eachTem = select.closest(".each-tem");
        const rightTem = eachTem.querySelector(".right-tem");
        const textBox = rightTem.querySelector("p");
        const imageBox = rightTem.querySelector("img");



        if (content) {
            if (textBox) {
                textBox.textContent = content.text || "";
            }
            if (imageBox) {
                if (content.img) {
                    imageBox.src = content.img;
                    imageBox.style.display = "block";
                } else {
                    imageBox.style.display = "none";
                }
            }
        }
    }

    // ✅ เพิ่ม event listener และแสดงผลเริ่มต้นทันทีเมื่อโหลดหน้า
    document.addEventListener("DOMContentLoaded", () => {
        document.querySelectorAll("select[id^='s1-']").forEach(select => {
            select.addEventListener("change", () => updateTemplateInfo(select));
            updateTemplateInfo(select); // 👈 แสดงผลทันทีตามค่าเริ่มต้น
        });
    });

    // ##### Function to save selected template values
    function saveSelectedTemplates() {
        console.log("===== assign_p2.js - saveSelectedTemplates() is working =====");
        const selectedTemplates = [];
        document.querySelectorAll(".each-tem").forEach(eachTem => {
            // Check if the parent container (.each-tem) is visible
            if (eachTem.style.display !== "none") {
                const select = eachTem.querySelector("select[id^='s1-']");
                if (select) {
                    const activityIdMatch = select.id.match(/s1-(\d+)/);
                    const templateIdMatch = select.value.match(/t(\d+)/);

                    if (activityIdMatch && templateIdMatch) {
                        selectedTemplates.push({
                            activityid: parseInt(activityIdMatch[1], 10),
                            templateid: parseInt(templateIdMatch[1], 10)
                        });
                    }
                }
            }
        });
        console.log("Selected Templates:", selectedTemplates);
        return selectedTemplates;
        // Here you can send `selectedTemplates` to the backend or store it as needed
        // Example: fetch('/save_templates', { method: 'POST', body: JSON.stringify(selectedTemplates) });
    }

    // ##### Event listener for the "Done" button
    document.getElementById("but-done").addEventListener("click", saveSelectedTemplates);

