# SelectQuery::union()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 1451–1471 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L1451-L1471)
- **Class:** [SelectQuery](../SelectQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function union(SelectQueryInterface $query, $type = '')
```

## Documentation

_No docblock in source._

## Code

```php
  public function union(SelectQueryInterface $query, $type = '') {
    // Handle UNION aliasing.
    switch ($type) {
      // Fold UNION DISTINCT to UNION for better cross database support.
      case 'DISTINCT':
      case '':
        $type = 'UNION';
        break;

      case 'ALL':
        $type = 'UNION ALL';
      default:
    }

    $this->union[] = array(
      'type' => $type,
      'query' => $query,
    );

    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
