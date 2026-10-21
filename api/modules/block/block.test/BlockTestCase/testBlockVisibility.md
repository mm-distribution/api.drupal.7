# BlockTestCase::testBlockVisibility()

- **Type:** Method
- **File:** [`modules/block/block.test`](../_file.md), lines 152–193 · [local source](../../../../../source/modules/block/block.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test#L152-L193)
- **Class:** [BlockTestCase](../BlockTestCase.md)
- **Module/theme:** block

## Signature

```php
function testBlockVisibility()
```

## Documentation

```text
Test block visibility.
```

## Code

```php
  function testBlockVisibility() {
    $block = array();

    // Create a random title for the block
    $title = $this->randomName(8);

    // Create the custom block
    $custom_block = array();
    $custom_block['info'] = $this->randomName(8);
    $custom_block['title'] = $title;
    $custom_block['body[value]'] = $this->randomName(32);
    $this->drupalPost('admin/structure/block/add', $custom_block, t('Save block'));

    $bid = db_query("SELECT bid FROM {block_custom} WHERE info = :info", array(':info' => $custom_block['info']))->fetchField();
    $block['module'] = 'block';
    $block['delta'] = $bid;
    $block['title'] = $title;

    // Set the block to be hidden on any user path, and to be shown only to
    // authenticated users.
    $edit = array();
    $edit['pages'] = 'user*';
    $edit['roles[' . DRUPAL_AUTHENTICATED_RID . ']'] = TRUE;
    $this->drupalPost('admin/structure/block/manage/' . $block['module'] . '/' . $block['delta'] . '/configure', $edit, t('Save block'));

    // Move block to the first sidebar.
    $this->moveBlockToRegion($block, $this->regions[1]);

    $this->drupalGet('');
    $this->assertText($title, 'Block was displayed on the front page.');

    $this->drupalGet('user');
    $this->assertNoText($title, 'Block was not displayed according to block visibility rules.');

    $this->drupalGet('USER/' . $this->admin_user->uid);
    $this->assertNoText($title, 'Block was not displayed according to block visibility rules regardless of path case.');

    // Confirm that the block is not displayed to anonymous users.
    $this->drupalLogout();
    $this->drupalGet('');
    $this->assertNoText($title, 'Block was not displayed to anonymous users.');
  }
```

---
_Drupal 7.103 · [modules/block/block.test](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test) · Licensed GPL-2.0-or-later (see LICENSE)._
