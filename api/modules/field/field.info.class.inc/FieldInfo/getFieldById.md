# FieldInfo::getFieldById()

- **Type:** Method
- **File:** [`modules/field/field.info.class.inc`](../_file.md), lines 306–334 · [local source](../../../../../source/modules/field/field.info.class.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.class.inc#L306-L334)
- **Class:** [FieldInfo](../FieldInfo.md)
- **Module/theme:** field

## Signature

```php
public function getFieldById($field_id)
```

## Documentation

```text
Returns a field definition from a field ID.

This method only retrieves active fields, deleted or not.

@param $field_id
  The field ID.

@return
  The field definition, or NULL if no field was found.
```

## Code

```php
  public function getFieldById($field_id) {
    // Read from the "static" cache.
    if (isset($this->fieldsById[$field_id])) {
      return $this->fieldsById[$field_id];
    }
    if (isset($this->unknownFields[$field_id])) {
      return;
    }

    // No persistent cache, fields are only persistently cached as part of a
    // bundle.

    // Cache miss: read from definition.
    if ($fields = field_read_fields(array('id' => $field_id), array('include_deleted' => TRUE))) {
      $field = current($fields);
      $field = $this->prepareField($field);

      // Store in the static cache.
      $this->fieldsById[$field['id']] = $field;
      if (!$field['deleted']) {
        $this->fieldIdsByName[$field['field_name']] = $field['id'];
      }

      return $field;
    }
    else {
      $this->unknownFields[$field_id] = TRUE;
    }
  }
```

---
_Drupal 7.103 · [modules/field/field.info.class.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.class.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
