# MergeQuery::fields()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 1506–1516 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L1506-L1516)
- **Class:** [MergeQuery](../MergeQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function fields(array $fields, array $values = array())
```

## Documentation

```text
Sets common field-value pairs in the INSERT and UPDATE query parts.

This method should only be called once. It may be called either
with a single associative array or two indexed arrays. If called
with an associative array, the keys are taken to be the fields
and the values are taken to be the corresponding values to set.
If called with two arrays, the first array is taken as the fields
and the second array is taken as the corresponding values.

@param $fields
  An array of fields to insert, or an associative array of fields and
  values. The keys of the array are taken to be the fields and the values
  are taken to be corresponding values to insert.
@param $values
  An array of values to set into the database. The values must be
  specified in the same order as the $fields array.

@return MergeQuery
  The called object.
```

## Code

```php
  public function fields(array $fields, array $values = array()) {
    if ($values) {
      $fields = array_combine($fields, $values);
    }
    foreach ($fields as $key => $value) {
      $this->insertFields[$key] = $value;
      $this->updateFields[$key] = $value;
    }
    $this->needsUpdate = TRUE;
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
