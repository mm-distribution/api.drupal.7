# DatabaseSelectComplexTestCase::testJoinTwice()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 2433–2442 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L2433-L2442)
- **Class:** [DatabaseSelectComplexTestCase](../DatabaseSelectComplexTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testJoinTwice()
```

## Documentation

```text
Confirm we can join on a single table twice with a dynamic alias.
```

## Code

```php
  function testJoinTwice() {
    $query = db_select('test')->fields('test');
    $alias = $query->join('test', 'test', 'test.job = %alias.job');
    $query->addField($alias, 'name', 'othername');
    $query->addField($alias, 'job', 'otherjob');
    $query->where("$alias.name <> test.name");
    $crowded_job = $query->execute()->fetch();
    $this->assertEqual($crowded_job->job, $crowded_job->otherjob, 'Correctly joined same table twice.');
    $this->assertNotEqual($crowded_job->name, $crowded_job->othername, 'Correctly joined same table twice.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
