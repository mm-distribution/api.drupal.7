# hook_locale()

- **Type:** Hook (documentation function)
- **File:** [`modules/locale/locale.api.php`](_file.md), lines 19–24 · [local source](../../../../source/modules/locale/locale.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.api.php#L19-L24)
- **Module/theme:** locale
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_locale($op = 'groups')
```

## Documentation

```text
Allows modules to define their own text groups that can be translated.

@param $op
  Type of operation. Currently, only supports 'groups'.
```

## Code

```php
function hook_locale($op = 'groups') {
  switch ($op) {
    case 'groups':
      return array('custom' => t('Custom'));
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_locale()".

- [locale_locale()](../locale.module/locale_locale.md) — `modules/locale/locale.module`
- [locale_test_locale()](../tests/locale_test.module/locale_test_locale.md) — `modules/locale/tests/locale_test.module`

---
_Drupal 7.103 · [modules/locale/locale.api.php](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
