# field_attach_submit()

- **Type:** Function
- **File:** [`modules/field/field.attach.inc`](_file.md), lines 884–900 · [local source](../../../../source/modules/field/field.attach.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc#L884-L900)
- **Module/theme:** field
- **Topics:** [field_attach](../../../topics/field_attach.md)

## Signature

```php
function field_attach_submit($entity_type, $entity, $form, &$form_state, $options = array())
```

## Documentation

```text
Perform necessary operations on field data submitted by a form.

Currently, this accounts for drag-and-drop reordering of
field values, and filtering of empty values.

@param $entity_type
  The type of $entity; e.g. 'node' or 'user'.
@param $entity
  The entity being submitted. The 'bundle', 'id' and (if applicable)
  'revision' keys should be present. The actual field values will be read
  from $form_state['values'].
@param $form
  The form structure where field elements are attached to. This might be a
  full form structure, or a sub-element of a larger form.
@param $form_state
  An associative array containing the current state of the form.
@param array $options
  An associative array of additional options. See _field_invoke() for
  details.
```

## Code

```php
function field_attach_submit($entity_type, $entity, $form, &$form_state, $options = array()) {
  // Validate $options since this is a new parameter added after Drupal 7 was
  // released.
  $options = is_array($options) ? $options : array();

  // Extract field values from submitted values.
  _field_invoke_default('extract_form_values', $entity_type, $entity, $form, $form_state, $options);

  _field_invoke_default('submit', $entity_type, $entity, $form, $form_state, $options);

  // Let other modules act on submitting the entity.
  // Avoid module_invoke_all() to let $form_state be taken by reference.
  foreach (module_implements('field_attach_submit') as $module) {
    $function = $module . '_field_attach_submit';
    $function($entity_type, $entity, $form, $form_state);
  }
}
```

---
_Drupal 7.103 · [modules/field/field.attach.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
