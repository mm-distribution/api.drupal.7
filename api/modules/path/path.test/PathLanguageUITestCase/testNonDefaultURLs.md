# PathLanguageUITestCase::testNonDefaultURLs()

- **Type:** Method
- **File:** [`modules/path/path.test`](../_file.md), lines 542–552 · [local source](../../../../../source/modules/path/path.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/path/path.test#L542-L552)
- **Class:** [PathLanguageUITestCase](../PathLanguageUITestCase.md)
- **Module/theme:** path

## Signature

```php
function testNonDefaultURLs()
```

## Documentation

```text
Tests that a non-default language URL alias works.
```

## Code

```php
  function testNonDefaultURLs() {
    $name = $this->randomName(8);
    $edit = array();
    $edit['source'] = 'admin/config/search/path';
    $edit['alias'] = $name;
    $edit['language'] = 'fr';
    $this->drupalPost('admin/config/search/path/add', $edit, t('Save'));

    $this->drupalGet('fr/' . $name);
    $this->assertText(t('Filter aliases'), 'Foreign URL alias works');
  }
```

---
_Drupal 7.103 · [modules/path/path.test](https://github.com/drupal/drupal/blob/7.103/modules/path/path.test) · Licensed GPL-2.0-or-later (see LICENSE)._
