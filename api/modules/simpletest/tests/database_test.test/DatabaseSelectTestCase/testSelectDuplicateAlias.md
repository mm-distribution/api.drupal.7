# DatabaseSelectTestCase::testSelectDuplicateAlias()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 1844–1849 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L1844-L1849)
- **Class:** [DatabaseSelectTestCase](../DatabaseSelectTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testSelectDuplicateAlias()
```

## Documentation

```text
Test that aliases are renamed when duplicates.
```

## Code

```php
  function testSelectDuplicateAlias() {
    $query = db_select('test', 't');
    $alias1 = $query->addField('t', 'name', 'the_alias');
    $alias2 = $query->addField('t', 'age', 'the_alias');
    $this->assertNotIdentical($alias1, $alias2, 'Duplicate aliases are renamed.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
