"use strict";

const WEDDING_DATE = new Date("2026-11-14T18:00:00+03:00").getTime();
const countdown = document.getElementById("countdown");
const celebration = document.getElementById("celebration-message");
const countdownNote = document.getElementById("countdown-note");
const fields = Object.fromEntries(
  [...document.querySelectorAll("[data-unit]")].map((field) => [field.dataset.unit, field]),
);

function updateCountdown() {
  const remaining = WEDDING_DATE - Date.now();
  if (remaining <= 0) {
    countdown.hidden = true;
    countdownNote.hidden = true;
    celebration.hidden = false;
    return false;
  }

  const totalSeconds = Math.floor(remaining / 1000);
  const values = {
    days: Math.floor(totalSeconds / 86400),
    hours: Math.floor((totalSeconds % 86400) / 3600),
    minutes: Math.floor((totalSeconds % 3600) / 60),
    seconds: totalSeconds % 60,
  };
  for (const [unit, value] of Object.entries(values)) {
    fields[unit].textContent = String(value).padStart(2, "0");
  }
  countdown.hidden = false;
  return true;
}

let timer;
if (updateCountdown()) {
  timer = window.setInterval(() => {
    if (!updateCountdown()) window.clearInterval(timer);
  }, 1000);
}

document.addEventListener("visibilitychange", () => {
  if (!document.hidden) updateCountdown();
});

// Content stays visible by default, including when JavaScript is unavailable.
if ("IntersectionObserver" in window && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
  const observer = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      if (entry.isIntersecting) {
        entry.target.classList.remove("will-reveal");
        observer.unobserve(entry.target);
      }
    }
  }, { threshold: 0.08 });

  document.querySelectorAll(".reveal").forEach((element) => {
    if (element.getBoundingClientRect().top > window.innerHeight) {
      element.classList.add("will-reveal");
      observer.observe(element);
    }
  });
}
