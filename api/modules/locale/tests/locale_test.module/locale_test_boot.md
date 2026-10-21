# locale_test_boot()

- **Type:** Function
- **File:** [`modules/locale/tests/locale_test.module`](_file.md), lines 24–28 · [local source](../../../../../source/modules/locale/tests/locale_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/tests/locale_test.module#L24-L28)
- **Module/theme:** locale_test
- **Implements:** [hook_boot()](../../../system/system.api.php/hook_boot.md)

## Signature

```php
function locale_test_boot()
```

## Documentation

```text
Implements hook_boot().

For testing domain language negotiation, we fake it by setting
the HTTP_HOST here
```

## Code

```php
function locale_test_boot() {
  if (variable_get('locale_test_domain')) {
    $_SERVER['HTTP_HOST'] = variable_get('locale_test_domain');
  }
}
```

---
_Drupal 7.103 · [modules/locale/tests/locale_test.module](https://github.com/drupal/drupal/blob/7.103/modules/locale/tests/locale_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
