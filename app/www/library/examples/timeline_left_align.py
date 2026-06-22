from components.ui.timeline import timeline

left_align_date = "sm:group-data-[orientation=vertical]/timeline:absolute sm:group-data-[orientation=vertical]/timeline:-left-32 sm:group-data-[orientation=vertical]/timeline:w-20 sm:group-data-[orientation=vertical]/timeline:text-right"


def timeline_left_aligned_dates():
    return timeline.root(
        timeline.item(
            timeline.indicator(),
            timeline.separator(),
            timeline.header(
                timeline.date("Jan 2024", class_name=left_align_date),
                timeline.title("Project kickoff"),
            ),
            timeline.content("Initial planning and team onboarding."),
            step=1,
            active_step=3,
        ),
        timeline.item(
            timeline.indicator(),
            timeline.separator(),
            timeline.header(
                timeline.date("Feb 2024", class_name=left_align_date),
                timeline.title("Design phase"),
            ),
            timeline.content("Wireframes and prototypes completed."),
            step=2,
            active_step=3,
        ),
        timeline.item(
            timeline.indicator(),
            timeline.separator(),
            timeline.header(
                timeline.date("Mar 2024", class_name=left_align_date),
                timeline.title("Development"),
            ),
            timeline.content("Core features implemented."),
            step=3,
            active_step=3,
        ),
        timeline.item(
            timeline.indicator(),
            timeline.separator(),
            timeline.header(
                timeline.date("Apr 2024", class_name=left_align_date),
                timeline.title("Launch"),
            ),
            timeline.content("Public release."),
            step=4,
            active_step=3,
        ),
        orientation="vertical",
    )
