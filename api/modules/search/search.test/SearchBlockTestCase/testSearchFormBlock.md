# SearchBlockTestCase::testSearchFormBlock()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 612–622 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L612-L622)
- **Class:** [SearchBlockTestCase](../SearchBlockTestCase.md)
- **Module/theme:** search

## Signature

```php
function testSearchFormBlock()
```

## Documentation

_No docblock in source._

## Code

```php
  function testSearchFormBlock() {
    // Set block title to confirm that the interface is available.
    $this->drupalPost('admin/structure/block/manage/search/form/configure', array('title' => $this->randomName(8)), t('Save block'));
    $this->assertText(t('The block configuration has been saved.'), 'Block configuration set.');

    // Set the block to a region to confirm block is available.
    $edit = array();
    $edit['blocks[search_form][region]'] = 'footer';
    $this->drupalPost('admin/structure/block', $edit, t('Save blocks'));
    $this->assertText(t('The block settings have been updated.'), 'Block successfully move to footer region.');
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
