# field_attach_validate()

- **Type:** Function
- **File:** [`modules/field/field.attach.inc`](_file.md), lines 781–803 · [local source](../../../../source/modules/field/field.attach.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc#L781-L803)
- **Module/theme:** field
- **Topics:** [field_attach](../../../topics/field_attach.md)

## Signature

```php
function field_attach_validate($entity_type, $entity, $options = array())
```

## Documentation

```text
Perform field validation against the field data in an entity.

This function does not perform field widget validation on form
submissions. It is intended to be called during API save
operations. Use field_attach_form_validate() to validate form
submissions.

@param $entity_type
  The type of $entity; e.g. 'node' or 'user'.
@param $entity
  The entity with fields to validate.
@throws FieldValidationException
  If validation errors are found, a FieldValidationException is thrown. The
  'errors' property contains the array of errors, keyed by field name,
  language and delta.
@param array $options
  An associative array of additional options. See _field_invoke() for
  details.
```

## Code

```php
function field_attach_validate($entity_type, $entity, $options = array()) {
  // Validate $options since this is a new parameter added after Drupal 7 was
  // released.
  $options = is_array($options) ? $options : array();

  $errors = array();
  // Check generic, field-type-agnostic errors first.
  $null = NULL;
  _field_invoke_default('validate', $entity_type, $entity, $errors, $null, $options);
  // Check field-type specific errors.
  _field_invoke('validate', $entity_type, $entity, $errors, $null, $options);

  // Let other modules validate the entity.
  // Avoid module_invoke_all() to let $errors be taken by reference.
  foreach (module_implements('field_attach_validate') as $module) {
    $function = $module . '_field_attach_validate';
    $function($entity_type, $entity, $errors);
  }

  if ($errors) {
    throw new FieldValidationException($errors);
  }
}
```

---
_Drupal 7.103 · [modules/field/field.attach.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
