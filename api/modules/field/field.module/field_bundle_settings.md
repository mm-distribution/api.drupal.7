# field_bundle_settings()

- **Type:** Function
- **File:** [`modules/field/field.module`](_file.md), lines 587–605 · [local source](../../../../source/modules/field/field.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module#L587-L605)
- **Module/theme:** field
- **Topics:** [field](../../../topics/field.md)

## Signature

```php
function field_bundle_settings($entity_type, $bundle, $settings = NULL)
```

## Documentation

```text
Gets or sets administratively defined bundle settings.

@param string $entity_type
  The type of $entity; e.g., 'node' or 'user'.
@param string $bundle
  The bundle name.
@param array|null $settings
  (optional) The settings to store, an associative array with the following
  elements:
  - view_modes: An associative array keyed by view mode, with the following
    key/value pairs:
    - custom_settings: Boolean specifying whether the view mode uses a
      dedicated set of display options (TRUE), or the 'default' options
      (FALSE). Defaults to FALSE.
  - extra_fields: An associative array containing the form and display
    settings for extra fields (also known as pseudo-fields):
    - form: An associative array whose keys are the names of extra fields,
      and whose values are associative arrays with the following elements:
      - weight: The weight of the extra field, determining its position on an
        entity form.
    - display: An associative array whose keys are the names of extra fields,
      and whose values are associative arrays keyed by the name of view
      modes. This array must include an item for the 'default' view mode.
      Each view mode sub-array contains the following elements:
      - weight: The weight of the extra field, determining its position when
        an entity is viewed.
      - visible: TRUE if the extra field is visible, FALSE otherwise.

@return array|null
  If no $settings are passed, the current settings are returned.
```

## Code

```php
function field_bundle_settings($entity_type, $bundle, $settings = NULL) {
  if (isset($settings)) {
    variable_set('field_bundle_settings_' . $entity_type . '__' . $bundle, $settings);
    field_info_cache_clear();
  }
  else {
    $settings = variable_get('field_bundle_settings_' . $entity_type . '__' . $bundle, array());
    $settings += array(
      'view_modes' => array(),
      'extra_fields' => array(),
    );
    $settings['extra_fields'] += array(
      'form' => array(),
      'display' => array(),
    );

    return $settings;
  }
}
```

---
_Drupal 7.103 · [modules/field/field.module](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module) · Licensed GPL-2.0-or-later (see LICENSE)._
