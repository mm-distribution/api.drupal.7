# BlockTestCase::testBlock()

- **Type:** Method
- **File:** [`modules/block/block.test`](../_file.md), lines 292–336 · [local source](../../../../../source/modules/block/block.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test#L292-L336)
- **Class:** [BlockTestCase](../BlockTestCase.md)
- **Module/theme:** block

## Signature

```php
function testBlock()
```

## Documentation

```text
Test configuring and moving a module-define block to specific regions.
```

## Code

```php
  function testBlock() {
    // Select the Navigation block to be configured and moved.
    $block = array();
    $block['module'] = 'system';
    $block['delta'] = 'management';
    $block['title'] = $this->randomName(8);

    // Set block title to confirm that interface works and override any custom titles.
    $this->drupalPost('admin/structure/block/manage/' . $block['module'] . '/' . $block['delta'] . '/configure', array('title' => $block['title']), t('Save block'));
    $this->assertText(t('The block configuration has been saved.'), 'Block title set.');
    $bid = db_query("SELECT bid FROM {block} WHERE module = :module AND delta = :delta", array(
      ':module' => $block['module'],
      ':delta' => $block['delta'],
    ))->fetchField();

    // Check to see if the block was created by checking that it's in the database.
    $this->assertTrue($bid, 'Block found in database');

    // Check whether the block can be moved to all available regions.
    foreach ($this->regions as $region) {
      $this->moveBlockToRegion($block, $region);
    }

    // Set the block to the disabled region.
    $edit = array();
    $edit['blocks[' . $block['module'] . '_' . $block['delta'] . '][region]'] = '-1';
    $this->drupalPost('admin/structure/block', $edit, t('Save blocks'));

    // Confirm that the block was moved to the proper region.
    $this->assertText(t('The block settings have been updated.'), 'Block successfully move to disabled region.');
    $this->assertNoText(t($block['title']), 'Block no longer appears on page.');

    // Confirm that the region's xpath is not available.
    $xpath = $this->buildXPathQuery('//div[@id=:id]/*', array(':id' => 'block-block-' . $bid));
    $this->assertNoFieldByXPath($xpath, FALSE, 'Custom block found in no regions.');

    // For convenience of developers, put the navigation block back.
    $edit = array();
    $edit['blocks[' . $block['module'] . '_' . $block['delta'] . '][region]'] = $this->regions[1];
    $this->drupalPost('admin/structure/block', $edit, t('Save blocks'));
    $this->assertText(t('The block settings have been updated.'), 'Block successfully move to first sidebar region.');

    $this->drupalPost('admin/structure/block/manage/' . $block['module'] . '/' . $block['delta'] . '/configure', array('title' => 'Navigation'), t('Save block'));
    $this->assertText(t('The block configuration has been saved.'), 'Block title set.');
  }
```

---
_Drupal 7.103 · [modules/block/block.test](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test) · Licensed GPL-2.0-or-later (see LICENSE)._
