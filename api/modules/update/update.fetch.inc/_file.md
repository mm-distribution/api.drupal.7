# modules/update/update.fetch.inc

- **Source:** [local](../../../../source/modules/update/update.fetch.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.fetch.inc) · 431 lines
- **Module/theme:** update

## File documentation

```text
@file
Code required only when fetching information about available updates.
```

## Functions (derived index)

- [update_manual_status()](update_manual_status.md) — Page callback: Checks for updates and displays the update status report.
- [update_fetch_data_batch()](update_fetch_data_batch.md) — Implements callback_batch_operation().
- [update_fetch_data_finished()](update_fetch_data_finished.md) — Implements callback_batch_finished().
- [_update_fetch_data()](_update_fetch_data.md) — Attempts to drain the queue of tasks for release history data to fetch.
- [_update_process_fetch_task()](_update_process_fetch_task.md) — Processes a task to fetch available update data for a single project.
- [_update_refresh()](_update_refresh.md) — Clears out all the cached available update data and initiates re-fetching.
- [_update_create_fetch_task()](_update_create_fetch_task.md) — Adds a task to the queue for fetching release history data for a project.
- [_update_build_fetch_url()](_update_build_fetch_url.md) — Generates the URL to fetch information about project updates.
- [_update_get_fetch_url_base()](_update_get_fetch_url_base.md) — Returns the base of the URL to fetch available update data for a project.
- [_update_cron_notify()](_update_cron_notify.md) — Performs any notifications that should be done once cron fetches new data.
- [update_parse_xml()](update_parse_xml.md) — Parses the XML of the Drupal release history info files.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
