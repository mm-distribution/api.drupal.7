# hook_field_attach_form()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 1317–1324 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L1317-L1324)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_attach](../../../topics/field_attach.md)

## Signature

```php
function hook_field_attach_form($entity_type, $entity, &$form, &$form_state, $langcode)
```

## Documentation

```text
Act on field_attach_form().

This hook is invoked after the field module has performed the operation.
Implementing modules should alter the $form or $form_state parameters.

@param $entity_type
  The type of $entity; for example, 'node' or 'user'.
@param $entity
  The entity for which an edit form is being built.
@param $form
  The form structure where field elements are attached to. This might be a
  full form structure, or a sub-element of a larger form. The
  $form['#parents'] property can be used to identify the corresponding part
  of $form_state['values']. Hook implementations that need to act on the
  top-level properties of the global form (like #submit, #validate...) can
  add a #process callback to the array received in the $form parameter, and
  act on the $complete_form parameter in the process callback.
@param $form_state
  An associative array containing the current state of the form.
@param $langcode
  The language the field values are going to be entered in. If no language
  is provided the default site language will be used.
```

## Code

```php
function hook_field_attach_form($entity_type, $entity, &$form, &$form_state, $langcode) {
  // Add a checkbox allowing a given field to be emptied.
  // See hook_field_attach_submit() for the corresponding processing code.
  $form['empty_field_foo'] = array(
    '#type' => 'checkbox',
    '#title' => t("Empty the 'field_foo' field"),
  );
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_attach_form()".

_None found._

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
