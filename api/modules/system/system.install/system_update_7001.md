# system_update_7001()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 1924–1926 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L1924-L1926)
- **Module/theme:** system
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function system_update_7001()
```

## Documentation

```text
Generate a cron key and save it in the variables table.
```

## Code

```php
function system_update_7001() {
  variable_set('cron_key', drupal_random_key());
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
