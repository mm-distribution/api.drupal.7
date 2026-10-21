# field_ui_field_delete_form()

- **Type:** Function
- **File:** [`modules/field_ui/field_ui.admin.inc`](_file.md), lines 1743–1768 · [local source](../../../../source/modules/field_ui/field_ui.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc#L1743-L1768)
- **Module/theme:** field_ui
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function field_ui_field_delete_form($form, &$form_state, $instance)
```

## Documentation

```text
Form constructor for removing a field instance from a bundle.

@see field_ui_field_delete_form_submit()
@ingroup forms
```

## Code

```php
function field_ui_field_delete_form($form, &$form_state, $instance) {
  $bundle = $instance['bundle'];
  $entity_type = $instance['entity_type'];
  $field = field_info_field($instance['field_name']);

  $admin_path = _field_ui_bundle_admin_path($entity_type, $bundle);

  $form['entity_type'] = array('#type' => 'value', '#value' => $entity_type);
  $form['bundle'] = array('#type' => 'value', '#value' => $bundle);
  $form['field_name'] = array('#type' => 'value', '#value' => $field['field_name']);

  $output = confirm_form($form,
    t('Are you sure you want to delete the field %field?', array('%field' => $instance['label'])),
    $admin_path . '/fields',
    t('If you have any content left in this field, it will be lost. This action cannot be undone.'),
    t('Delete'), t('Cancel'),
    'confirm'
  );

  if ($field['locked']) {
    unset($output['actions']['submit']);
    $output['description']['#markup'] = t('This field is <strong>locked</strong> and cannot be deleted.');
  }

  return $output;
}
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
