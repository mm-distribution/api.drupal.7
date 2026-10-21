# field_update_7002()

- **Type:** Function
- **File:** [`modules/field/field.install`](_file.md), lines 451–461 · [local source](../../../../source/modules/field/field.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.install#L451-L461)
- **Module/theme:** field
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function field_update_7002()
```

## Documentation

```text
Split the all-inclusive field_bundle_settings variable per bundle.
```

## Code

```php
function field_update_7002() {
  $settings = variable_get('field_bundle_settings', array());
  if ($settings) {
    foreach ($settings as $entity_type => $entity_type_settings) {
      foreach ($entity_type_settings as $bundle => $bundle_settings) {
        variable_set('field_bundle_settings_' . $entity_type . '__' . $bundle, $bundle_settings);
      }
    }
    variable_del('field_bundle_settings');
  }
}
```

---
_Drupal 7.103 · [modules/field/field.install](https://github.com/drupal/drupal/blob/7.103/modules/field/field.install) · Licensed GPL-2.0-or-later (see LICENSE)._
