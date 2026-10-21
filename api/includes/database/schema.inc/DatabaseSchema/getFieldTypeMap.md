# DatabaseSchema::getFieldTypeMap()

- **Type:** Method
- **File:** [`includes/database/schema.inc`](../_file.md), lines 450–450 · [local source](../../../../../source/includes/database/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc#L450)
- **Class:** [DatabaseSchema](../DatabaseSchema.md)
- **Topics:** [schemaapi](../../../../topics/schemaapi.md)

## Signature

```php
abstract public function getFieldTypeMap();
```

## Documentation

```text
Returns a mapping of Drupal schema field names to DB-native field types.

Because different field types do not map 1:1 between databases, Drupal has
its own normalized field type names. This function returns a driver-specific
mapping table from Drupal names to the native names for each database.

@return array
  An array of Schema API field types to driver-specific field types.
```

## Code

```php
  abstract public function getFieldTypeMap();
```

---
_Drupal 7.103 · [includes/database/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
