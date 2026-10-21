# FileTestCase::assertDirectoryPermissions()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 141–165 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L141-L165)
- **Class:** [FileTestCase](../FileTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function assertDirectoryPermissions($directory, $expected_mode, $message = NULL)
```

## Documentation

```text
Helper function to test the permissions of a directory.

@param $directory
  String directory path.
@param $expected_mode
  Octal integer like 0664 or 0777.
@param $message
  Optional message.
```

## Code

```php
  function assertDirectoryPermissions($directory, $expected_mode, $message = NULL) {
    // Clear out PHP's file stat cache to be sure we see the current value.
    clearstatcache();

    // Mask out all but the last three octets.
    $actual_mode = fileperms($directory) & 0777;
    $expected_mode = $expected_mode & 0777;

    // PHP on Windows has limited support for file permissions. Usually each of
    // "user", "group" and "other" use one octal digit (3 bits) to represent the
    // read/write/execute bits. On Windows, chmod() ignores the "group" and
    // "other" bits, and fileperms() returns the "user" bits in all three
    // positions. $expected_mode is updated to reflect this.
    if (substr(PHP_OS, 0, 3) == 'WIN') {
      // Reset the "group" and "other" bits.
      $expected_mode = $expected_mode & 0700;
      // Shift the "user" bits to the "group" and "other" positions also.
      $expected_mode = $expected_mode | $expected_mode >> 3 | $expected_mode >> 6;
    }

    if (!isset($message)) {
      $message = t('Expected directory permission to be %expected, actually were %actual.', array('%actual' => decoct($actual_mode), '%expected' => decoct($expected_mode)));
    }
    $this->assertEqual($actual_mode, $expected_mode, $message);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
