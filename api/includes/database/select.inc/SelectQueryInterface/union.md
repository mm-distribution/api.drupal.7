# SelectQueryInterface::union()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 448–448 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L448)
- **Class:** [SelectQueryInterface](../SelectQueryInterface.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function union(SelectQueryInterface $query, $type = '');
```

## Documentation

```text
Add another Select query to UNION to this one.

Union queries consist of two or more queries whose
results are effectively concatenated together. Queries
will be UNIONed in the order they are specified, with
this object's query coming first. Duplicate columns will
be discarded. All forms of UNION are supported, using
the second '$type' argument.

Note: All queries UNIONed together must have the same
field structure, in the same order. It is up to the
caller to ensure that they match properly. If they do
not, an SQL syntax error will result.

@param $query
  The query to UNION to this query.
@param $type
  The type of UNION to add to the query. Defaults to plain
  UNION.
@return SelectQueryInterface
  The called object.
```

## Code

```php
  public function union(SelectQueryInterface $query, $type = '');
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
