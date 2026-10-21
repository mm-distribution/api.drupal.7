# SimpleTestFolderTestCase::testFolderSetup()

- **Type:** Method
- **File:** [`modules/simpletest/simpletest.test`](../_file.md), lines 550–553 · [local source](../../../../../source/modules/simpletest/simpletest.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test#L550-L553)
- **Class:** [SimpleTestFolderTestCase](../SimpleTestFolderTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
function testFolderSetup()
```

## Documentation

_No docblock in source._

## Code

```php
  function testFolderSetup() {
    $directory = file_default_scheme() . '://styles';
    $this->assertTrue(file_prepare_directory($directory, FALSE), 'Directory created.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test) · Licensed GPL-2.0-or-later (see LICENSE)._
