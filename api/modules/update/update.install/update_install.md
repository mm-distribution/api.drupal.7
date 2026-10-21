# update_install()

- **Type:** Function
- **File:** [`modules/update/update.install`](_file.md), lines 71–74 · [local source](../../../../source/modules/update/update.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.install#L71-L74)
- **Module/theme:** update
- **Implements:** [hook_install()](../../system/system.api.php/hook_install.md)

## Signature

```php
function update_install()
```

## Documentation

```text
Implements hook_install().
```

## Code

```php
function update_install() {
  $queue = DrupalQueue::get('update_fetch_tasks', TRUE);
  $queue->createQueue();
}
```

---
_Drupal 7.103 · [modules/update/update.install](https://github.com/drupal/drupal/blob/7.103/modules/update/update.install) · Licensed GPL-2.0-or-later (see LICENSE)._
