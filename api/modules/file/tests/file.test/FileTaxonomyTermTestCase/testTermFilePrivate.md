# FileTaxonomyTermTestCase::testTermFilePrivate()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 319–321 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L319-L321)
- **Class:** [FileTaxonomyTermTestCase](../FileTaxonomyTermTestCase.md)
- **Module/theme:** file_module_test

## Signature

```php
public function testTermFilePrivate()
```

## Documentation

```text
Tests that a private file can be attached to a taxonomy term.

This is a regression test for https://www.drupal.org/node/2305017.
```

## Code

```php
  public function testTermFilePrivate() {
    $this->_testTermFile('private');
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
