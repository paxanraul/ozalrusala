"use strict";

(() => {
  const audio = document.getElementById("wedding-music");
  const button = document.getElementById("music-toggle");
  if (!audio || !button) return;

  let enabled = false;
  let chosen = false;
  let attempt = 0;
  audio.volume = 0.55;
  button.hidden = false;

  const reflect = () => {
    const playing = enabled && !audio.paused && !audio.muted;
    const label = playing ? "Выключить звук" : "Включить звук";
    button.setAttribute("aria-pressed", String(playing));
    button.setAttribute("aria-label", label);
    button.querySelector("span").textContent = label;
  };

  const start = async () => {
    enabled = true;
    const current = ++attempt;
    try {
      await audio.play();
    } catch {
      // Browsers may require a user gesture before allowing audible playback.
      if (current === attempt) enabled = false;
    }
    if (current === attempt) reflect();
  };

  const stop = () => {
    enabled = false;
    ++attempt;
    audio.pause();
    reflect();
  };

  const firstGesture = (event) => {
    if (chosen || button.contains(event.target)) return;
    if (event.type === "keydown" && (event.repeat || event.ctrlKey || event.metaKey || event.altKey)) return;
    // Retry within the gesture even when an earlier autoplay request is pending.
    // Safari may only grant audible playback on touchend/click.
    if (audio.paused || !enabled) void start();
  };
  const events = ["pointerdown", "touchstart", "touchend", "pointerup", "click", "keydown"];
  events.forEach((event) => window.addEventListener(event, firstGesture, { capture: true, passive: true }));

  button.addEventListener("click", () => {
    chosen = true;
    events.forEach((event) => window.removeEventListener(event, firstGesture, true));
    if (enabled) stop();
    else void start();
  });
  audio.addEventListener("playing", reflect);
  audio.addEventListener("pause", reflect);
  audio.addEventListener("error", stop);
  document.addEventListener("visibilitychange", () => {
    if (document.hidden) {
      ++attempt;
      audio.pause();
    } else if (enabled) void start();
  });
  void start();
})();
