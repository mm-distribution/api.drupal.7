# DatabaseSchemaObjectExistsException

- **Type:** Class
- **File:** [`includes/database/schema.inc`](_file.md), lines 787–787 · [local source](../../../../source/includes/database/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc#L787)
- **Topics:** [schemaapi](../../../topics/schemaapi.md)

## Signature

```php
class DatabaseSchemaObjectExistsException extends Exception {}
```

## Documentation

```text
Exception thrown if an object being created already exists.

For example, this exception should be thrown whenever there is an attempt to
create a new database table, field, or index that already exists in the
database schema.
```

---
_Drupal 7.103 · [includes/database/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
