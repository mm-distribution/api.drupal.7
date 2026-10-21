# SelectQueryExtender::uniqueIdentifier()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 571–573 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L571-L573)
- **Class:** [SelectQueryExtender](../SelectQueryExtender.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function uniqueIdentifier()
```

## Documentation

```text
Implements QueryPlaceholderInterface::uniqueIdentifier().
```

## Code

```php
  public function uniqueIdentifier() {
    return $this->uniqueIdentifier;
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
