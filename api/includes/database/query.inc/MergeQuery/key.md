# MergeQuery::key()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 1540–1549 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L1540-L1549)
- **Class:** [MergeQuery](../MergeQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function key(array $fields, array $values = array())
```

## Documentation

```text
Sets the key field(s) to be used as conditions for this query.

This method should only be called once. It may be called either
with a single associative array or two indexed arrays. If called
with an associative array, the keys are taken to be the fields
and the values are taken to be the corresponding values to set.
If called with two arrays, the first array is taken as the fields
and the second array is taken as the corresponding values.

The fields are copied to the condition of the query and the INSERT part.
If no other method is called, the UPDATE will become a no-op.

@param $fields
  An array of fields to set, or an associative array of fields and values.
@param $values
  An array of values to set into the database. The values must be
  specified in the same order as the $fields array.

@return MergeQuery
  The called object.
```

## Code

```php
  public function key(array $fields, array $values = array()) {
    if ($values) {
      $fields = array_combine($fields, $values);
    }
    foreach ($fields as $key => $value) {
      $this->insertFields[$key] = $value;
      $this->condition($key, $value);
    }
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
