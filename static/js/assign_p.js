const calendar = document.getElementById('calendar');
const title = document.getElementById('month-title');
const prevBtn = document.getElementById('prev-month');
const nextBtn = document.getElementById('next-month');

let current = new Date();
current.setDate(1); // Always start on first of the month

const today = new Date();
today.setHours(0, 0, 0, 0); // Clean time

const months = [
  'January', 'February', 'March', 'April', 'May', 'June',
  'July', 'August', 'September', 'October', 'November', 'December'
];

const selections = {};

function getMonthKey(date) {
  const y = date.getFullYear();
  const m = (date.getMonth() + 1).toString().padStart(2, '0');
  return `${y}-${m}`;
}

function renderCalendar(date) {
  calendar.innerHTML = '';
  title.textContent = `${months[date.getMonth()]} ${date.getFullYear()}`;

  const year = date.getFullYear();
  const month = date.getMonth();
  const firstDay = new Date(year, month, 1).getDay();
  const totalDays = new Date(year, month + 1, 0).getDate();

  // Get selected days for this month
  const monthKey = getMonthKey(date);
  const selectedDays = selections[monthKey] || [];

  // Add empty cells before the 1st day
  for (let i = 0; i < firstDay; i++) {
    const empty = document.createElement('div');
    empty.classList.add('day', 'empty');
    calendar.appendChild(empty);
  }

  // Add each day
  for (let d = 1; d <= totalDays; d++) {
    const day = document.createElement('div');
    day.classList.add('day');
    day.textContent = d;

    const thisDate = new Date(year, month, d);
    thisDate.setHours(0, 0, 0, 0);

    // Mark as selected if stored in selections for this month
    if (selectedDays.includes(d)) {
      day.classList.add('selected');
    }

    if (thisDate < today) {
      day.classList.add('disabled');
    } else {
      day.addEventListener('click', () => {
        const index = selectedDays.indexOf(d);

        if (index !== -1) {
          selectedDays.splice(index, 1); // Remove selected day
          day.classList.remove('selected');
        } else {
          selectedDays.push(d); // Add selected day
          day.classList.add('selected');
        }

        // Update the selections object
        selections[monthKey] = [...selectedDays];
      });

    }

    calendar.appendChild(day);
  }
}


// Button listeners
let selectedDayOfMonth = current.getDate(); // track selected day

prevBtn.addEventListener('click', () => {
  const prevMonth = new Date(current);
  prevMonth.setMonth(prevMonth.getMonth() - 1);

  const maxDay = new Date(prevMonth.getFullYear(), prevMonth.getMonth() + 1, 0).getDate();
  prevMonth.setDate(Math.min(selectedDayOfMonth, maxDay));

  current = prevMonth;
  renderCalendar(current);
});

nextBtn.addEventListener('click', () => {
  const nextMonth = new Date(current);
  nextMonth.setMonth(nextMonth.getMonth() + 1);

  const maxDay = new Date(nextMonth.getFullYear(), nextMonth.getMonth() + 1, 0).getDate();
  nextMonth.setDate(Math.min(selectedDayOfMonth, maxDay));

  current = nextMonth;
  renderCalendar(current);
});

// Initial render
renderCalendar(current);