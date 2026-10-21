# locale_test_language_types_info()

- **Type:** Function
- **File:** [`modules/locale/tests/locale_test.module`](_file.md), lines 43–55 · [local source](../../../../../source/modules/locale/tests/locale_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/tests/locale_test.module#L43-L55)
- **Module/theme:** locale_test
- **Implements:** [hook_language_types_info()](../../../system/language.api.php/hook_language_types_info.md)

## Signature

```php
function locale_test_language_types_info()
```

## Documentation

```text
Implements hook_language_types_info().
```

## Code

```php
function locale_test_language_types_info() {
  if (variable_get('locale_test_language_types', FALSE)) {
    return array(
      'test_language_type' => array(
        'name' => t('Test'),
        'description' => t('A test language type.'),
      ),
      'fixed_test_language_type' => array(
        'fixed' => array('test_language_provider'),
      ),
    );
  }
}
```

---
_Drupal 7.103 · [modules/locale/tests/locale_test.module](https://github.com/drupal/drupal/blob/7.103/modules/locale/tests/locale_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
