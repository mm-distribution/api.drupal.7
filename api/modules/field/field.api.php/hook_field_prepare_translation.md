# hook_field_prepare_translation()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 696–705 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L696-L705)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_types](../../../topics/field_types.md), [field_language](../../../topics/field_language.md)

## Signature

```php
function hook_field_prepare_translation($entity_type, $entity, $field, $instance, $langcode, &$items, $source_entity, $source_langcode)
```

## Documentation

```text
Define custom prepare_translation behavior for this module's field types.

@param $entity_type
  The type of $entity.
@param $entity
  The entity for the operation.
@param $field
  The field structure for the operation.
@param $instance
  The instance structure for $field on $entity's bundle.
@param $langcode
  The language associated to $items.
@param $items
  $entity->{$field['field_name']}[$langcode], or an empty array if unset.
@param $source_entity
  The source entity from which field values are being copied.
@param $source_langcode
  The source language from which field values are being copied.

@ingroup field_language
```

## Code

```php
function hook_field_prepare_translation($entity_type, $entity, $field, $instance, $langcode, &$items, $source_entity, $source_langcode) {
  // If the translating user is not permitted to use the assigned text format,
  // we must not expose the source values.
  $field_name = $field['field_name'];
  $formats = filter_formats();
  $format_id = $source_entity->{$field_name}[$source_langcode][0]['format'];
  if (!filter_access($formats[$format_id])) {
    $items = array();
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_prepare_translation()".

- [text_field_prepare_translation()](../modules/text/text.module/text_field_prepare_translation.md) — `modules/field/modules/text/text.module`

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
