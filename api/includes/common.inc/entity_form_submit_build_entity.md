# entity_form_submit_build_entity()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 8497–8520 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L8497-L8520)

## Signature

```php
function entity_form_submit_build_entity($entity_type, $entity, $form, &$form_state)
```

## Documentation

```text
Copies submitted values to entity properties for simple entity forms.

During the submission handling of an entity form's "Save", "Preview", and
possibly other buttons, the form state's entity needs to be updated with the
submitted form values. Each entity form implements its own builder function
for doing this, appropriate for the particular entity and form, whereas
modules may specify additional builder functions in $form['#entity_builders']
for copying the form values of added form elements to entity properties.
Many of the main entity builder functions can call this helper function to
re-use its logic of copying $form_state['values'][PROPERTY] values to
$entity->PROPERTY for all entries in $form_state['values'] that are not field
data, and calling field_attach_submit() to copy field data. Apart from that
this helper invokes any additional builder functions that have been specified
in $form['#entity_builders'].

For some entity forms (e.g., forms with complex non-field data and forms that
simultaneously edit multiple entities), this behavior may be inappropriate,
so the builder function for such forms needs to implement the required
functionality instead of calling this function.
```

## Code

```php
function entity_form_submit_build_entity($entity_type, $entity, $form, &$form_state) {
  $info = entity_get_info($entity_type);
  list(, , $bundle) = entity_extract_ids($entity_type, $entity);

  // Copy top-level form values that are not for fields to entity properties,
  // without changing existing entity properties that are not being edited by
  // this form. Copying field values must be done using field_attach_submit().
  $values_excluding_fields = $info['fieldable'] ? array_diff_key($form_state['values'], field_info_instances($entity_type, $bundle)) : $form_state['values'];
  foreach ($values_excluding_fields as $key => $value) {
    $entity->$key = $value;
  }

  // Invoke all specified builders for copying form values to entity properties.
  if (isset($form['#entity_builders'])) {
    foreach ($form['#entity_builders'] as $function) {
      $function($entity_type, $entity, $form, $form_state);
    }
  }

  // Copy field values to the entity.
  if ($info['fieldable']) {
    field_attach_submit($entity_type, $entity, $form, $form_state);
  }
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
