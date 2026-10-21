# FileLoadTest::testLoadMissingFid()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 2123–2126 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L2123-L2126)
- **Class:** [FileLoadTest](../FileLoadTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testLoadMissingFid()
```

## Documentation

```text
Try to load a non-existent file by fid.
```

## Code

```php
  function testLoadMissingFid() {
    $this->assertFalse(file_load(-1), "Try to load an invalid fid fails.");
    $this->assertFileHooksCalled(array());
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
