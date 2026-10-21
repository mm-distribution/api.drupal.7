# locale_test_language_negotiation_info_alter()

- **Type:** Function
- **File:** [`modules/locale/tests/locale_test.module`](_file.md), lines 112–116 · [local source](../../../../../source/modules/locale/tests/locale_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/tests/locale_test.module#L112-L116)
- **Module/theme:** locale_test
- **Implements:** [hook_language_negotiation_info_alter()](../../../system/language.api.php/hook_language_negotiation_info_alter.md)

## Signature

```php
function locale_test_language_negotiation_info_alter(array &$language_providers)
```

## Documentation

```text
Implements hook_language_negotiation_info_alter().
```

## Code

```php
function locale_test_language_negotiation_info_alter(array &$language_providers) {
  if (variable_get('locale_test_language_negotiation_info_alter', FALSE)) {
    unset($language_providers[LOCALE_LANGUAGE_NEGOTIATION_INTERFACE]);
  }
}
```

---
_Drupal 7.103 · [modules/locale/tests/locale_test.module](https://github.com/drupal/drupal/blob/7.103/modules/locale/tests/locale_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
