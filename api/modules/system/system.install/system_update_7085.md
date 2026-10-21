# system_update_7085()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 3383–3385 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L3383-L3385)
- **Module/theme:** system
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function system_update_7085()
```

## Documentation

```text
Remove FLoC-blocking variable.
```

## Code

```php
function system_update_7085() {
  variable_del('block_interest_cohort');
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
