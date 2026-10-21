# FileNameMungingTest::testMungeIgnoreInsecure()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 2852–2856 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L2852-L2856)
- **Class:** [FileNameMungingTest](../FileNameMungingTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testMungeIgnoreInsecure()
```

## Documentation

```text
If the allow_insecure_uploads variable evaluates to true, the file should
come out untouched, no matter how evil the filename.
```

## Code

```php
  function testMungeIgnoreInsecure() {
    variable_set('allow_insecure_uploads', 1);
    $munged_name = file_munge_filename($this->name, '');
    $this->assertIdentical($munged_name, $this->name, format_string('The original filename (%original) matches the munged filename (%munged) when insecure uploads are enabled.', array('%munged' => $munged_name, '%original' => $this->name)));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
