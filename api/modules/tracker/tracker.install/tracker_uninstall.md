# tracker_uninstall()

- **Type:** Function
- **File:** [`modules/tracker/tracker.install`](_file.md), lines 11–14 · [local source](../../../../source/modules/tracker/tracker.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.install#L11-L14)
- **Module/theme:** tracker
- **Implements:** [hook_uninstall()](../../system/system.api.php/hook_uninstall.md)

## Signature

```php
function tracker_uninstall()
```

## Documentation

```text
Implements hook_uninstall().
```

## Code

```php
function tracker_uninstall() {
  variable_del('tracker_index_nid');
  variable_del('tracker_batch_size');
}
```

---
_Drupal 7.103 · [modules/tracker/tracker.install](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.install) · Licensed GPL-2.0-or-later (see LICENSE)._
