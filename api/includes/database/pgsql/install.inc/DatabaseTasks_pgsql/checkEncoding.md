# DatabaseTasks_pgsql::checkEncoding()

- **Type:** Method
- **File:** [`includes/database/pgsql/install.inc`](../_file.md), lines 44–63 · [local source](../../../../../../source/includes/database/pgsql/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/install.inc#L44-L63)
- **Class:** [DatabaseTasks_pgsql](../DatabaseTasks_pgsql.md)

## Signature

```php
protected function checkEncoding()
```

## Documentation

```text
Check encoding is UTF8.
```

## Code

```php
  protected function checkEncoding() {
    try {
      if (db_query('SHOW server_encoding')->fetchField() == 'UTF8') {
        $this->pass(st('Database is encoded in UTF-8'));
      }
      else {
        $replacements = array(
          '%encoding' => 'UTF8',
          '%driver' => $this->name(),
          '!link' => '<a href="INSTALL.pgsql.txt">INSTALL.pgsql.txt</a>'
        );
        $text  = 'The %driver database must use %encoding encoding to work with Drupal.';
        $text .= 'Recreate the database with %encoding encoding. See !link for more details.';
        $this->fail(st($text, $replacements));
      }
    }
    catch (Exception $e) {
      $this->fail(st('Drupal could not determine the encoding of the database was set to UTF-8'));
    }
  }
```

---
_Drupal 7.103 · [includes/database/pgsql/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
