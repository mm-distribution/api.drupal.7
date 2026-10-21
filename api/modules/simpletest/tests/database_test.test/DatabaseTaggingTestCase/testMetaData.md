# DatabaseTaggingTestCase::testMetaData()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 2897–2914 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L2897-L2914)
- **Class:** [DatabaseTaggingTestCase](../DatabaseTaggingTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testMetaData()
```

## Documentation

```text
Test that we can attach meta data to a query object.

This is how we pass additional context to alter hooks.
```

## Code

```php
  function testMetaData() {
    $query = db_select('test');
    $query->addField('test', 'name');
    $query->addField('test', 'age', 'age');

    $data = array(
      'a' => 'A',
      'b' => 'B',
    );

    $query->addMetaData('test', $data);

    $return = $query->getMetaData('test');
    $this->assertEqual($data, $return, 'Corect metadata returned.');

    $return = $query->getMetaData('nothere');
    $this->assertNull($return, 'Non-existent key returned NULL.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
