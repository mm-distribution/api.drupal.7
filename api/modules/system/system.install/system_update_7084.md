# system_update_7084()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 3376–3378 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L3376-L3378)
- **Module/theme:** system
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function system_update_7084()
```

## Documentation

```text
Rebuild JavaScript aggregates to include 'ajax.js' fix for Chrome 83.
```

## Code

```php
function system_update_7084() {
  // Empty update to force a rebuild of JS aggregates.
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
