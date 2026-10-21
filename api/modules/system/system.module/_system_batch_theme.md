# _system_batch_theme()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 1087–1098 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L1087-L1098)
- **Module/theme:** system

## Signature

```php
function _system_batch_theme()
```

## Documentation

```text
Theme callback for the default batch page.
```

## Code

```php
function _system_batch_theme() {
  // Retrieve the current state of the batch.
  $batch = &batch_get();
  if (!$batch && isset($_REQUEST['id'])) {
    require_once DRUPAL_ROOT . '/includes/batch.inc';
    $batch = batch_load($_REQUEST['id']);
  }
  // Use the same theme as the page that started the batch.
  if (!empty($batch['theme'])) {
    return $batch['theme'];
  }
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
