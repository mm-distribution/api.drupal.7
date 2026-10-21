# FieldInfo::prepareField()

- **Type:** Method
- **File:** [`modules/field/field.info.class.inc`](../_file.md), lines 493–513 · [local source](../../../../../source/modules/field/field.info.class.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.class.inc#L493-L513)
- **Class:** [FieldInfo](../FieldInfo.md)
- **Module/theme:** field

## Signature

```php
public function prepareField($field)
```

## Documentation

```text
Prepares a field definition for the current run-time context.

@param $field
  The raw field structure as read from the database.

@return
  The field definition completed for the current runtime context.
```

## Code

```php
  public function prepareField($field) {
    // Make sure all expected field settings are present.
    $field['settings'] += field_info_field_settings($field['type']);
    $field['storage']['settings'] += field_info_storage_settings($field['storage']['type']);

    // Add storage details.
    $details = (array) module_invoke($field['storage']['module'], 'field_storage_details', $field);
    drupal_alter('field_storage_details', $details, $field);
    $field['storage']['details'] = $details;

    // Populate the list of bundles using the field.
    $field['bundles'] = array();
    if (!$field['deleted']) {
      $map = $this->getFieldMap();
      if (isset($map[$field['field_name']])) {
        $field['bundles'] = $map[$field['field_name']]['bundles'];
      }
    }

    return $field;
  }
```

---
_Drupal 7.103 · [modules/field/field.info.class.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.class.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
