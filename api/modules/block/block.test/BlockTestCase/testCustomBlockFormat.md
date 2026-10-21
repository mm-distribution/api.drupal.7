# BlockTestCase::testCustomBlockFormat()

- **Type:** Method
- **File:** [`modules/block/block.test`](../_file.md), lines 115–147 · [local source](../../../../../source/modules/block/block.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test#L115-L147)
- **Class:** [BlockTestCase](../BlockTestCase.md)
- **Module/theme:** block

## Signature

```php
function testCustomBlockFormat()
```

## Documentation

```text
Test creating custom block using Full HTML.
```

## Code

```php
  function testCustomBlockFormat() {
    // Add a new custom block by filling out the input form on the admin/structure/block/add page.
    $custom_block = array();
    $custom_block['info'] = $this->randomName(8);
    $custom_block['title'] = $this->randomName(8);
    $custom_block['body[value]'] = '<h1>Full HTML</h1>';
    $full_html_format = filter_format_load('full_html');
    $custom_block['body[format]'] = $full_html_format->format;
    $this->drupalPost('admin/structure/block/add', $custom_block, t('Save block'));

    // Set the created custom block to a specific region.
    $bid = db_query("SELECT bid FROM {block_custom} WHERE info = :info", array(':info' => $custom_block['info']))->fetchField();
    $edit = array();
    $edit['blocks[block_' . $bid . '][region]'] = $this->regions[1];
    $this->drupalPost('admin/structure/block', $edit, t('Save blocks'));

    // Confirm that the custom block is being displayed using configured text format.
    $this->drupalGet('node');
    $this->assertRaw('<h1>Full HTML</h1>', 'Custom block successfully being displayed using Full HTML.');

    // Confirm that a user without access to Full HTML can not see the body field,
    // but can still submit the form without errors.
    $block_admin = $this->drupalCreateUser(array('administer blocks'));
    $this->drupalLogin($block_admin);
    $this->drupalGet('admin/structure/block/manage/block/' . $bid . '/configure');
    $this->assertFieldByXPath("//textarea[@name='body[value]' and @disabled='disabled']", t('This field has been disabled because you do not have sufficient permissions to edit it.'), 'Body field contains denied message');
    $this->drupalPost('admin/structure/block/manage/block/' . $bid . '/configure', array(), t('Save block'));
    $this->assertNoText(t('Ensure that each block description is unique.'));

    // Confirm that the custom block is still being displayed using configured text format.
    $this->drupalGet('node');
    $this->assertRaw('<h1>Full HTML</h1>', 'Custom block successfully being displayed using Full HTML.');
  }
```

---
_Drupal 7.103 · [modules/block/block.test](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test) · Licensed GPL-2.0-or-later (see LICENSE)._
