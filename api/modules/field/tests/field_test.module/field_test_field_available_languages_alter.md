# field_test_field_available_languages_alter()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.module`](_file.md), lines 104–112 · [local source](../../../../../source/modules/field/tests/field_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.module#L104-L112)
- **Module/theme:** field_test_schema_alter
- **Implements:** [hook_field_available_languages_alter()](../../field.api.php/hook_field_available_languages_alter.md)

## Signature

```php
function field_test_field_available_languages_alter(&$languages, $context)
```

## Documentation

```text
Implements hook_field_available_languages_alter().
```

## Code

```php
function field_test_field_available_languages_alter(&$languages, $context) {
  if (variable_get('field_test_field_available_languages_alter', FALSE)) {
    // Add an unavailable language.
    $languages[] = 'xx';
    // Remove an available language.
    $index = array_search('en', $languages);
    unset($languages[$index]);
  }
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.module](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
