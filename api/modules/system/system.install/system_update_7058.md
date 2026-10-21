# system_update_7058()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 2724–2726 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L2724-L2726)
- **Module/theme:** system
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function system_update_7058()
```

## Documentation

```text
Remove cron semaphore variable.
```

## Code

```php
function system_update_7058() {
  variable_del('cron_semaphore');
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
