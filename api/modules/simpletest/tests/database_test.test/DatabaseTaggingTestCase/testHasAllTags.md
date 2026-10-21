# DatabaseTaggingTestCase::testHasAllTags()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 2820–2830 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L2820-L2830)
- **Class:** [DatabaseTaggingTestCase](../DatabaseTaggingTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testHasAllTags()
```

## Documentation

```text
Test query tagging "has all of these tags" functionality.
```

## Code

```php
  function testHasAllTags() {
    $query = db_select('test');
    $query->addField('test', 'name');
    $query->addField('test', 'age', 'age');

    $query->addTag('test');
    $query->addTag('other');

    $this->assertTrue($query->hasAllTags('test', 'other'), 'hasAllTags() returned true.');
    $this->assertFalse($query->hasAllTags('test', 'stuff'), 'hasAllTags() returned false.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
