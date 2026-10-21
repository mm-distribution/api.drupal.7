# field_attach_preprocess()

- **Type:** Function
- **File:** [`modules/field/field.attach.inc`](_file.md), lines 1272–1290 · [local source](../../../../source/modules/field/field.attach.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc#L1272-L1290)
- **Module/theme:** field
- **Topics:** [field_attach](../../../topics/field_attach.md)

## Signature

```php
function field_attach_preprocess($entity_type, $entity, $element, &$variables)
```

## Documentation

```text
Populate the template variables with the field values available for rendering.

The $variables array will be populated with all the field instance values
associated with the given entity type, keyed by field name; in case of
translatable fields the language currently chosen for display will be
selected.

@param $entity_type
  The type of $entity; e.g. 'node' or 'user'.
@param $entity
  The entity with fields to render.
@param $element
  The structured array containing the values ready for rendering.
@param $variables
  The variables array is passed by reference and will be populated with field
  values.
```

## Code

```php
function field_attach_preprocess($entity_type, $entity, $element, &$variables) {
  list(, , $bundle) = entity_extract_ids($entity_type, $entity);

  foreach (field_info_instances($entity_type, $bundle) as $instance) {
    $field_name = $instance['field_name'];
    if (isset($element[$field_name]['#language'])) {
      $langcode = $element[$field_name]['#language'];
      $variables[$field_name] = isset($entity->{$field_name}[$langcode]) ? $entity->{$field_name}[$langcode] : NULL;
    }
  }

  // Let other modules make changes to the $variables array.
  $context = array(
    'entity_type' => $entity_type,
    'entity' => $entity,
    'element' => $element,
  );
  drupal_alter('field_attach_preprocess', $variables, $context);
}
```

---
_Drupal 7.103 · [modules/field/field.attach.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
