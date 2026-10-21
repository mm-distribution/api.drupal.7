# BlockTestCase::testBlockVisibilityPerUser()

- **Type:** Method
- **File:** [`modules/block/block.test`](../_file.md), lines 241–287 · [local source](../../../../../source/modules/block/block.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test#L241-L287)
- **Class:** [BlockTestCase](../BlockTestCase.md)
- **Module/theme:** block

## Signature

```php
function testBlockVisibilityPerUser()
```

## Documentation

```text
Test user customization of block visibility.
```

## Code

```php
  function testBlockVisibilityPerUser() {
    $block = array();

    // Create a random title for the block.
    $title = $this->randomName(8);

    // Create our custom test block.
    $custom_block = array();
    $custom_block['info'] = $this->randomName(8);
    $custom_block['title'] = $title;
    $custom_block['body[value]'] = $this->randomName(32);
    $this->drupalPost('admin/structure/block/add', $custom_block, t('Save block'));

    $bid = db_query("SELECT bid FROM {block_custom} WHERE info = :info", array(':info' => $custom_block['info']))->fetchField();
    $block['module'] = 'block';
    $block['delta'] = $bid;
    $block['title'] = $title;

    // Move block to the first sidebar.
    $this->moveBlockToRegion($block, $this->regions[1]);

    // Set the block to be customizable per user, visible by default.
    $edit = array();
    $edit['custom'] = BLOCK_CUSTOM_ENABLED;
    $this->drupalPost('admin/structure/block/manage/' . $block['module'] . '/' . $block['delta'] . '/configure', $edit, t('Save block'));

    // Disable block visibility for the admin user.
    $edit = array();
    $edit['block[' . $block['module'] . '][' . $block['delta'] . ']'] = FALSE;
    $this->drupalPost('user/' . $this->admin_user->uid . '/edit', $edit, t('Save'));

    $this->drupalGet('');
    $this->assertNoText($block['title'], 'Block was not displayed according to per user block visibility setting.');

    // Set the block to be customizable per user, hidden by default.
    $edit = array();
    $edit['custom'] = BLOCK_CUSTOM_DISABLED;
    $this->drupalPost('admin/structure/block/manage/' . $block['module'] . '/' . $block['delta'] . '/configure', $edit, t('Save block'));

    // Enable block visibility for the admin user.
    $edit = array();
    $edit['block[' . $block['module'] . '][' . $block['delta'] . ']'] = TRUE;
    $this->drupalPost('user/' . $this->admin_user->uid . '/edit', $edit, t('Save'));

    $this->drupalGet('');
    $this->assertText($block['title'], 'Block was displayed according to per user block visibility setting.');
  }
```

---
_Drupal 7.103 · [modules/block/block.test](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test) · Licensed GPL-2.0-or-later (see LICENSE)._
