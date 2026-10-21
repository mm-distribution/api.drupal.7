# DatabaseTaggingTestCase::testHasAnyTag()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 2835–2844 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L2835-L2844)
- **Class:** [DatabaseTaggingTestCase](../DatabaseTaggingTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testHasAnyTag()
```

## Documentation

```text
Test query tagging "has at least one of these tags" functionality.
```

## Code

```php
  function testHasAnyTag() {
    $query = db_select('test');
    $query->addField('test', 'name');
    $query->addField('test', 'age', 'age');

    $query->addTag('test');

    $this->assertTrue($query->hasAnyTag('test', 'other'), 'hasAnyTag() returned true.');
    $this->assertFalse($query->hasAnyTag('other', 'stuff'), 'hasAnyTag() returned false.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
