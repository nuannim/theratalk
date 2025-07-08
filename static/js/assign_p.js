const calendar = document.getElementById('calendar');
const title = document.getElementById('month-title');
const prevBtn = document.getElementById('prev-month');
const nextBtn = document.getElementById('next-month');

let current = new Date();
current.setDate(1); // Always start on first of the month

const today = new Date();
today.setHours(0, 0, 0, 0); // Clear time for comparison

const months = [
  'January', 'February', 'March', 'April', 'May', 'June',
  'July', 'August', 'September', 'October', 'November', 'December'
];

// Store selections as ISO date strings for clarity
const selections = new Set();

// Utility to format Date object as YYYY-MM-DD string
function formatDate(date) {
  const y = date.getFullYear();
  const m = (date.getMonth() + 1).toString().padStart(2, '0');
  const d = date.getDate().toString().padStart(2, '0');
  return `${y}-${m}-${d}`;
}

function renderCalendar(date) {
  calendar.innerHTML = '';
  title.textContent = `${months[date.getMonth()]} ${date.getFullYear()}`;

  const year = date.getFullYear();
  const month = date.getMonth();
  const firstDay = new Date(year, month, 1).getDay();
  const totalDays = new Date(year, month + 1, 0).getDate();

  // Add empty cells before first day of month
  for (let i = 0; i < firstDay; i++) {
    const empty = document.createElement('div');
    empty.classList.add('day', 'empty');
    calendar.appendChild(empty);
  }

  // Add each day cell
  for (let d = 1; d <= totalDays; d++) {
    const day = document.createElement('div');
    day.classList.add('day');
    day.textContent = d;

    const thisDate = new Date(year, month, d);
    thisDate.setHours(0, 0, 0, 0);
    const dateStr = formatDate(thisDate);

    // Mark day as selected if in selections set
    if (selections.has(dateStr)) {
      day.classList.add('selected');
    }

    // Disable past dates
    if (thisDate < today) {
      day.classList.add('disabled');
    } else {
      day.addEventListener('click', () => {
        if (selections.has(dateStr)) {
          selections.delete(dateStr);
          day.classList.remove('selected');
        } else {
          selections.add(dateStr);
          day.classList.add('selected');
        }
      });
    }

    calendar.appendChild(day);
  }
}

// Navigation buttons
prevBtn.addEventListener('click', () => {
  current.setMonth(current.getMonth() - 1);
  current.setDate(1);
  renderCalendar(current);
});

nextBtn.addEventListener('click', () => {
  current.setMonth(current.getMonth() + 1);
  current.setDate(1);
  renderCalendar(current);
});

// Function to get all selected dates as array of strings
function getSelectedDates() {
  return Array.from(selections).sort();
}

// Initial render
renderCalendar(current);

// For debugging: print selected dates on button click
document.querySelector('.forbut .but').addEventListener('click', () => {
  console.log('Selected dates:', getSelectedDates());
});

const steps = document.querySelectorAll('.con');
let currentStep = 0;

function goToStep(index) {
  steps.forEach((step, i) => {
    step.classList.toggle('active', i === index);
  });
  currentStep = index;
}

const backButtons = document.querySelectorAll('.forbut .back');

backButtons.forEach(button => {
  button.addEventListener('click', () => {
    goToStep(currentStep - 1); // Go one step back
  });
});
const nextButtons = document.querySelectorAll('.forbut .next');

nextButtons.forEach((button, i) => {
  button.addEventListener('click', () => {
    if (i === 0) {
      // Step 0 → Step 1: check selected dates
      if (selections.size === 0) {
        alert('กรุณาเลือกวันที่อย่างน้อย 1 วัน');
        return;
      }
    } else if (i === 1) {
      // Step 1 → Step 2: check lessons
      const checked = document.querySelectorAll('.con.active input[type="checkbox"]:checked');
      if (checked.length === 0) {
        alert('กรุณาเลือกแบบฝึกหัดอย่างน้อย 1 รายการ');
        return;
      }
    }

    goToStep(currentStep + 1); // Go to next step
  });
});

nextButtons[nextButtons.length - 1].addEventListener('click', () => {
  alert('ส่งข้อมูลสำเร็จ!');

  // Redirect to another page (change URL to what you want)
  window.location.href = 'home_p.html'; // Replace with your desired page
});
