# BlockHashTestCase::assertWeight()

- **Type:** Method
- **File:** [`modules/block/block.test`](../_file.md), lines 975–979 · [local source](../../../../../source/modules/block/block.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test#L975-L979)
- **Class:** [BlockHashTestCase](../BlockHashTestCase.md)
- **Module/theme:** block

## Signature

```php
function assertWeight($weight)
```

## Documentation

```text
Asserts that the block_test module's block has a given weight.

@param $weight
  The expected weight.
```

## Code

```php
  function assertWeight($weight) {
    $db_weight = db_query('SELECT weight FROM {block} WHERE module = :module AND delta = :delta', array(':module' => 'block_test', ':delta' => 'test_html_id'))->fetchField();
    // By casting to string the assert fails on FALSE.
    $this->assertIdentical((string) $db_weight, (string) $weight);
  }
```

---
_Drupal 7.103 · [modules/block/block.test](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test) · Licensed GPL-2.0-or-later (see LICENSE)._
