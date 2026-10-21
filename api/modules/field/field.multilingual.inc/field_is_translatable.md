# field_is_translatable()

- **Type:** Function
- **File:** [`modules/field/field.multilingual.inc`](_file.md), lines 175–177 · [local source](../../../../source/modules/field/field.multilingual.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.multilingual.inc#L175-L177)
- **Module/theme:** field
- **Topics:** [field_language](../../../topics/field_language.md)

## Signature

```php
function field_is_translatable($entity_type, $field)
```

## Documentation

```text
Checks whether a field has language support.

A field has language support enabled if its 'translatable' property is set to
TRUE, and its entity type has at least one translation handler registered.

@param $entity_type
  The type of the entity the field is attached to.
@param $field
  A field data structure.

@return
  TRUE if the field can be translated.
```

## Code

```php
function field_is_translatable($entity_type, $field) {
  return $field['translatable'] && field_has_translation_handler($entity_type);
}
```

---
_Drupal 7.103 · [modules/field/field.multilingual.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.multilingual.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
