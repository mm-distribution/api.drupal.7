# FileNameMungingTest::testUnMunge()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 2886–2890 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L2886-L2890)
- **Class:** [FileNameMungingTest](../FileNameMungingTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testUnMunge()
```

## Documentation

```text
Ensure that unmunge gets your name back.
```

## Code

```php
  function testUnMunge() {
    $munged_name = file_munge_filename($this->name, '', FALSE);
    $unmunged_name = file_unmunge_filename($munged_name);
    $this->assertIdentical($unmunged_name, $this->name, format_string('The unmunged (%unmunged) filename matches the original (%original)', array('%unmunged' => $unmunged_name, '%original' => $this->name)));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
