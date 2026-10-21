# system_update_7069()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 3186–3188 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L3186-L3188)
- **Module/theme:** system
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function system_update_7069()
```

## Documentation

```text
Remove the obsolete 'site_offline' variable.

@see update_fix_d7_requirements()
```

## Code

```php
function system_update_7069() {
  variable_del('site_offline');
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
