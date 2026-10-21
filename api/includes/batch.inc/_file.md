# includes/batch.inc

- **Source:** [local](../../../source/includes/batch.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/batch.inc) · 498 lines

## File documentation

```text
@file
Batch processing API for processes to run in multiple HTTP requests.

Note that batches are usually invoked by form submissions, which is
why the core interaction functions of the batch processing API live in
form.inc.

@see form.inc
@see batch_set()
@see batch_process()
@see batch_get()
```

## Functions (derived index)

- [batch_load()](batch_load.md) — Loads a batch from the database.
- [_batch_page()](_batch_page.md) — Renders the batch processing page based on the current state of the batch.
- [_batch_do()](_batch_do.md) — Does one execution pass with JavaScript and returns progress to the browser.
- [_batch_progress_page()](_batch_progress_page.md) — Outputs a batch processing page.
- [_batch_process()](_batch_process.md) — Processes sets in a batch.
- [_batch_api_percentage()](_batch_api_percentage.md) — Formats the percent completion for a batch set.
- [_batch_current_set()](_batch_current_set.md) — Returns the batch set being currently processed.
- [_batch_next_set()](_batch_next_set.md) — Retrieves the next set in a batch.
- [_batch_finished()](_batch_finished.md) — Ends the batch processing.
- [_batch_shutdown()](_batch_shutdown.md) — Shutdown function: Stores the current batch data for the next request.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
