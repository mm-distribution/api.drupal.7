# FileLoadTest::testLoadInvalidStatus()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 2140–2144 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L2140-L2144)
- **Class:** [FileLoadTest](../FileLoadTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testLoadInvalidStatus()
```

## Documentation

```text
Try to load a non-existent file by status.
```

## Code

```php
  function testLoadInvalidStatus() {
    $files = file_load_multiple(array(), array('status' => -99));
    $this->assertFalse(reset($files), "Trying to load a file with an invalid status fails.");
    $this->assertFileHooksCalled(array());
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
