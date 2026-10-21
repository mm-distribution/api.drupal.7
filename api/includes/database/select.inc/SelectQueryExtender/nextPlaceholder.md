# SelectQueryExtender::nextPlaceholder()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 578–580 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L578-L580)
- **Class:** [SelectQueryExtender](../SelectQueryExtender.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function nextPlaceholder()
```

## Documentation

```text
Implements QueryPlaceholderInterface::nextPlaceholder().
```

## Code

```php
  public function nextPlaceholder() {
    return $this->placeholder++;
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
