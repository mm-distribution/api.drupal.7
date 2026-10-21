# hook_field_available_languages_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 1605–1612 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L1605-L1612)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_attach](../../../topics/field_attach.md), [field_language](../../../topics/field_language.md)

## Signature

```php
function hook_field_available_languages_alter(&$languages, $context)
```

## Documentation

```text
Alter field_available_languages() values.

This hook is invoked from field_available_languages() to allow modules to
alter the array of available languages for the given field.

@param $languages
  A reference to an array of language codes to be made available.
@param $context
  An associative array containing:
  - entity_type: The type of the entity the field is attached to.
  - field: A field data structure.

@ingroup field_language
```

## Code

```php
function hook_field_available_languages_alter(&$languages, $context) {
  // Add an unavailable language.
  $languages[] = 'xx';

  // Remove an available language.
  $index = array_search('yy', $languages);
  unset($languages[$index]);
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_available_languages_alter()".

- [field_test_field_available_languages_alter()](../tests/field_test.module/field_test_field_available_languages_alter.md) — `modules/field/tests/field_test.module`

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
