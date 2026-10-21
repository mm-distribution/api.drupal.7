# trigger_install()

- **Type:** Function
- **File:** [`modules/trigger/trigger.install`](_file.md), lines 52–55 · [local source](../../../../source/modules/trigger/trigger.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.install#L52-L55)
- **Module/theme:** trigger
- **Implements:** [hook_install()](../../system/system.api.php/hook_install.md)

## Signature

```php
function trigger_install()
```

## Documentation

```text
Implements hook_install().
```

## Code

```php
function trigger_install() {
  // Do initial synchronization of actions in code and the database.
  actions_synchronize();
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.install](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.install) · Licensed GPL-2.0-or-later (see LICENSE)._
