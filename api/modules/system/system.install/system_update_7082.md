# system_update_7082()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 3362–3364 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L3362-L3364)
- **Module/theme:** system
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function system_update_7082()
```

## Documentation

```text
Add 'jquery-extend-3.4.0.js' to the 'jquery' library.
```

## Code

```php
function system_update_7082() {
  // Empty update to force a rebuild of hook_library() and JS aggregates.
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
