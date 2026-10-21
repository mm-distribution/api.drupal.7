# BatchPageTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/batch.test`](../_file.md), lines 281–287 · [local source](../../../../../../source/modules/simpletest/tests/batch.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch.test#L281-L287)
- **Class:** [BatchPageTestCase](../BatchPageTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public static function getInfo()
```

## Documentation

_No docblock in source._

## Code

```php
  public static function getInfo() {
    return array(
      'name' => 'Batch progress page',
      'description' => 'Test the content of the progress page.',
      'group' => 'Batch API',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/batch.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch.test) · Licensed GPL-2.0-or-later (see LICENSE)._
