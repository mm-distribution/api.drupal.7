# _batch_page()

- **Type:** Function
- **File:** [`includes/batch.inc`](_file.md), lines 43–96 · [local source](../../../source/includes/batch.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/batch.inc#L43-L96)

## Signature

```php
function _batch_page()
```

## Documentation

```text
Renders the batch processing page based on the current state of the batch.

@see _batch_shutdown()
```

## Code

```php
function _batch_page() {
  $batch = &batch_get();

  if (!isset($_REQUEST['id'])) {
    return FALSE;
  }

  // Retrieve the current state of the batch.
  if (!$batch) {
    $batch = batch_load($_REQUEST['id']);
    if (!$batch) {
      drupal_set_message(t('No active batch.'), 'error');
      drupal_goto();
    }
  }

  // Register database update for the end of processing.
  drupal_register_shutdown_function('_batch_shutdown');

  // Add batch-specific CSS.
  foreach ($batch['sets'] as $batch_set) {
    if (isset($batch_set['css'])) {
      foreach ($batch_set['css'] as $css) {
        drupal_add_css($css);
      }
    }
  }

  $op = isset($_REQUEST['op']) ? $_REQUEST['op'] : '';
  $output = NULL;
  switch ($op) {
    case 'start':
      // Display the full progress page on startup and on each additional
      // non-JavaScript iteration.
      $output = _batch_progress_page();
      break;

    case 'do':
      // JavaScript-based progress page callback.
      _batch_do();
      break;

    case 'do_nojs':
      // Non-JavaScript-based progress page.
      $output = _batch_progress_page();
      break;

    case 'finished':
      $output = _batch_finished();
      break;
  }

  return $output;
}
```

---
_Drupal 7.103 · [includes/batch.inc](https://github.com/drupal/drupal/blob/7.103/includes/batch.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
