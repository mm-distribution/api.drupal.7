# locale_theme()

- **Type:** Function
- **File:** [`modules/locale/locale.module`](_file.md), lines 453–465 · [local source](../../../../source/modules/locale/locale.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module#L453-L465)
- **Module/theme:** locale
- **Implements:** [hook_theme()](../../system/system.api.php/hook_theme.md)

## Signature

```php
function locale_theme()
```

## Documentation

```text
Implements hook_theme().
```

## Code

```php
function locale_theme() {
  return array(
    'locale_languages_overview_form' => array(
      'render element' => 'form',
    ),
    'locale_languages_configure_form' => array(
      'render element' => 'form',
    ),
    'locale_date_format_form' => array(
      'render element' => 'form',
    ),
  );
}
```

---
_Drupal 7.103 · [modules/locale/locale.module](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module) · Licensed GPL-2.0-or-later (see LICENSE)._
