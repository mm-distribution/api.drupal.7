# field_attach_prepare_translation()

- **Type:** Function
- **File:** [`modules/field/field.attach.inc`](_file.md), lines 1315–1329 · [local source](../../../../source/modules/field/field.attach.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc#L1315-L1329)
- **Module/theme:** field
- **Topics:** [field_attach](../../../topics/field_attach.md)

## Signature

```php
function field_attach_prepare_translation($entity_type, $entity, $langcode, $source_entity, $source_langcode)
```

## Documentation

```text
Prepares an entity for translation.

This function is used to fill-in the form default values for Field API fields
while performing entity translation. By default it copies all the source
values in the given source language to the new entity and assigns them the
target language.

This is used as part of the 'per entity' translation pattern, which is
implemented only for nodes by translation.module. Other entity types may be
supported through contributed modules.

@param $entity_type
  The type of $entity; e.g. 'node' or 'user'.
@param $entity
  The entity to be prepared for translation.
@param $langcode
  The language the entity has to be translated in.
@param $source_entity
  The source entity holding the field values to be translated.
@param $source_langcode
  The source language from which translate.
```

## Code

```php
function field_attach_prepare_translation($entity_type, $entity, $langcode, $source_entity, $source_langcode) {
  $options = array('language' => $langcode);
  // Copy source field values into the entity to be prepared.
  _field_invoke_default('prepare_translation', $entity_type, $entity, $source_entity, $source_langcode, $options);
  // Let field types handle their own advanced translation pattern if needed.
  _field_invoke('prepare_translation', $entity_type, $entity, $source_entity, $source_langcode, $options);
  // Let other modules alter the entity translation.
  $context = array(
    'entity_type' => $entity_type,
    'langcode' => $langcode,
    'source_entity' => $source_entity,
    'source_langcode' => $source_langcode,
  );
  drupal_alter('field_attach_prepare_translation', $entity, $context);
}
```

---
_Drupal 7.103 · [modules/field/field.attach.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
