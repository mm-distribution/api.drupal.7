# system_update_7047()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 2522–2524 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L2522-L2524)
- **Module/theme:** system
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function system_update_7047()
```

## Documentation

```text
Normalize the front page path variable.
```

## Code

```php
function system_update_7047() {
  variable_set('site_frontpage', drupal_get_normal_path(variable_get('site_frontpage', 'node')));
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
