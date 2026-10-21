# MergeQuery::updateFields()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 1403–1407 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L1403-L1407)
- **Class:** [MergeQuery](../MergeQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function updateFields(array $fields)
```

## Documentation

```text
Adds a set of field->value pairs to be updated.

@param $fields
  An associative array of fields to write into the database. The array keys
  are the field names and the values are the values to which to set them.

@return MergeQuery
  The called object.
```

## Code

```php
  public function updateFields(array $fields) {
    $this->updateFields = $fields;
    $this->needsUpdate = TRUE;
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
