# FieldInfo::prepareExtraFields()

- **Type:** Method
- **File:** [`modules/field/field.info.class.inc`](../_file.md), lines 649–685 · [local source](../../../../../source/modules/field/field.info.class.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.class.inc#L649-L685)
- **Class:** [FieldInfo](../FieldInfo.md)
- **Module/theme:** field

## Signature

```php
public function prepareExtraFields($extra_fields, $entity_type, $bundle)
```

## Documentation

```text
Prepares 'extra fields' for the current run-time context.

@param $extra_fields
  The array of extra fields, as collected in hook_field_extra_fields().
@param $entity_type
  The entity type.
@param $bundle
  The bundle name.

@return
  The list of extra fields completed for the current runtime context.
```

## Code

```php
  public function prepareExtraFields($extra_fields, $entity_type, $bundle) {
    $entity_type_info = entity_get_info($entity_type);
    $bundle_settings = field_bundle_settings($entity_type, $bundle);
    $extra_fields += array('form' => array(), 'display' => array());

    $result = array();
    // Extra fields in forms.
    foreach ($extra_fields['form'] as $name => $field_data) {
      $settings = isset($bundle_settings['extra_fields']['form'][$name]) ? $bundle_settings['extra_fields']['form'][$name] : array();
      if (isset($settings['weight'])) {
        $field_data['weight'] = $settings['weight'];
      }
      $result['form'][$name] = $field_data;
    }

    // Extra fields in displayed entities.
    $data = $extra_fields['display'];
    foreach ($extra_fields['display'] as $name => $field_data) {
      $settings = isset($bundle_settings['extra_fields']['display'][$name]) ? $bundle_settings['extra_fields']['display'][$name] : array();
      $view_modes = array_merge(array('default'), array_keys($entity_type_info['view modes']));
      foreach ($view_modes as $view_mode) {
        if (isset($settings[$view_mode])) {
          $field_data['display'][$view_mode] = $settings[$view_mode];
        }
        else {
          $field_data['display'][$view_mode] = array(
            'weight' => $field_data['weight'],
            'visible' => TRUE,
          );
        }
      }
      unset($field_data['weight']);
      $result['display'][$name] = $field_data;
    }

    return $result;
  }
```

---
_Drupal 7.103 · [modules/field/field.info.class.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.class.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
