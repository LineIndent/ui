

# Card

Displays a card with header, content, and footer.

# Installation

Copy the following code into your app directory.

### CLI

```bash
buridan add component card
```

### Manual Installation

```python
from reflex.components.component import ComponentNamespace
from reflex.vars.base import Var
from reflex_components_core.el import Div

from components.ui.component import CoreComponent


class ClassNames:
    ROOT = (
        "group/card flex flex-col gap-(--card-spacing) overflow-hidden rounded-xl bg-card "
        "py-(--card-spacing) text-sm text-card-foreground ring-1 ring-foreground/10 "
        "[--card-spacing:--spacing(4)] has-data-[slot=card-footer]:pb-0 "
        "has-[>img:first-child]:pt-0 data-[size=sm]:[--card-spacing:--spacing(3)] "
        "data-[size=sm]:has-data-[slot=card-footer]:pb-0 "
        "*:[img:first-child]:rounded-t-xl *:[img:last-child]:rounded-b-xl"
    )
    HEADER = (
        "group/card-header @container/card-header grid auto-rows-min items-start gap-1 "
        "rounded-t-xl px-(--card-spacing) has-data-[slot=card-action]:grid-cols-[1fr_auto] "
        "has-data-[slot=card-description]:grid-rows-[auto_auto] [.border-b]:pb-(--card-spacing)"
    )
    TITLE = "cn-font-heading text-base leading-snug font-medium group-data-[size=sm]/card:text-sm"
    DESCRIPTION = "text-sm text-muted-foreground"
    ACTION = "col-start-2 row-span-2 row-start-1 self-start justify-self-end"
    CONTENT = "px-(--card-spacing)"
    FOOTER = "flex items-center rounded-b-xl border-t border-input bg-muted/50 p-(--card-spacing)"


class CardRoot(Div, CoreComponent):
    size: Var[str]

    @classmethod
    def create(cls, *children, **props):
        props["data-slot"] = "card"
        if "size" in props:
            props["data-size"] = props.pop("size")
        cls.set_class_name(ClassNames.ROOT, props)
        return super().create(*children, **props)


class CardHeader(Div, CoreComponent):
    @classmethod
    def create(cls, *children, **props):
        props["data-slot"] = "card-header"
        cls.set_class_name(ClassNames.HEADER, props)
        return super().create(*children, **props)


class CardTitle(Div, CoreComponent):
    @classmethod
    def create(cls, *children, **props):
        props["data-slot"] = "card-title"
        cls.set_class_name(ClassNames.TITLE, props)
        return super().create(*children, **props)


class CardDescription(Div, CoreComponent):
    @classmethod
    def create(cls, *children, **props):
        props["data-slot"] = "card-description"
        cls.set_class_name(ClassNames.DESCRIPTION, props)
        return super().create(*children, **props)


class CardAction(Div, CoreComponent):
    @classmethod
    def create(cls, *children, **props):
        props["data-slot"] = "card-action"
        cls.set_class_name(ClassNames.ACTION, props)
        return super().create(*children, **props)


class CardContent(Div, CoreComponent):
    @classmethod
    def create(cls, *children, **props):
        props["data-slot"] = "card-content"
        cls.set_class_name(ClassNames.CONTENT, props)
        return super().create(*children, **props)


class CardFooter(Div, CoreComponent):
    @classmethod
    def create(cls, *children, **props):
        props["data-slot"] = "card-footer"
        cls.set_class_name(ClassNames.FOOTER, props)
        return super().create(*children, **props)


class Card(ComponentNamespace):
    root = staticmethod(CardRoot.create)
    header = staticmethod(CardHeader.create)
    title = staticmethod(CardTitle.create)
    description = staticmethod(CardDescription.create)
    action = staticmethod(CardAction.create)
    content = staticmethod(CardContent.create)
    footer = staticmethod(CardFooter.create)
    class_names = ClassNames


card = Card()
```


# Usage


```python
from components.ui.card import Card
```


# Anatomy 
Use the following composition to build a `Card` component.


```python
card.root(
    card.header(
        card.title(),
        card.description(),
        card.action(),
    ),
    card.content(),
    card.footer(),
)
```


# Examples

## Size

Use the `size="sm"` prop to set the size of the card to small. The small size variant uses smaller spacing.


```python
def card_small() -> rx.Component:
    feature_name = "Scheduled reports"

    return card.root(
        card.header(
            card.title(feature_name),
            card.description("Weekly snapshots. No more manual exports."),
        ),
        card.content(
            rx.el.ul(
                rx.el.li(
                    hi(
                        "ArrowRight01Icon",
                        class_name="mt-0.5 size-4 shrink-0 text-muted-foreground",
                    ),
                    rx.el.span("Choose a schedule (daily, or weekly)."),
                    class_name="flex gap-2",
                ),
                rx.el.li(
                    hi(
                        "ArrowRight01Icon",
                        class_name="mt-0.5 size-4 shrink-0 text-muted-foreground",
                    ),
                    rx.el.span("Send to channels or specific teammates."),
                    class_name="flex gap-2",
                ),
                rx.el.li(
                    hi(
                        "ArrowRight01Icon",
                        class_name="mt-0.5 size-4 shrink-0 text-muted-foreground",
                    ),
                    rx.el.span("Include charts, tables, and key metrics."),
                    class_name="flex gap-2",
                ),
                class_name="grid gap-2 py-2 text-sm",
            )
        ),
        card.footer(
            button(
                "Set up scheduled reports",
                size="sm",
                class_name="w-full",
            ),
            button(
                "See what's new",
                variant="outline",
                size="sm",
                class_name="w-full",
            ),
            class_name="flex-col gap-2",
        ),
        size="sm",
        class_name="mx-auto w-full max-w-xs my-10",
    )
```


## Spacing

In addition to the `size` prop, you can use the `--card-spacing` CSS variable to control the spacing between sections and the inset of card parts.


```python
def card_spacing() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            *[
                button(
                    item["label"],
                    variant="outline",
                    size="sm",
                    class_name=rx.cond(
                        selected_card_spacing.value == item["value"], "!bg-muted", ""
                    ),
                    on_click=selected_card_spacing.set_value(item["value"]),
                )
                for item in spacing_options
            ],
            class_name="flex gap-1 justify-start items-center w-full",
        ),
        card.root(
            card.header(
                card.title("Login to your account"),
                card.description("Enter your email below to login to your account"),
                card.action(
                    button("Sign Up", variant="link"),
                ),
            ),
            card.content(
                rx.el.form(
                    rx.el.div(
                        rx.el.div(
                            rx.el.label(
                                "Email",
                                html_for="email-spacing",
                                class_name="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70",
                            ),
                            rx.el.input(
                                id="email-spacing",
                                type="email",
                                placeholder="m@example.com",
                                required=True,
                                class_name="flex h-9 w-full rounded-md border border-input bg-transparent px-3 py-1 text-sm shadow-xs transition-colors file:border-0 file:bg-transparent file:text-sm file:font-medium text-foreground placeholder:text-muted-foreground focus-visible:outline-hidden focus-visible:ring-1 focus-visible:ring-ring disabled:cursor-not-allowed disabled:opacity-50",
                            ),
                            class_name="grid gap-2",
                        ),
                        rx.el.div(
                            rx.el.div(
                                rx.el.label(
                                    "Password",
                                    html_for="password-spacing",
                                    class_name="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70",
                                ),
                                rx.el.a(
                                    "Forgot your password?",
                                    href="#",
                                    class_name="ml-auto inline-block text-sm underline-offset-4 hover:underline",
                                ),
                                class_name="flex items-center",
                            ),
                            rx.el.input(
                                id="password-spacing",
                                type="password",
                                required=True,
                                class_name="flex h-9 w-full rounded-md border border-input bg-transparent px-3 py-1 text-sm shadow-xs transition-colors file:border-0 file:bg-transparent file:text-sm file:font-medium text-foreground placeholder:text-muted-foreground focus-visible:outline-hidden focus-visible:ring-1 focus-visible:ring-ring disabled:cursor-not-allowed disabled:opacity-50",
                            ),
                            class_name="grid gap-2",
                        ),
                        class_name="flex flex-col gap-6",
                    )
                )
            ),
            card.footer(
                button("Login", type="submit", class_name="w-full"),
                button("Login with Google", variant="outline", class_name="w-full"),
                class_name="flex-col gap-2",
            ),
            class_name=f"[--card-spacing:--spacing({selected_card_spacing.value})]",
        ),
        class_name="mx-auto grid w-full max-w-sm gap-4 my-10",
    )
```


Use negative margins with `-mx-(--card-spacing)` to make content go edge to edge while keeping it aligned with the card inset. When the edge-to-edge content sits above a footer, use `-mb-(--card-spacing)` on `card.content` to remove the section gap.


```python
def card_edge_to_edge() -> rx.Component:
    return card.root(
        card.header(
            card.title("Terms of Service"),
            card.description("Review the terms before accepting the agreement."),
        ),
        card.content(
            rx.el.div(
                rx.el.p(
                    "These terms govern your use of the workspace, including access to shared documents, project files, and collaboration tools."
                ),
                rx.el.p(
                    "You are responsible for the content you upload and for ensuring that your team has the appropriate permissions to view or edit it."
                ),
                rx.el.p(
                    "We may update features or limits as the service evolves. When those changes materially affect your workflow, we will notify your workspace administrators."
                ),
                rx.el.p(
                    "By continuing, you agree to keep your account credentials secure and to follow your organization's acceptable use policies."
                ),
                class_name="-mx-(--card-spacing) max-h-48 space-y-4 overflow-y-scroll border-input border-t bg-muted/50 px-(--card-spacing) py-4 text-sm leading-relaxed",
            ),
            class_name="-mb-(--card-spacing)",
        ),
        card.footer(
            button("Decline", variant="outline"),
            button("Accept"),
            class_name="justify-end gap-2",
        ),
        class_name="mx-auto w-full max-w-sm",
    )
```



## Image

Add an image before the card header to create a card with an image.


```python
def card_image() -> rx.Component:
    return card.root(
        rx.el.div(
            class_name="absolute inset-0 z-30 aspect-video bg-black/35",
        ),
        rx.el.img(
            src="https://avatar.vercel.sh/shadcn1",
            alt="Event cover",
            class_name="relative z-20 aspect-video w-full object-cover brightness-60 grayscale dark:brightness-40",
        ),
        card.header(
            card.action(
                badge("Featured", variant="secondary"),
            ),
            card.title("Design systems meetup"),
            card.description(
                "A practical talk on component APIs, accessibility, and shipping faster."
            ),
        ),
        card.footer(
            button("View Event", class_name="w-full"),
        ),
        class_name="relative mx-auto w-full max-w-sm pt-0",
    )
```



# API Reference

## card.root

The `card.root` component is the root container for card content.

| Prop        | Type                | Default     |
| ----------- | ------------------- | ----------- |
| `size`      | `"default" \| "sm"` | `"default"` |
| `class_name` | `string`            | -           |

## card.header

The `card.header` component is used for a title, description, and optional action.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `class_name` | `string` | -       |

## card.title

The `card.title` component is used for the card title.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `class_name` | `string` | -       |

## card.description

The `card.description` component is used for helper text under the title.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `class_name` | `string` | -       |

## card.action

The `card.action` component places content in the top-right of the header (for example, a button or a badge).

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `class_name` | `string` | -       |

## card.content

The `card.content` component is used for the main card body.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `class_name` | `string` | -       |

## card.footer

The `card.footer` component is used for actions and secondary content at the bottom of the card.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `class_name` | `string` | -       |
