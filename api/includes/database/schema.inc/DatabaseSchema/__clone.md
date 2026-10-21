# DatabaseSchema::__clone()

- **Type:** Method
- **File:** [`includes/database/schema.inc`](../_file.md), lines 208–210 · [local source](../../../../../source/includes/database/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc#L208-L210)
- **Class:** [DatabaseSchema](../DatabaseSchema.md)
- **Topics:** [schemaapi](../../../../topics/schemaapi.md)

## Signature

```php
public function __clone()
```

## Documentation

```text
Implements the magic __clone function.
```

## Code

```php
  public function __clone() {
    $this->uniqueIdentifier = uniqid('', TRUE);
  }
```

---
_Drupal 7.103 · [includes/database/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
