# UpdateTestFileTransfer::factory()

- **Type:** Method
- **File:** [`modules/update/tests/update_test.module`](../_file.md), lines 167–169 · [local source](../../../../../../source/modules/update/tests/update_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/tests/update_test.module#L167-L169)
- **Class:** [UpdateTestFileTransfer](../UpdateTestFileTransfer.md)
- **Module/theme:** aaa_update_test

## Signature

```php
public static function factory()
```

## Documentation

```text
Returns an UpdateTestFileTransfer object.

@return
  A new UpdateTestFileTransfer object.
```

## Code

```php
  public static function factory() {
    return new UpdateTestFileTransfer;
  }
```

---
_Drupal 7.103 · [modules/update/tests/update_test.module](https://github.com/drupal/drupal/blob/7.103/modules/update/tests/update_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
