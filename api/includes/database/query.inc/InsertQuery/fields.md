# InsertQuery::fields()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 526–541 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L526-L541)
- **Class:** [InsertQuery](../InsertQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function fields(array $fields, array $values = array())
```

## Documentation

```text
Adds a set of field->value pairs to be inserted.

This method may only be called once. Calling it a second time will be
ignored. To queue up multiple sets of values to be inserted at once,
use the values() method.

@param $fields
  An array of fields on which to insert. This array may be indexed or
  associative. If indexed, the array is taken to be the list of fields.
  If associative, the keys of the array are taken to be the fields and
  the values are taken to be corresponding values to insert. If a
  $values argument is provided, $fields must be indexed.
@param $values
  An array of fields to insert into the database. The values must be
  specified in the same order as the $fields array.

@return InsertQuery
  The called object.
```

## Code

```php
  public function fields(array $fields, array $values = array()) {
    if (empty($this->insertFields)) {
      if (empty($values)) {
        if (!is_numeric(key($fields))) {
          $values = array_values($fields);
          $fields = array_keys($fields);
        }
      }
      $this->insertFields = $fields;
      if (!empty($values)) {
        $this->insertValues[] = $values;
      }
    }

    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
