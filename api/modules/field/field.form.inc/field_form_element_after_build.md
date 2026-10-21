# field_form_element_after_build()

- **Type:** Function
- **File:** [`modules/field/field.form.inc`](_file.md), lines 385–395 · [local source](../../../../source/modules/field/field.form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.form.inc#L385-L395)
- **Module/theme:** field

## Signature

```php
function field_form_element_after_build($element, &$form_state)
```

## Documentation

```text
#after_build callback for field elements in a form.

This stores the final location of the field within the form structure so
that field_default_form_errors() can assign validation errors to the right
form element.

@see field_default_form_errors()
```

## Code

```php
function field_form_element_after_build($element, &$form_state) {
  $parents = $element['#field_parents'];
  $field_name = $element['#field_name'];
  $langcode = $element['#language'];

  $field_state = field_form_get_state($parents, $field_name, $langcode, $form_state);
  $field_state['array_parents'] = $element['#array_parents'];
  field_form_set_state($parents, $field_name, $langcode, $form_state, $field_state);

  return $element;
}
```

---
_Drupal 7.103 · [modules/field/field.form.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
