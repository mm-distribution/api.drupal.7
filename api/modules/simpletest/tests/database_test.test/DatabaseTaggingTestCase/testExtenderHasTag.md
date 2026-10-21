# DatabaseTaggingTestCase::testExtenderHasTag()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 2849–2859 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L2849-L2859)
- **Class:** [DatabaseTaggingTestCase](../DatabaseTaggingTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testExtenderHasTag()
```

## Documentation

```text
Confirm that an extended query has a "tag" added to it.
```

## Code

```php
  function testExtenderHasTag() {
    $query = db_select('test')
      ->extend('SelectQueryExtender');
    $query->addField('test', 'name');
    $query->addField('test', 'age', 'age');

    $query->addTag('test');

    $this->assertTrue($query->hasTag('test'), 'hasTag() returned true.');
    $this->assertFalse($query->hasTag('other'), 'hasTag() returned false.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
