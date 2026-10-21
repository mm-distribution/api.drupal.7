# hook_field_language_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 1582–1588 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L1582-L1588)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_attach](../../../topics/field_attach.md), [field_language](../../../topics/field_language.md)

## Signature

```php
function hook_field_language_alter(&$display_language, $context)
```

## Documentation

```text
Perform alterations on field_language() values.

This hook is invoked to alter the array of display languages for the given
entity.

@param $display_language
  A reference to an array of language codes keyed by field name.
@param $context
  An associative array containing:
  - entity_type: The type of the entity to be displayed.
  - entity: The entity with fields to render.
  - langcode: The language code $entity has to be displayed in.

@ingroup field_language
```

## Code

```php
function hook_field_language_alter(&$display_language, $context) {
  // Do not apply core language fallback rules if they are disabled or if Locale
  // is not registered as a translation handler.
  if (variable_get('locale_field_language_fallback', TRUE) && field_has_translation_handler($context['entity_type'], 'locale')) {
    locale_field_language_fallback($display_language, $context['entity'], $context['language']);
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_language_alter()".

- [field_test_field_language_alter()](../tests/field_test.module/field_test_field_language_alter.md) — `modules/field/tests/field_test.module`
- [locale_field_language_alter()](../../locale/locale.module/locale_field_language_alter.md) — `modules/locale/locale.module`

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
