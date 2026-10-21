# BlockTestCase::testCustomBlock()

- **Type:** Method
- **File:** [`modules/block/block.test`](../_file.md), lines 45–110 · [local source](../../../../../source/modules/block/block.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test#L45-L110)
- **Class:** [BlockTestCase](../BlockTestCase.md)
- **Module/theme:** block

## Signature

```php
function testCustomBlock()
```

## Documentation

```text
Test creating custom block, moving it to a specific region and then deleting it.
```

## Code

```php
  function testCustomBlock() {
    // Confirm that the add block link appears on block overview pages.
    $this->drupalGet('admin/structure/block');
    $this->assertRaw(l('Add block', 'admin/structure/block/add'), 'Add block link is present on block overview page for default theme.');
    $this->drupalGet('admin/structure/block/list/seven');
    $this->assertRaw(l('Add block', 'admin/structure/block/list/seven/add'), 'Add block link is present on block overview page for non-default theme.');

    // Confirm that hidden regions are not shown as options for block placement
    // when adding a new block.
    theme_enable(array('stark'));
    $themes = list_themes();
    $this->drupalGet('admin/structure/block/add');
    foreach ($themes as $key => $theme) {
      if ($theme->status) {
        foreach ($theme->info['regions_hidden'] as $hidden_region) {
          $elements = $this->xpath('//select[@id=:id]//option[@value=:value]', array(':id' => 'edit-regions-' . $key, ':value' => $hidden_region));
          $this->assertFalse(isset($elements[0]), format_string('The hidden region @region is not available for @theme.', array('@region' => $hidden_region, '@theme' => $key)));
        }
      }
    }

    // Add a new custom block by filling out the input form on the admin/structure/block/add page.
    $custom_block = array();
    $custom_block['info'] = $this->randomName(8);
    $custom_block['title'] = $this->randomName(8);
    $custom_block['body[value]'] = $this->randomName(32);
    $this->drupalPost('admin/structure/block/add', $custom_block, t('Save block'));

    // Confirm that the custom block has been created, and then query the created bid.
    $this->assertText(t('The block has been created.'), 'Custom block successfully created.');
    $bid = db_query("SELECT bid FROM {block_custom} WHERE info = :info", array(':info' => $custom_block['info']))->fetchField();

    // Check to see if the custom block was created by checking that it's in the database.
    $this->assertTrue($bid, 'Custom block found in database');

    // Check that block_block_view() returns the correct title and content.
    $data = block_block_view($bid);
    $format = db_query("SELECT format FROM {block_custom} WHERE bid = :bid", array(':bid' => $bid))->fetchField();
    $this->assertTrue(array_key_exists('subject', $data) && empty($data['subject']), 'block_block_view() provides an empty block subject, since custom blocks do not have default titles.');
    $this->assertEqual(check_markup($custom_block['body[value]'], $format), $data['content'], 'block_block_view() provides correct block content.');

    // Check whether the block can be moved to all available regions.
    $custom_block['module'] = 'block';
    $custom_block['delta'] = $bid;
    foreach ($this->regions as $region) {
      $this->moveBlockToRegion($custom_block, $region);
    }

    // Verify presence of configure and delete links for custom block.
    $this->drupalGet('admin/structure/block');
    $this->assertLinkByHref('admin/structure/block/manage/block/' . $bid . '/configure', 0, 'Custom block configure link found.');
    $this->assertLinkByHref('admin/structure/block/manage/block/' . $bid . '/delete', 0, 'Custom block delete link found.');

    // Set visibility only for authenticated users, to verify delete functionality.
    $edit = array();
    $edit['roles[' . DRUPAL_AUTHENTICATED_RID . ']'] = TRUE;
    $this->drupalPost('admin/structure/block/manage/block/' . $bid . '/configure', $edit, t('Save block'));

    // Delete the created custom block & verify that it's been deleted and no longer appearing on the page.
    $this->clickLink(t('delete'));
    $this->drupalPost('admin/structure/block/manage/block/' . $bid . '/delete', array(), t('Delete'));
    $this->assertRaw(t('The block %title has been removed.', array('%title' => $custom_block['info'])), 'Custom block successfully deleted.');
    $this->assertNoText(t($custom_block['title']), 'Custom block no longer appears on page.');
    $count = db_query("SELECT 1 FROM {block_role} WHERE module = :module AND delta = :delta", array(':module' => $custom_block['module'], ':delta' => $custom_block['delta']))->fetchField();
    $this->assertFalse($count, 'Table block_role being cleaned.');
  }
```

---
_Drupal 7.103 · [modules/block/block.test](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test) · Licensed GPL-2.0-or-later (see LICENSE)._
