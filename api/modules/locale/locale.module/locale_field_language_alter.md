# locale_field_language_alter()

- **Type:** Function
- **File:** [`modules/locale/locale.module`](_file.md), lines 470–476 · [local source](../../../../source/modules/locale/locale.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module#L470-L476)
- **Module/theme:** locale
- **Implements:** [hook_field_language_alter()](../../field/field.api.php/hook_field_language_alter.md)

## Signature

```php
function locale_field_language_alter(&$display_language, $context)
```

## Documentation

```text
Implements hook_field_language_alter().
```

## Code

```php
function locale_field_language_alter(&$display_language, $context) {
  // Do not apply core language fallback rules if they are disabled or if Locale
  // is not registered as a translation handler.
  if (variable_get('locale_field_language_fallback', TRUE) && field_has_translation_handler($context['entity_type'], 'locale')) {
    locale_field_language_fallback($display_language, $context['entity'], $context['language']);
  }
}
```

---
_Drupal 7.103 · [modules/locale/locale.module](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module) · Licensed GPL-2.0-or-later (see LICENSE)._
