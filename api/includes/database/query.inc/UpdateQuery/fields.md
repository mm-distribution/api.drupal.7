# UpdateQuery::fields()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 1120–1123 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L1120-L1123)
- **Class:** [UpdateQuery](../UpdateQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function fields(array $fields)
```

## Documentation

```text
Adds a set of field->value pairs to be updated.

@param $fields
  An associative array of fields to write into the database. The array keys
  are the field names and the values are the values to which to set them.

@return UpdateQuery
  The called object.
```

## Code

```php
  public function fields(array $fields) {
    $this->fields = $fields;
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
