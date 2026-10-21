# hook_cron_queue_info_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 640–644 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L640-L644)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_cron_queue_info_alter(&$queues)
```

## Documentation

```text
Alter cron queue information before cron runs.

Called by drupal_cron_run() to allow modules to alter cron queue settings
before any jobs are processesed.

@param array $queues
  An array of cron queue information.

@see hook_cron_queue_info()
@see drupal_cron_run()
```

## Code

```php
function hook_cron_queue_info_alter(&$queues) {
  // This site has many feeds so let's spend 90 seconds on each cron run
  // updating feeds instead of the default 60.
  $queues['aggregator_feeds']['time'] = 90;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_cron_queue_info_alter()".

_None found._

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
