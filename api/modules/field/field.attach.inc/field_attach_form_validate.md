# field_attach_form_validate()

- **Type:** Function
- **File:** [`modules/field/field.attach.inc`](_file.md), lines 837–861 · [local source](../../../../source/modules/field/field.attach.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc#L837-L861)
- **Module/theme:** field
- **Topics:** [field_attach](../../../topics/field_attach.md)

## Signature

```php
function field_attach_form_validate($entity_type, $entity, $form, &$form_state, $options = array())
```

## Documentation

```text
Perform field validation against form-submitted field values.

There are two levels of validation for fields in forms: widget
validation, and field validation.
- Widget validation steps are specific to a given widget's own form
  structure and UI metaphors. They are executed through FAPI's
  #element_validate property during normal form validation.
- Field validation steps are common to a given field type, independently of
  the specific widget being used in a given form. They are defined in the
  field type's implementation of hook_field_validate().

This function performs field validation in the context of a form
submission. It converts field validation errors into form errors
on the correct form elements. Fieldable entity types should call
this function during their own form validation function.

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
function field_attach_form_validate($entity_type, $entity, $form, &$form_state, $options = array()) {
  // Validate $options since this is a new parameter added after Drupal 7 was
  // released.
  $options = is_array($options) ? $options : array();

  // Extract field values from submitted values.
  _field_invoke_default('extract_form_values', $entity_type, $entity, $form, $form_state);

  // Perform field_level validation.
  try {
    field_attach_validate($entity_type, $entity, $options);
  }
  catch (FieldValidationException $e) {
    // Pass field-level validation errors back to widgets for accurate error
    // flagging.
    foreach ($e->errors as $field_name => $field_errors) {
      foreach ($field_errors as $langcode => $errors) {
        $field_state = field_form_get_state($form['#parents'], $field_name, $langcode, $form_state);
        $field_state['errors'] = $errors;
        field_form_set_state($form['#parents'], $field_name, $langcode, $form_state, $field_state);
      }
    }
    _field_invoke_default('form_errors', $entity_type, $entity, $form, $form_state, $options);
  }
}
```

---
_Drupal 7.103 · [modules/field/field.attach.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
