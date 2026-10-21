# DatabaseSelectComplexTestCase2::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 2504–2516 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L2504-L2516)
- **Class:** [DatabaseSelectComplexTestCase2](../DatabaseSelectComplexTestCase2.md)
- **Module/theme:** batch_test

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    DrupalWebTestCase::setUp('database_test', 'node_access_test');

    $schema['test'] = drupal_get_schema('test');
    $schema['test_people'] = drupal_get_schema('test_people');
    $schema['test_one_blob'] = drupal_get_schema('test_one_blob');
    $schema['test_two_blobs'] = drupal_get_schema('test_two_blobs');
    $schema['test_task'] = drupal_get_schema('test_task');

    $this->installTables($schema);

    $this->addSampleData();
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
