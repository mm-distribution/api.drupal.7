# DatabaseSchema::uniqueIdentifier()

- **Type:** Method
- **File:** [`includes/database/schema.inc`](../_file.md), lines 215–217 · [local source](../../../../../source/includes/database/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc#L215-L217)
- **Class:** [DatabaseSchema](../DatabaseSchema.md)
- **Topics:** [schemaapi](../../../../topics/schemaapi.md)

## Signature

```php
public function uniqueIdentifier()
```

## Documentation

```text
Implements QueryPlaceHolderInterface::uniqueIdentifier().
```

## Code

```php
  public function uniqueIdentifier() {
    return $this->uniqueIdentifier;
  }
```

---
_Drupal 7.103 · [includes/database/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
