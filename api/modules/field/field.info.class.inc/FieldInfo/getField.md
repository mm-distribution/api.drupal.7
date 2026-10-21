# FieldInfo::getField()

- **Type:** Method
- **File:** [`modules/field/field.info.class.inc`](../_file.md), lines 268–293 · [local source](../../../../../source/modules/field/field.info.class.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.class.inc#L268-L293)
- **Class:** [FieldInfo](../FieldInfo.md)
- **Module/theme:** field

## Signature

```php
public function getField($field_name)
```

## Documentation

```text
Returns a field definition from a field name.

This method only retrieves active, non-deleted fields.

@param $field_name
  The field name.

@return
  The field definition, or NULL if no field was found.
```

## Code

```php
  public function getField($field_name) {
    // Read from the "static" cache.
    if (isset($this->fieldIdsByName[$field_name])) {
      $field_id = $this->fieldIdsByName[$field_name];
      return $this->fieldsById[$field_id];
    }
    if (isset($this->unknownFields[$field_name])) {
      return;
    }

    // Do not check the (large) persistent cache, but read the definition.

    // Cache miss: read from definition.
    if ($field = field_read_field($field_name)) {
      $field = $this->prepareField($field);

      // Save in the "static" cache.
      $this->fieldsById[$field['id']] = $field;
      $this->fieldIdsByName[$field['field_name']] = $field['id'];

      return $field;
    }
    else {
      $this->unknownFields[$field_name] = TRUE;
    }
  }
```

---
_Drupal 7.103 · [modules/field/field.info.class.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.class.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
