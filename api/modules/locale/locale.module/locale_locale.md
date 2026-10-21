# locale_locale()

- **Type:** Function
- **File:** [`modules/locale/locale.module`](_file.md), lines 264–269 · [local source](../../../../source/modules/locale/locale.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module#L264-L269)
- **Module/theme:** locale
- **Implements:** [hook_locale()](../locale.api.php/hook_locale.md)

## Signature

```php
function locale_locale($op = 'groups')
```

## Documentation

```text
Implements hook_locale().
```

## Code

```php
function locale_locale($op = 'groups') {
  switch ($op) {
    case 'groups':
      return array('default' => t('Built-in interface'));
  }
}
```

---
_Drupal 7.103 · [modules/locale/locale.module](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module) · Licensed GPL-2.0-or-later (see LICENSE)._
