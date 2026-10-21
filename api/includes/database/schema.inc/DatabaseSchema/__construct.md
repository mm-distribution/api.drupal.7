# DatabaseSchema::__construct()

- **Type:** Method
- **File:** [`includes/database/schema.inc`](../_file.md), lines 200–203 · [local source](../../../../../source/includes/database/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc#L200-L203)
- **Class:** [DatabaseSchema](../DatabaseSchema.md)
- **Topics:** [schemaapi](../../../../topics/schemaapi.md)

## Signature

```php
public function __construct($connection)
```

## Documentation

_No docblock in source._

## Code

```php
  public function __construct($connection) {
    $this->uniqueIdentifier = uniqid('', TRUE);
    $this->connection = $connection;
  }
```

---
_Drupal 7.103 · [includes/database/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
