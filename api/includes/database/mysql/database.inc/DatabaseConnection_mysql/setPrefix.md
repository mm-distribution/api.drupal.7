# DatabaseConnection_mysql::setPrefix()

- **Type:** Method
- **File:** [`includes/database/mysql/database.inc`](../_file.md), lines 392–412 · [local source](../../../../../../source/includes/database/mysql/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/database.inc#L392-L412)
- **Class:** [DatabaseConnection_mysql](../DatabaseConnection_mysql.md)
- **Topics:** [database](../../../../../topics/database.md)

## Signature

```php
protected function setPrefix($prefix)
```

## Documentation

```text
{@inheritdoc}}
```

## Code

```php
  protected function setPrefix($prefix) {
    parent::setPrefix($prefix);
    // Successive versions of MySQL have become increasingly strict about the
    // use of reserved keywords as table names. Drupal 7 uses at least one such
    // table (system). Therefore we surround all table names with quotes.
    $quote_char = variable_get('mysql_identifier_quote_character', MYSQL_IDENTIFIER_QUOTE_CHARACTER_DEFAULT);
    foreach ($this->prefixSearch as $i => $prefixSearch) {
      if (substr($prefixSearch, 0, 1) === '{') {
        // If the prefix already contains one or more quotes remove them.
        // This can happen when - for example - DrupalUnitTestCase sets up a
        // "temporary prefixed database". Also if there's a dot in the prefix,
        // wrap it in quotes to cater for schema names in prefixes.
        $search = array($quote_char, '.');
        $replace = array('', $quote_char . '.' . $quote_char);
        $this->prefixReplace[$i] = $quote_char . str_replace($search, $replace, $this->prefixReplace[$i]);
      }
      if (substr($prefixSearch, -1) === '}') {
        $this->prefixReplace[$i] .= $quote_char;
      }
    }
  }
```

---
_Drupal 7.103 · [includes/database/mysql/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
