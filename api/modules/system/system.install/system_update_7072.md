# system_update_7072()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 3227–3229 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L3227-L3229)
- **Module/theme:** system
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function system_update_7072()
```

## Documentation

```text
Remove the obsolete 'site_offline_message' variable.

@see update_fix_d7_requirements()
```

## Code

```php
function system_update_7072() {
  variable_del('site_offline_message');
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
