# DatabaseConnection_mysql::quoteIdentifier()

- **Type:** Method
- **File:** [`includes/database/mysql/database.inc`](../_file.md), lines 446–459 · [local source](../../../../../../source/includes/database/mysql/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/database.inc#L446-L459)
- **Class:** [DatabaseConnection_mysql](../DatabaseConnection_mysql.md)
- **Topics:** [database](../../../../../topics/database.md)

## Signature

```php
private function quoteIdentifier($identifier)
```

## Documentation

```text
Quotes an identifier if it matches a MySQL reserved keyword.

@param string $identifier
  The field to check.

@return string
  The identifier, quoted if it matches a MySQL reserved keyword.
```

## Code

```php
  private function quoteIdentifier($identifier) {
    // Quote identifiers so that MySQL reserved words like 'function' can be
    // used as column names. Sometimes the 'table.column_name' format is passed
    // in. For example, menu_load_links() adds a condition on "ml.menu_name".
    if (strpos($identifier, '.') !== FALSE) {
      list($table, $identifier) = explode('.', $identifier, 2);
    }
    if (in_array(strtolower($identifier), $this->reservedKeyWords, TRUE)) {
      // Quote the string for MySQL reserved keywords.
      $quote_char = variable_get('mysql_identifier_quote_character', MYSQL_IDENTIFIER_QUOTE_CHARACTER_DEFAULT);
      $identifier = $quote_char . $identifier . $quote_char;
    }
    return isset($table) ? $table . '.' . $identifier : $identifier;
  }
```

---
_Drupal 7.103 · [includes/database/mysql/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
