# SelectQueryExtender::__clone()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 823–829 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L823-L829)
- **Class:** [SelectQueryExtender](../SelectQueryExtender.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function __clone()
```

## Documentation

_No docblock in source._

## Code

```php
  public function __clone() {
    $this->uniqueIdentifier = uniqid('', TRUE);

    // We need to deep-clone the query we're wrapping, which in turn may
    // deep-clone other objects.  Exciting!
    $this->query = clone($this->query);
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
