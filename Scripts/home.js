const expenses = [
  {
    date: { day: "Friday", month: "August", date: "25" },
    details: "Income Tax",
    amount: "Rs. 80,000"
  },
  {
    date: { day: "Saturday", month: "September", date: "09" },
    details: "Rent",
    amount: "Rs. 15,000"
  },
  {
    date: { day: "Saturday", month: "September", date: "09" },
    details: "Cable Tv",
    amount: "Rs. 1,500"
  }
];

const container = document.getElementById("row2_col2");

for (let i = 0; i < expenses.length; i++) {
  const expense = expenses[i];
  const div = document.createElement("div");
  div.classList.add("row2_col2_col1");

  const dateSection = document.createElement("section");
  dateSection.classList.add("fp_date");

  const time = document.createElement("time");
  time.classList.add("icon");

  const em = document.createElement("em");
  em.textContent = expense.date.day;

  const strong = document.createElement("strong");
  strong.textContent = expense.date.month;

  const span = document.createElement("span");
  span.textContent = expense.date.date;

  time.appendChild(em);
  time.appendChild(strong);
  time.appendChild(span);
  dateSection.appendChild(time);

  const detailsSection = document.createElement("section");
  detailsSection.classList.add("fp_details");
  detailsSection.textContent = expense.details;

  const amountSection = document.createElement("section");
  amountSection.classList.add("fp_entry");
  amountSection.textContent = expense.amount;

  div.appendChild(dateSection);
  div.appendChild(detailsSection);
  div.appendChild(amountSection);

  container.appendChild(div);
}
