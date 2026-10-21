# system_batch_page()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 2402–2418 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L2402-L2418)
- **Module/theme:** system

## Signature

```php
function system_batch_page()
```

## Documentation

```text
Default page callback for batches.
```

## Code

```php
function system_batch_page() {
  require_once DRUPAL_ROOT . '/includes/batch.inc';
  $output = _batch_page();

  if ($output === FALSE) {
    drupal_access_denied();
    drupal_exit();
  }
  elseif (isset($output)) {
    // Force a page without blocks or messages to
    // display a list of collected messages later.
    drupal_set_page_content($output);
    $page = element_info('page');
    $page['#show_messages'] = FALSE;
    return $page;
  }
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
