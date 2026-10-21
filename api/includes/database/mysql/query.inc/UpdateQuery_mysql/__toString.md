# UpdateQuery_mysql::__toString()

- **Type:** Method
- **File:** [`includes/database/mysql/query.inc`](../_file.md), lines 105–123 · [local source](../../../../../../source/includes/database/mysql/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/query.inc#L105-L123)
- **Class:** [UpdateQuery_mysql](../UpdateQuery_mysql.md)
- **Topics:** [database](../../../../../topics/database.md)

## Signature

```php
public function __toString()
```

## Documentation

_No docblock in source._

## Code

```php
  public function __toString() {
    if (method_exists($this->connection, 'escapeField')) {
      if (!is_array($this->fields)) {
        if (version_compare(PHP_VERSION, '7.4', '>=')) {
          throw new UnexpectedValueException();
        }
        else {
          drupal_trigger_fatal_error('Unexpected Value');
        }
      }
      $escapedFields = array();
      foreach ($this->fields as $field => $data) {
        $field = $this->connection->escapeField($field);
        $escapedFields[$field] = $data;
      }
      $this->fields = $escapedFields;
    }
    return parent::__toString();
  }
```

---
_Drupal 7.103 · [includes/database/mysql/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
