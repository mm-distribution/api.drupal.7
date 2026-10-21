# system_update_7049()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 2539–2543 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L2539-L2543)
- **Module/theme:** system
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function system_update_7049()
```

## Documentation

```text
Rename 'Default' profile to 'Standard.'
```

## Code

```php
function system_update_7049() {
  if (variable_get('install_profile', 'standard') == 'default') {
    variable_set('install_profile', 'standard');
  }
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
