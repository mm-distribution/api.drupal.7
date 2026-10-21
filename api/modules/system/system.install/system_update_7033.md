# system_update_7033()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 2316–2321 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L2316-L2321)
- **Module/theme:** system
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function system_update_7033()
```

## Documentation

```text
Move CACHE_AGGRESSIVE to CACHE_NORMAL.
```

## Code

```php
function system_update_7033() {
  if (variable_get('cache') == 2) {
    variable_set('cache', 1);
    return t('Aggressive caching was disabled and replaced with normal caching. Read the page caching section in default.settings.php for more information on how to enable similar functionality.');
  }
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
