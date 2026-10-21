# system_date_format_types()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 3624–3630 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L3624-L3630)
- **Module/theme:** system
- **Implements:** [hook_date_format_types()](../system.api.php/hook_date_format_types.md)

## Signature

```php
function system_date_format_types()
```

## Documentation

```text
Implements hook_date_format_types().
```

## Code

```php
function system_date_format_types() {
  return array(
    'long' => t('Long'),
    'medium' => t('Medium'),
    'short' => t('Short'),
  );
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
