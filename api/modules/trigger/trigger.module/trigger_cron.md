# trigger_cron()

- **Type:** Function
- **File:** [`modules/trigger/trigger.module`](_file.md), lines 447–456 · [local source](../../../../source/modules/trigger/trigger.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module#L447-L456)
- **Module/theme:** trigger
- **Implements:** [hook_cron()](../../system/system.api.php/hook_cron.md)

## Signature

```php
function trigger_cron()
```

## Documentation

```text
Implements hook_cron().
```

## Code

```php
function trigger_cron() {
  $aids = trigger_get_assigned_actions('cron');
  $context = array(
    'group' => 'cron',
    'hook' => 'cron',
  );
  // Cron does not act on any specific object.
  $object = NULL;
  actions_do(array_keys($aids), $object, $context);
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.module](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module) · Licensed GPL-2.0-or-later (see LICENSE)._
