# update_uninstall()

- **Type:** Function
- **File:** [`modules/update/update.install`](_file.md), lines 79–96 · [local source](../../../../source/modules/update/update.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.install#L79-L96)
- **Module/theme:** update
- **Implements:** [hook_uninstall()](../../system/system.api.php/hook_uninstall.md)

## Signature

```php
function update_uninstall()
```

## Documentation

```text
Implements hook_uninstall().
```

## Code

```php
function update_uninstall() {
  // Clear any variables that might be in use
  $variables = array(
    'update_check_frequency',
    'update_fetch_url',
    'update_last_check',
    'update_last_email_notification',
    'update_notification_threshold',
    'update_notify_emails',
    'update_max_fetch_attempts',
    'update_max_fetch_time',
  );
  foreach ($variables as $variable) {
    variable_del($variable);
  }
  $queue = DrupalQueue::get('update_fetch_tasks');
  $queue->deleteQueue();
}
```

---
_Drupal 7.103 · [modules/update/update.install](https://github.com/drupal/drupal/blob/7.103/modules/update/update.install) · Licensed GPL-2.0-or-later (see LICENSE)._
