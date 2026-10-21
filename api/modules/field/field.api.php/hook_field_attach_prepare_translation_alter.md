# hook_field_attach_prepare_translation_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 1560–1564 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L1560-L1564)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_attach](../../../topics/field_attach.md)

## Signature

```php
function hook_field_attach_prepare_translation_alter(&$entity, $context)
```

## Documentation

```text
Perform alterations on field_attach_prepare_translation().

This hook is invoked after the field module has performed the operation.

@param $entity
  The entity being prepared for translation.
@param $context
  An associative array containing:
  - entity_type: The type of $entity; e.g. 'node' or 'user'.
  - langcode: The language the entity has to be translated in.
  - source_entity: The entity holding the field values to be translated.
  - source_langcode: The source language from which translate.
```

## Code

```php
function hook_field_attach_prepare_translation_alter(&$entity, $context) {
  if ($context['entity_type'] == 'custom_entity_type') {
    $entity->custom_field = $context['source_entity']->custom_field;
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_attach_prepare_translation_alter()".

- [poll_field_attach_prepare_translation_alter()](../../poll/poll.module/poll_field_attach_prepare_translation_alter.md) — `modules/poll/poll.module`

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
