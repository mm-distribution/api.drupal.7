# system_date_formats()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 3635–3638 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L3635-L3638)
- **Module/theme:** system
- **Implements:** [hook_date_formats()](../system.api.php/hook_date_formats.md)

## Signature

```php
function system_date_formats()
```

## Documentation

```text
Implements hook_date_formats().
```

## Code

```php
function system_date_formats() {
  include_once DRUPAL_ROOT . '/includes/date.inc';
  return system_default_date_formats();
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
