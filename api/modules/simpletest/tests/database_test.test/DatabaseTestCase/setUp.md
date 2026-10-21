# DatabaseTestCase::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 22–37 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L22-L37)
- **Class:** [DatabaseTestCase](../DatabaseTestCase.md)
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
    parent::setUp('database_test');

    $schema['test'] = drupal_get_schema('test');
    $schema['test_classtype'] = drupal_get_schema('test_classtype');
    $schema['test_people'] = drupal_get_schema('test_people');
    $schema['test_people_copy'] = drupal_get_schema('test_people_copy');
    $schema['test_one_blob'] = drupal_get_schema('test_one_blob');
    $schema['test_two_blobs'] = drupal_get_schema('test_two_blobs');
    $schema['test_task'] = drupal_get_schema('test_task');
    $schema['TEST_UPPERCASE'] = drupal_get_schema('TEST_UPPERCASE');

    $this->installTables($schema);

    $this->addSampleData();
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
