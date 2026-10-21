# system_update_7070()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 3204–3207 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L3204-L3207)
- **Module/theme:** system
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function system_update_7070()
```

## Documentation

```text
Remove the obsolete 'drupal_badge_color' and 'drupal_badge_size' variables.
```

## Code

```php
function system_update_7070() {
  variable_del('drupal_badge_color');
  variable_del('drupal_badge_size');
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
