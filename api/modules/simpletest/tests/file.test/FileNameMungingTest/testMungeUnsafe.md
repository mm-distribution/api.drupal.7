# FileNameMungingTest::testMungeUnsafe()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 2874–2881 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L2874-L2881)
- **Class:** [FileNameMungingTest](../FileNameMungingTest.md)
- **Module/theme:** batch_test

## Signature

```php
public function testMungeUnsafe()
```

## Documentation

```text
Tests unsafe extensions are munged by file_munge_filename().
```

## Code

```php
  public function testMungeUnsafe() {
    $prefix = $this->randomName();
    $name = "$prefix.php.txt";
    // Put the php extension in the allowed list, but since it is in the unsafe
    // extension list, it should still be munged.
    $munged_name = file_munge_filename($name, 'php txt');
    $this->assertIdentical($munged_name, "$prefix.php_.txt", format_string('The filename (%munged) has been modified from the original (%original) if the allowed extension is also on the unsafe list.', array('%munged' => $munged_name, '%original' => $name)));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
