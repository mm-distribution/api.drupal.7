# DatabaseSchema::fieldNames()

- **Type:** Method
- **File:** [`includes/database/schema.inc`](../_file.md), lines 751–762 · [local source](../../../../../source/includes/database/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc#L751-L762)
- **Class:** [DatabaseSchema](../DatabaseSchema.md)
- **Topics:** [schemaapi](../../../../topics/schemaapi.md)

## Signature

```php
public function fieldNames($fields)
```

## Documentation

```text
Return an array of field names from an array of key/index column specifiers.

This is usually an identity function but if a key/index uses a column prefix
specification, this function extracts just the name.

@param $fields
  An array of key/index column specifiers.

@return
  An array of field names.
```

## Code

```php
  public function fieldNames($fields) {
    $return = array();
    foreach ($fields as $field) {
      if (is_array($field)) {
        $return[] = $field[0];
      }
      else {
        $return[] = $field;
      }
    }
    return $return;
  }
```

---
_Drupal 7.103 · [includes/database/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
