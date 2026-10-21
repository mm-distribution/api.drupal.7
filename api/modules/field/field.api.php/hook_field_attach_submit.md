# hook_field_attach_submit()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 1398–1405 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L1398-L1405)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_attach](../../../topics/field_attach.md)

## Signature

```php
function hook_field_attach_submit($entity_type, $entity, $form, &$form_state)
```

## Documentation

```text
Act on field_attach_submit().

This hook is invoked after the field module has performed the operation.

@param $entity_type
  The type of $entity; for example, 'node' or 'user'.
@param $entity
  The entity for which an edit form is being submitted. The incoming form
  values have been extracted as field values of the $entity object.
@param $form
  The form structure where field elements are attached to. This might be a
  full form structure, or a sub-part of a larger form. The $form['#parents']
  property can be used to identify the corresponding part of
  $form_state['values'].
@param $form_state
  An associative array containing the current state of the form.
```

## Code

```php
function hook_field_attach_submit($entity_type, $entity, $form, &$form_state) {
  // Sample case of an 'Empty the field' checkbox added on the form, allowing
  // a given field to be emptied.
  $values = drupal_array_get_nested_value($form_state['values'], $form['#parents']);
  if (!empty($values['empty_field_foo'])) {
    unset($entity->field_foo);
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_attach_submit()".

_None found._

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
