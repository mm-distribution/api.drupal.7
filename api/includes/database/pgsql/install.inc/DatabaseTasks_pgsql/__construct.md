# DatabaseTasks_pgsql::__construct()

- **Type:** Method
- **File:** [`includes/database/pgsql/install.inc`](../_file.md), lines 14–31 · [local source](../../../../../../source/includes/database/pgsql/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/install.inc#L14-L31)
- **Class:** [DatabaseTasks_pgsql](../DatabaseTasks_pgsql.md)

## Signature

```php
public function __construct()
```

## Documentation

_No docblock in source._

## Code

```php
  public function __construct() {
    $this->tasks[] = array(
      'function' => 'checkEncoding',
      'arguments' => array(),
    );
    $this->tasks[] = array(
      'function' => 'checkPHPVersion',
      'arguments' => array(),
    );
    $this->tasks[] = array(
      'function' => 'checkBinaryOutput',
      'arguments' => array(),
    );
    $this->tasks[] = array(
      'function' => 'initializeDatabase',
      'arguments' => array(),
    );
  }
```

---
_Drupal 7.103 · [includes/database/pgsql/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
