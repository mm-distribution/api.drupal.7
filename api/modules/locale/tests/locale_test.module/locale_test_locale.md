# locale_test_locale()

- **Type:** Function
- **File:** [`modules/locale/tests/locale_test.module`](_file.md), lines 11–16 · [local source](../../../../../source/modules/locale/tests/locale_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/tests/locale_test.module#L11-L16)
- **Module/theme:** locale_test
- **Implements:** [hook_locale()](../../locale.api.php/hook_locale.md)

## Signature

```php
function locale_test_locale($op = 'groups')
```

## Documentation

```text
Implements hook_locale().
```

## Code

```php
function locale_test_locale($op = 'groups') {
  switch ($op) {
    case 'groups':
      return array('custom' => t('Custom'));
  }
}
```

---
_Drupal 7.103 · [modules/locale/tests/locale_test.module](https://github.com/drupal/drupal/blob/7.103/modules/locale/tests/locale_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
