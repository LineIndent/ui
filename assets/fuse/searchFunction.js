(function () {
  const INPUT_ID = "buridan-search-input";
  const RESULTS_ID = "buridan-search-results";

  const FUSE_OPTIONS = {
    keys: [
      { name: "title", weight: 0.6 },
      { name: "section", weight: 0.25 },
      // { name: "description", weight: 0.15 },
    ],
    threshold: 0.3,
    ignoreLocation: true,
    includeScore: true,
    minMatchCharLength: 2,
  };

  let _fuse = null;
  let _allItems = [];

  // ─── Init ──────────────────────────────────────────────────────────────────

  window.initializeFuse = function (list) {
    try {
      _allItems = list;
      _fuse = new Fuse(list, FUSE_OPTIONS);
      window.fuseInitialized = true;
      console.log("[buridan-search] ready,", list.length, "items");
    } catch (e) {
      console.error("[buridan-search] init error", e);
    }
  };

  // ─── Public: called from trigger on_click ──────────────────────────────────
  // Wire happens here — guaranteed the input is in the DOM at this point.

  window.openSearch = function () {
    setTimeout(() => {
      _tryWire(); // always try to wire on open
      const input = document.getElementById(INPUT_ID);
      if (input) {
        input.value = "";
        input.focus();
      }
      _render("");
    }, 50);
  };

  // ─── Wire input events ─────────────────────────────────────────────────────

  function _tryWire() {
    const input = document.getElementById(INPUT_ID);
    if (!input || input._buridanWired) return;
    input._buridanWired = true;
    console.log("[buridan-search] wiring input");

    input.addEventListener("focus", function () {
      _render(this.value);
    });
    input.addEventListener("input", function () {
      _render(this.value);
    });
    input.addEventListener("keydown", function (e) {
      if (e.key === "Escape") {
        this.value = "";
        _render("");
      }
    });
  }

  // ─── Render ────────────────────────────────────────────────────────────────

  function _render(query) {
    const container = document.getElementById(RESULTS_ID);
    if (!container) return;

    const items =
      !query || !query.trim()
        ? _allItems
        : _fuse
          ? _fuse.search(query.trim()).map((r) => r.item)
          : [];

    container.innerHTML = "";

    if (!items.length) {
      container.innerHTML = `<p class="text-xs text-muted-foreground px-3 py-2 text-center">No results for "${_esc(query)}"</p>`;
      return;
    }

    const grouped = {};
    items.forEach((item) => {
      if (!grouped[item.section]) grouped[item.section] = [];
      grouped[item.section].push(item);
    });

    Object.entries(grouped).forEach(([section, sectionItems]) => {
      const label = document.createElement("p");
      label.className =
        "!text-[11px] font-semibold text-muted-foreground tracking-wider px-3 py-2";
      label.textContent = section;
      container.appendChild(label);

      sectionItems.forEach((item) => {
        const a = document.createElement("a");
        a.href = item.url.startsWith("http")
          ? item.url
          : "/" + item.url.replace(/^\//, "");
        a.className = [
          "flex flex-col gap-0.5",
          "px-3 py-2 rounded-radius",
          "cursor-pointer no-underline",
          "hover:bg-secondary transition-colors",
        ].join(" ");
        a.innerHTML = `<span class="text-sm font-medium text-foreground">${_esc(item.title)}</span>`;
        a.addEventListener("mousedown", (e) => e.preventDefault());
        container.appendChild(a);
      });
    });
  }

  // ─── Helpers ───────────────────────────────────────────────────────────────

  function _esc(s) {
    return String(s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }
})();
