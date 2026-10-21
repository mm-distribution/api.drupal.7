# DatabaseConnection_pgsql::nextId()

- **Type:** Method
- **File:** [`includes/database/pgsql/database.inc`](../_file.md), lines 184–219 · [local source](../../../../../../source/includes/database/pgsql/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/database.inc#L184-L219)
- **Class:** [DatabaseConnection_pgsql](../DatabaseConnection_pgsql.md)
- **Topics:** [database](../../../../../topics/database.md)

## Signature

```php
public function nextId($existing = 0)
```

## Documentation

```text
Retrieve the next id in a sequence.

PostgreSQL has built in sequences. We'll use these instead of inserting
and updating a sequences table.
```

## Code

```php
  public function nextId($existing = 0) {

    // Retrieve the name of the sequence. This information cannot be cached
    // because the prefix may change, for example, like it does in simpletests.
    $sequence_name = $this->makeSequenceName('sequences', 'value');

    // When PostgreSQL gets a value too small then it will lock the table,
    // retry the INSERT and if it's still too small then alter the sequence.
    $id = $this->query("SELECT nextval('" . $sequence_name . "')")->fetchField();
    if ($id > $existing) {
      return $id;
    }

    // PostgreSQL advisory locks are simply locks to be used by an
    // application such as Drupal. This will prevent other Drupal processes
    // from altering the sequence while we are.
    $this->query("SELECT pg_advisory_lock(" . POSTGRESQL_NEXTID_LOCK . ")");

    // While waiting to obtain the lock, the sequence may have been altered
    // so lets try again to obtain an adequate value.
    $id = $this->query("SELECT nextval('" . $sequence_name . "')")->fetchField();
    if ($id > $existing) {
      $this->query("SELECT pg_advisory_unlock(" . POSTGRESQL_NEXTID_LOCK . ")");
      return $id;
    }

    // Reset the sequence to a higher value than the existing id.
    $this->query("ALTER SEQUENCE " . $sequence_name . " RESTART WITH " . ($existing + 1));

    // Retrieve the next id. We know this will be as high as we want it.
    $id = $this->query("SELECT nextval('" . $sequence_name . "')")->fetchField();

    $this->query("SELECT pg_advisory_unlock(" . POSTGRESQL_NEXTID_LOCK . ")");

    return $id;
  }
```

---
_Drupal 7.103 · [includes/database/pgsql/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
