# NodeBlockTestCase::testSyndicateBlock()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 858–868 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L858-L868)
- **Class:** [NodeBlockTestCase](../NodeBlockTestCase.md)
- **Module/theme:** node

## Signature

```php
function testSyndicateBlock()
```

## Documentation

```text
Tests that the "Syndicate" block is shown when enabled.
```

## Code

```php
  function testSyndicateBlock() {
    // Set block title to confirm that the interface is available.
    $this->drupalPost('admin/structure/block/manage/node/syndicate/configure', array('title' => $this->randomName(8)), t('Save block'));
    $this->assertText(t('The block configuration has been saved.'), 'Block configuration set.');

    // Set the block to a region to confirm block is available.
    $edit = array();
    $edit['blocks[node_syndicate][region]'] = 'footer';
    $this->drupalPost('admin/structure/block', $edit, t('Save blocks'));
    $this->assertText(t('The block settings have been updated.'), 'Block successfully move to footer region.');
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
