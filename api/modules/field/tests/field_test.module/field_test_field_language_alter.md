# field_test_field_language_alter()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.module`](_file.md), lines 117–121 · [local source](../../../../../source/modules/field/tests/field_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.module#L117-L121)
- **Module/theme:** field_test_schema_alter
- **Implements:** [hook_field_language_alter()](../../field.api.php/hook_field_language_alter.md)

## Signature

```php
function field_test_field_language_alter(&$display_language, $context)
```

## Documentation

```text
Implements hook_field_language_alter().
```

## Code

```php
function field_test_field_language_alter(&$display_language, $context) {
  if (variable_get('field_test_language_fallback', TRUE)) {
    locale_field_language_fallback($display_language, $context['entity'], $context['language']);
  }
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.module](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
