"""
MessageScroller component — auto-scrolling chat message container.

A self-contained JS implementation ported from @shadcn/react/message-scroller.
Handles auto-scroll-to-bottom, scroll mode tracking, resize observation,
scroll anchor items, and an animated scroll-to-bottom button.
"""

import reflex as rx
from reflex.components.component import ComponentNamespace
from reflex.utils.imports import ImportVar

from ..utils.twmerge import cn


class ClassNames:
    ROOT = "group/message-scroller relative flex size-full min-h-0 flex-col overflow-hidden"
    VIEWPORT = (
        "size-full min-h-0 min-w-0 overflow-y-auto overscroll-contain "
        "scrollbar-thin scrollbar-gutter-stable "
        "data-[autoscrolling=true]:scrollbar-none"
    )
    CONTENT = "flex h-max min-h-full flex-col gap-6"
    ITEM = "min-w-0 shrink-0"
    BUTTON = (
        "absolute left-1/2 -translate-x-1/2 bottom-4 "
        "flex items-center justify-center "
        "size-8 rounded-full border border-border bg-background text-foreground shadow-md "
        "transition-[transform,opacity] duration-200 "
        "data-[active=false]:pointer-events-none "
        "data-[active=false]:scale-95 "
        "data-[active=false]:opacity-0 "
        "data-[active=true]:scale-100 "
        "data-[active=true]:opacity-100 "
        "hover:bg-muted"
    )


BURIDAN_MESSAGE_SCROLLER_JS = """
(function () {
  const EDGE_THRESHOLD = 8;   // px from bottom to count as "at end"
  const AUTOSCROLL_RESET_MS = 180;

  // ── helpers ────────────────────────────────────────────────────────────────
  function atEnd(viewport) {
    return viewport.scrollHeight - viewport.scrollTop - viewport.clientHeight <= EDGE_THRESHOLD;
  }

  function atStart(viewport) {
    return viewport.scrollTop <= EDGE_THRESHOLD;
  }

  function scrollableState(viewport) {
    return {
      start: viewport.scrollTop > EDGE_THRESHOLD,
      end:   !atEnd(viewport),
    };
  }

  // ── BuridanMessageScrollerRoot ────────────────────────────────────────────
  function BuridanMessageScrollerRoot({
    autoScroll = false,
    defaultScrollPosition = "end",
    rootClass,
    viewportClass,
    contentClass,
    children,
  }) {
    const rootRef     = React.useRef(null);
    const viewportRef = React.useRef(null);
    const contentRef  = React.useRef(null);

    // mode: "following-bottom" | "free-scrolling"
    const modeRef            = React.useRef(autoScroll ? "following-bottom" : "free-scrolling");
    const autoscrollingRef   = React.useRef(false);
    const autoscrollTimerRef = React.useRef(null);
    const initializedRef     = React.useRef(false);

    const [showButton, setShowButton] = React.useState(false);

    // ── scroll state sync ──────────────────────────────────────────────────
    function syncState() {
      const vp = viewportRef.current;
      if (!vp) return;
      const state = scrollableState(vp);
      setShowButton(state.end);

      // Update data attributes for CSS selectors
      const root = rootRef.current;
      if (root) {
        root.toggleAttribute("data-scrollable-start", state.start);
        root.toggleAttribute("data-scrollable-end",   state.end);
      }
    }

    // ── auto-scroll to bottom ──────────────────────────────────────────────
    function scrollToEnd(behavior = "auto") {
      const vp = viewportRef.current;
      if (!vp) return;

      // Mark as autoscrolling so scrollbar hides during the scroll
      autoscrollingRef.current = true;
      vp.setAttribute("data-autoscrolling", "true");

      vp.scrollTo({ top: vp.scrollHeight, behavior });

      if (autoscrollTimerRef.current) clearTimeout(autoscrollTimerRef.current);
      autoscrollTimerRef.current = setTimeout(() => {
        autoscrollingRef.current = false;
        vp.removeAttribute("data-autoscrolling");
        syncState();
      }, AUTOSCROLL_RESET_MS);
    }

    function scrollToStart(behavior = "auto") {
      const vp = viewportRef.current;
      if (!vp) return;
      vp.scrollTo({ top: 0, behavior });
    }

    // ── user scroll intent — switches to free-scrolling ────────────────────
    function handleUserScroll() {
      if (autoscrollingRef.current) return;
      const vp = viewportRef.current;
      if (!vp) return;
      if (atEnd(vp)) {
        modeRef.current = "following-bottom";
      } else {
        modeRef.current = "free-scrolling";
      }
      syncState();
    }

    // ── content mutation observer — fires when messages are added ──────────
    React.useLayoutEffect(() => {
      const content = contentRef.current;
      if (!content) return;

      const observer = new MutationObserver(() => {
        if (!initializedRef.current) return;
        if (modeRef.current === "following-bottom" && autoScroll) {
          scrollToEnd("auto");
        } else {
          syncState();
        }
      });

      observer.observe(content, { childList: true, subtree: false });
      return () => observer.disconnect();
    }, [autoScroll]);

    // ── resize observer on viewport ────────────────────────────────────────
    React.useEffect(() => {
      const vp = viewportRef.current;
      if (!vp || typeof ResizeObserver === "undefined") return;

      const observer = new ResizeObserver(() => {
        if (modeRef.current === "following-bottom" && autoScroll) {
          scrollToEnd("auto");
        } else {
          syncState();
        }
      });

      observer.observe(vp);
      return () => observer.disconnect();
    }, [autoScroll]);

    // ── initial scroll position ────────────────────────────────────────────
    React.useLayoutEffect(() => {
      const vp = viewportRef.current;
      if (!vp || initializedRef.current) return;

      if (defaultScrollPosition === "end") {
        vp.scrollTop = vp.scrollHeight;
      } else if (defaultScrollPosition === "start") {
        vp.scrollTop = 0;
      }

      initializedRef.current = true;
      syncState();
    }, [defaultScrollPosition]);

    // ── expose scroll methods on root element for imperative use ───────────
    React.useEffect(() => {
      const root = rootRef.current;
      if (!root) return;
      root.__scrollToEnd   = (b) => scrollToEnd(b ?? "smooth");
      root.__scrollToStart = (b) => scrollToStart(b ?? "smooth");
    });

    return (
      <div ref={rootRef} className={rootClass} data-slot="message-scroller">
        <div
          ref={viewportRef}
          className={viewportClass}
          data-slot="message-scroller-viewport"
          role="region"
          aria-label="Messages"
          tabIndex={0}
          onScroll={handleUserScroll}
          onWheel={handleUserScroll}
          onTouchMove={handleUserScroll}
          onKeyDown={(e) => {
            const scrollKeys = new Set(["ArrowDown","ArrowUp","End","Home","PageDown","PageUp"," "]);
            if (scrollKeys.has(e.key)) handleUserScroll();
          }}
        >
          <div
            ref={contentRef}
            className={contentClass}
            data-slot="message-scroller-content"
            role="log"
            aria-relevant="additions"
          >
            {children}
          </div>
        </div>

        {/* Scroll-to-bottom button */}
        <button
          data-slot="message-scroller-button"
          data-active={showButton ? "true" : "false"}
          aria-hidden={!showButton}
          tabIndex={showButton ? 0 : -1}
          onClick={() => {
            modeRef.current = "following-bottom";
            scrollToEnd("smooth");
          }}
          className={[
            "absolute left-1/2 -translate-x-1/2 bottom-4",
            "flex items-center justify-center",
            "size-8 rounded-full border border-border bg-background text-foreground shadow-md",
            "transition-[transform,opacity] duration-200",
            "data-[active=false]:pointer-events-none",
            "data-[active=false]:scale-95",
            "data-[active=false]:opacity-0",
            "data-[active=true]:scale-100",
            "data-[active=true]:opacity-100",
            "hover:bg-muted cursor-pointer",
          ].join(" ")}
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="16" height="16"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
          >
            <path d="M12 5v14M5 12l7 7 7-7"/>
          </svg>
          <span style={{ position: "absolute", width: "1px", height: "1px", overflow: "hidden", clip: "rect(0,0,0,0)", whiteSpace: "nowrap" }}>
            Scroll to end
          </span>
        </button>
      </div>
    );
  }

  // ── BuridanMessageScrollerItem ─────────────────────────────────────────────
  function BuridanMessageScrollerItem({
    messageId,
    scrollAnchor = false,
    itemClass,
    children,
  }) {
    return (
      <div
        data-slot="message-scroller-item"
        data-message-id={messageId}
        data-scroll-anchor={scrollAnchor ? "true" : "false"}
        className={itemClass}
      >
        {children}
      </div>
    );
  }

  if (typeof window !== "undefined") {
    window.BuridanMessageScrollerRoot = BuridanMessageScrollerRoot;
    window.BuridanMessageScrollerItem = BuridanMessageScrollerItem;
  }

  // SSR-safe wrappers
  function BuridanMessageScrollerRootSSR(props) {
    const [mounted, setMounted] = React.useState(false);
    React.useEffect(() => { setMounted(true); }, []);
    if (!mounted || typeof BuridanMessageScrollerRoot === "undefined") return null;
    return React.createElement(BuridanMessageScrollerRoot, props);
  }

  function BuridanMessageScrollerItemSSR(props) {
    const [mounted, setMounted] = React.useState(false);
    React.useEffect(() => { setMounted(true); }, []);
    if (!mounted || typeof BuridanMessageScrollerItem === "undefined") return null;
    return React.createElement(BuridanMessageScrollerItem, props);
  }

  if (typeof window !== "undefined") {
    window.BuridanMessageScrollerRootSSR = BuridanMessageScrollerRootSSR;
    window.BuridanMessageScrollerItemSSR = BuridanMessageScrollerItemSSR;
  }
})();
"""


class MessageScrollerRoot(rx.Component):
    """
    Auto-scrolling chat container.

    Props:
        auto_scroll         — bool, auto-scroll to bottom when new messages arrive (default False)
        default_scroll_position — "start" | "end" (default "end")
    """

    tag = "BuridanMessageScrollerRootSSR"
    is_default = False

    auto_scroll: rx.Var[bool]
    default_scroll_position: rx.Var[str]
    root_class: rx.Var[str]
    viewport_class: rx.Var[str]
    content_class: rx.Var[str]

    def add_custom_code(self) -> list[str]:
        return [BURIDAN_MESSAGE_SCROLLER_JS]

    def add_imports(self) -> dict:
        return {"react": ImportVar(tag="React", is_default=True)}

    @classmethod
    def create(cls, *children, **props):
        props.setdefault("auto_scroll", False)
        props.setdefault("default_scroll_position", "end")
        props["root_class"] = cn(ClassNames.ROOT, props.pop("root_class", ""))
        props["viewport_class"] = cn(
            ClassNames.VIEWPORT, props.pop("viewport_class", "")
        )
        props["content_class"] = cn(ClassNames.CONTENT, props.pop("content_class", ""))
        return super().create(*children, **props)


class MessageScrollerItem(rx.Component):
    """
    A single item in the scroller.

    Props:
        message_id    — str, unique ID for visibility tracking
        scroll_anchor — bool, marks this item as a scroll anchor point (default False)
    """

    tag = "BuridanMessageScrollerItemSSR"
    is_default = False

    message_id: rx.Var[str]
    scroll_anchor: rx.Var[bool]
    item_class: rx.Var[str]

    def add_custom_code(self) -> list[str]:
        return [BURIDAN_MESSAGE_SCROLLER_JS]

    def add_imports(self) -> dict:
        return {"react": ImportVar(tag="React", is_default=True)}

    @classmethod
    def create(cls, *children, **props):
        props.setdefault("scroll_anchor", False)
        props["item_class"] = cn(ClassNames.ITEM, props.pop("item_class", ""))
        return super().create(*children, **props)


class MessageScroller(ComponentNamespace):
    """MessageScroller namespace."""

    root = staticmethod(MessageScrollerRoot.create)
    item = staticmethod(MessageScrollerItem.create)

    class_names = ClassNames


message_scroller = MessageScroller()
