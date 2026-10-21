# DatabaseTasks_pgsql::initializeDatabase()

- **Type:** Method
- **File:** [`includes/database/pgsql/install.inc`](../_file.md), lines 139–195 · [local source](../../../../../../source/includes/database/pgsql/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/install.inc#L139-L195)
- **Class:** [DatabaseTasks_pgsql](../DatabaseTasks_pgsql.md)

## Signature

```php
function initializeDatabase()
```

## Documentation

```text
Make PostgreSQL Drupal friendly.
```

## Code

```php
  function initializeDatabase() {
    // We create some functions using global names instead of prefixing them
    // like we do with table names. This is so that we don't double up if more
    // than one instance of Drupal is running on a single database. We therefore
    // avoid trying to create them again in that case.

    try {
      // Create functions.
      db_query('CREATE OR REPLACE FUNCTION "greatest"(numeric, numeric) RETURNS numeric AS
        \'SELECT CASE WHEN (($1 > $2) OR ($2 IS NULL)) THEN $1 ELSE $2 END;\'
        LANGUAGE \'sql\''
      );
      db_query('CREATE OR REPLACE FUNCTION "greatest"(numeric, numeric, numeric) RETURNS numeric AS
        \'SELECT greatest($1, greatest($2, $3));\'
        LANGUAGE \'sql\''
      );
      // Don't use {} around pg_proc table.
      if (!db_query("SELECT COUNT(*) FROM pg_proc WHERE proname = 'rand'")->fetchField()) {
        db_query('CREATE OR REPLACE FUNCTION "rand"() RETURNS float AS
          \'SELECT random();\'
          LANGUAGE \'sql\''
        );
      }

      db_query('CREATE OR REPLACE FUNCTION "substring_index"(text, text, integer) RETURNS text AS
        \'SELECT array_to_string((string_to_array($1, $2)) [1:$3], $2);\'
        LANGUAGE \'sql\''
      );

      // Using || to concatenate in Drupal is not recommended because there are
      // database drivers for Drupal that do not support the syntax, however
      // they do support CONCAT(item1, item2) which we can replicate in
      // PostgreSQL. PostgreSQL requires the function to be defined for each
      // different argument variation the function can handle.
      db_query('CREATE OR REPLACE FUNCTION "concat"(anynonarray, anynonarray) RETURNS text AS
        \'SELECT CAST($1 AS text) || CAST($2 AS text);\'
        LANGUAGE \'sql\'
      ');
      db_query('CREATE OR REPLACE FUNCTION "concat"(text, anynonarray) RETURNS text AS
        \'SELECT $1 || CAST($2 AS text);\'
        LANGUAGE \'sql\'
      ');
      db_query('CREATE OR REPLACE FUNCTION "concat"(anynonarray, text) RETURNS text AS
        \'SELECT CAST($1 AS text) || $2;\'
        LANGUAGE \'sql\'
      ');
      db_query('CREATE OR REPLACE FUNCTION "concat"(text, text) RETURNS text AS
        \'SELECT $1 || $2;\'
        LANGUAGE \'sql\'
      ');

      $this->pass(st('PostgreSQL has initialized itself.'));
    }
    catch (Exception $e) {
      $this->fail(st('Drupal could not be correctly setup with the existing database. Revise any errors.'));
    }
  }
```

---
_Drupal 7.103 · [includes/database/pgsql/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
