# DatabaseConnection::setPrefix()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 451–481 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L451-L481)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
protected function setPrefix($prefix)
```

## Documentation

```text
Set the list of prefixes used by this database connection.

@param $prefix
  The prefixes, in any of the multiple forms documented in
  default.settings.php.
```

## Code

```php
  protected function setPrefix($prefix) {
    if (is_array($prefix)) {
      $this->prefixes = $prefix + array('default' => '');
    }
    else {
      $this->prefixes = array('default' => $prefix);
    }

    // Set up variables for use in prefixTables(). Replace table-specific
    // prefixes first.
    $this->prefixSearch = array();
    $this->prefixReplace = array();
    foreach ($this->prefixes as $key => $val) {
      if ($key != 'default') {
        $this->prefixSearch[] = '{' . $key . '}';
        $this->prefixReplace[] = $val . $key;
      }
    }
    // Then replace remaining tables with the default prefix.
    $this->prefixSearch[] = '{';
    $this->prefixReplace[] = $this->prefixes['default'];
    $this->prefixSearch[] = '}';
    $this->prefixReplace[] = '';

    // Set up a map of prefixed => un-prefixed tables.
    foreach ($this->prefixes as $table_name => $prefix) {
      if ($table_name !== 'default') {
        $this->unprefixedTablesMap[$prefix . $table_name] = $table_name;
      }
    }
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
