# InsertQuery::useDefaults()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 591–594 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L591-L594)
- **Class:** [InsertQuery](../InsertQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function useDefaults(array $fields)
```

## Documentation

```text
Specifies fields for which the database defaults should be used.

If you want to force a given field to use the database-defined default,
not NULL or undefined, use this method to instruct the database to use
default values explicitly. In most cases this will not be necessary
unless you are inserting a row that is all default values, as you cannot
specify no values in an INSERT query.

Specifying a field both in fields() and in useDefaults() is an error
and will not execute.

@param $fields
  An array of values for which to use the default values
  specified in the table definition.

@return InsertQuery
  The called object.
```

## Code

```php
  public function useDefaults(array $fields) {
    $this->defaultFields = $fields;
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
