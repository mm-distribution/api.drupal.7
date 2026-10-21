# PathLanguageUITestCase::testLanguageNeutralURLs()

- **Type:** Method
- **File:** [`modules/path/path.test`](../_file.md), lines 513–522 · [local source](../../../../../source/modules/path/path.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/path/path.test#L513-L522)
- **Class:** [PathLanguageUITestCase](../PathLanguageUITestCase.md)
- **Module/theme:** path

## Signature

```php
function testLanguageNeutralURLs()
```

## Documentation

```text
Tests that a language-neutral URL alias works.
```

## Code

```php
  function testLanguageNeutralURLs() {
    $name = $this->randomName(8);
    $edit = array();
    $edit['source'] = 'admin/config/search/path';
    $edit['alias'] = $name;
    $this->drupalPost('admin/config/search/path/add', $edit, t('Save'));

    $this->drupalGet($name);
    $this->assertText(t('Filter aliases'), 'Language-neutral URL alias works');
  }
```

---
_Drupal 7.103 · [modules/path/path.test](https://github.com/drupal/drupal/blob/7.103/modules/path/path.test) · Licensed GPL-2.0-or-later (see LICENSE)._
