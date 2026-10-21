# FileNameMungingTest::testMungeIgnoreWhitelisted()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 2861–2869 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L2861-L2869)
- **Class:** [FileNameMungingTest](../FileNameMungingTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testMungeIgnoreWhitelisted()
```

## Documentation

```text
White listed extensions are ignored by file_munge_filename().
```

## Code

```php
  function testMungeIgnoreWhitelisted() {
    // Declare our extension as whitelisted. The declared extensions should
    // be case insensitive so test using one with a different case.
    $munged_name = file_munge_filename($this->name_with_uc_ext, $this->bad_extension);
    $this->assertIdentical($munged_name, $this->name_with_uc_ext, format_string('The new filename (%munged) matches the original (%original) once the extension has been whitelisted.', array('%munged' => $munged_name, '%original' => $this->name_with_uc_ext)));
    // The allowed extensions should also be normalized.
    $munged_name = file_munge_filename($this->name, strtoupper($this->bad_extension));
    $this->assertIdentical($munged_name, $this->name, format_string('The new filename (%munged) matches the original (%original) also when the whitelisted extension is in uppercase.', array('%munged' => $munged_name, '%original' => $this->name)));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
