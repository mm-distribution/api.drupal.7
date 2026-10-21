# locale_test_language_types_info_alter()

- **Type:** Function
- **File:** [`modules/locale/tests/locale_test.module`](_file.md), lines 76–80 · [local source](../../../../../source/modules/locale/tests/locale_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/tests/locale_test.module#L76-L80)
- **Module/theme:** locale_test
- **Implements:** [hook_language_types_info_alter()](../../../system/language.api.php/hook_language_types_info_alter.md)

## Signature

```php
function locale_test_language_types_info_alter(array &$language_types)
```

## Documentation

```text
Implements hook_language_types_info_alter().
```

## Code

```php
function locale_test_language_types_info_alter(array &$language_types) {
  if (variable_get('locale_test_content_language_type', FALSE)) {
    unset($language_types[LANGUAGE_TYPE_CONTENT]['fixed']);
  }
}
```

---
_Drupal 7.103 · [modules/locale/tests/locale_test.module](https://github.com/drupal/drupal/blob/7.103/modules/locale/tests/locale_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
