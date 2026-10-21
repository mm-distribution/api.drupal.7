# FileLoadTest::testLoadMissingFilepath()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 2131–2135 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L2131-L2135)
- **Class:** [FileLoadTest](../FileLoadTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testLoadMissingFilepath()
```

## Documentation

```text
Try to load a non-existent file by URI.
```

## Code

```php
  function testLoadMissingFilepath() {
    $files = file_load_multiple(array(), array('uri' => 'foobar://misc/druplicon.png'));
    $this->assertFalse(reset($files), "Try to load a file that doesn't exist in the database fails.");
    $this->assertFileHooksCalled(array());
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
