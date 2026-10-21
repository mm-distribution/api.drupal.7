# FileFieldPathTestCase::assertPathMatch()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 1470–1479 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L1470-L1479)
- **Class:** [FileFieldPathTestCase](../FileFieldPathTestCase.md)
- **Module/theme:** file_module_test

## Signature

```php
function assertPathMatch($expected_path, $actual_path, $message)
```

## Documentation

```text
Asserts that a file is uploaded to the right location.

@param $expected_path
  The location where the file is expected to be uploaded. Duplicate file
  names to not need to be taken into account.
@param $actual_path
  Where the file was actually uploaded.
@param $message
  The message to display with this assertion.
```

## Code

```php
  function assertPathMatch($expected_path, $actual_path, $message) {
    // Strip off the extension of the expected path to allow for _0, _1, etc.
    // suffixes when the file hits a duplicate name.
    $pos = strrpos($expected_path, '.');
    $base_path = substr($expected_path, 0, $pos);
    $extension = substr($expected_path, $pos + 1);

    $result = preg_match('/' . preg_quote($base_path, '/') . '(_[0-9]+)?\.' . preg_quote($extension, '/') . '/', $actual_path);
    $this->assertTrue($result, $message);
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
