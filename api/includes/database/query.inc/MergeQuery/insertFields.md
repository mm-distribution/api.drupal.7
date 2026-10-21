# MergeQuery::insertFields()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 1453–1459 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L1453-L1459)
- **Class:** [MergeQuery](../MergeQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function insertFields(array $fields, array $values = array())
```

## Documentation

```text
Adds a set of field->value pairs to be inserted.

@param $fields
  An array of fields on which to insert. This array may be indexed or
  associative. If indexed, the array is taken to be the list of fields.
  If associative, the keys of the array are taken to be the fields and
  the values are taken to be corresponding values to insert. If a
  $values argument is provided, $fields must be indexed.
@param $values
  An array of fields to insert into the database. The values must be
  specified in the same order as the $fields array.

@return MergeQuery
  The called object.
```

## Code

```php
  public function insertFields(array $fields, array $values = array()) {
    if ($values) {
      $fields = array_combine($fields, $values);
    }
    $this->insertFields = $fields;
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
