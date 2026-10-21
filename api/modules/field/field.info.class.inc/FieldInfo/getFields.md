# FieldInfo::getFields()

- **Type:** Method
- **File:** [`modules/field/field.info.class.inc`](../_file.md), lines 163–196 · [local source](../../../../../source/modules/field/field.info.class.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.class.inc#L163-L196)
- **Class:** [FieldInfo](../FieldInfo.md)
- **Module/theme:** field

## Signature

```php
public function getFields()
```

## Documentation

```text
Returns all active fields, including deleted ones.

@return
  An array of field definitions, keyed by field ID.
```

## Code

```php
  public function getFields() {
    // Read from the "static" cache.
    if ($this->loadedAllFields) {
      return $this->fieldsById;
    }

    // Read from persistent cache.
    if ($cached = cache_get('field_info:fields', 'cache_field')) {
      $this->fieldsById = $cached->data;
    }
    else {
      // Collect and prepare fields.
      foreach (field_read_fields(array(), array('include_deleted' => TRUE)) as $field) {
        $this->fieldsById[$field['id']] = $this->prepareField($field);
      }

      // Store in persistent cache.
      if (lock_acquire('field_info:fields')) {
        cache_set('field_info:fields', $this->fieldsById, 'cache_field');
        lock_release('field_info:fields');
      }
    }

    // Fill the name/ID map.
    foreach ($this->fieldsById as $field) {
      if (!$field['deleted']) {
        $this->fieldIdsByName[$field['field_name']] = $field['id'];
      }
    }

    $this->loadedAllFields = TRUE;

    return $this->fieldsById;
  }
```

---
_Drupal 7.103 · [modules/field/field.info.class.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.class.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
