# field_ui_field_delete_form_submit()

- **Type:** Function
- **File:** [`modules/field_ui/field_ui.admin.inc`](_file.md), lines 1776–1805 · [local source](../../../../source/modules/field_ui/field_ui.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc#L1776-L1805)
- **Module/theme:** field_ui

## Signature

```php
function field_ui_field_delete_form_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for field_ui_field_delete_form().

Removes a field instance from a bundle. If the field has no more instances,
it will be marked as deleted too.
```

## Code

```php
function field_ui_field_delete_form_submit($form, &$form_state) {
  $form_values = $form_state['values'];
  $field_name = $form_values['field_name'];
  $bundle = $form_values['bundle'];
  $entity_type = $form_values['entity_type'];

  $field = field_info_field($field_name);
  $instance = field_info_instance($entity_type, $field_name, $bundle);
  $bundles = field_info_bundles();
  $bundle_label = $bundles[$entity_type][$bundle]['label'];

  if (!empty($bundle) && $field && !$field['locked'] && $form_values['confirm']) {
    field_delete_instance($instance);
    drupal_set_message(t('The field %field has been deleted from the %type content type.', array('%field' => $instance['label'], '%type' => $bundle_label)));
  }
  else {
    drupal_set_message(t('There was a problem removing the %field from the %type content type.', array('%field' => $instance['label'], '%type' => $bundle_label)), 'error');
  }

  $admin_path = _field_ui_bundle_admin_path($entity_type, $bundle);
  $form_state['redirect'] = field_ui_get_destinations(array($admin_path . '/fields'));

  // Fields are purged on cron. However field module prevents disabling modules
  // when field types they provided are used in a field until it is fully
  // purged. In the case that a field has minimal or no content, a single call
  // to field_purge_batch() will remove it from the system. Call this with a
  // low batch limit to avoid administrators having to wait for cron runs when
  // removing instances that meet this criteria.
  field_purge_batch(10);
}
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
