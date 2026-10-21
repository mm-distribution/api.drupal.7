# FileTaxonomyTermTestCase::testTermFilePublic()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 310–312 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L310-L312)
- **Class:** [FileTaxonomyTermTestCase](../FileTaxonomyTermTestCase.md)
- **Module/theme:** file_module_test

## Signature

```php
public function testTermFilePublic()
```

## Documentation

```text
Tests that a public file can be attached to a taxonomy term.

This is a regression test for https://www.drupal.org/node/2305017.
```

## Code

```php
  public function testTermFilePublic() {
    $this->_testTermFile('public');
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
