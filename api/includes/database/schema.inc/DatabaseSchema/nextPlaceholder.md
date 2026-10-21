# DatabaseSchema::nextPlaceholder()

- **Type:** Method
- **File:** [`includes/database/schema.inc`](../_file.md), lines 222–224 · [local source](../../../../../source/includes/database/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc#L222-L224)
- **Class:** [DatabaseSchema](../DatabaseSchema.md)
- **Topics:** [schemaapi](../../../../topics/schemaapi.md)

## Signature

```php
public function nextPlaceholder()
```

## Documentation

```text
Implements QueryPlaceHolderInterface::nextPlaceholder().
```

## Code

```php
  public function nextPlaceholder() {
    return $this->placeholder++;
  }
```

---
_Drupal 7.103 · [includes/database/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
