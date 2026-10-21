# DatabaseSchemaObjectDoesNotExistException

- **Type:** Class
- **File:** [`includes/database/schema.inc`](_file.md), lines 796–796 · [local source](../../../../source/includes/database/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc#L796)
- **Topics:** [schemaapi](../../../topics/schemaapi.md)

## Signature

```php
class DatabaseSchemaObjectDoesNotExistException extends Exception {}
```

## Documentation

```text
Exception thrown if an object being modified doesn't exist yet.

For example, this exception should be thrown whenever there is an attempt to
modify a database table, field, or index that does not currently exist in
the database schema.
```

---
_Drupal 7.103 · [includes/database/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
