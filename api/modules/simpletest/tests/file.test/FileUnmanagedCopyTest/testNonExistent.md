# FileUnmanagedCopyTest::testNonExistent()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 1687–1693 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L1687-L1693)
- **Class:** [FileUnmanagedCopyTest](../FileUnmanagedCopyTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testNonExistent()
```

## Documentation

```text
Copy a non-existent file.
```

## Code

```php
  function testNonExistent() {
    // Copy non-existent file
    $desired_filepath = $this->randomName();
    $this->assertFalse(file_exists($desired_filepath), "Randomly named file doesn't exists.");
    $new_filepath = file_unmanaged_copy($desired_filepath, $this->randomName());
    $this->assertFalse($new_filepath, 'Copying a missing file fails.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
