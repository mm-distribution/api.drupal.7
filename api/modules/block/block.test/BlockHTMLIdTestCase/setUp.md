# BlockHTMLIdTestCase::setUp()

- **Type:** Method
- **File:** [`modules/block/block.test`](../_file.md), lines 689–703 · [local source](../../../../../source/modules/block/block.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test#L689-L703)
- **Class:** [BlockHTMLIdTestCase](../BlockHTMLIdTestCase.md)
- **Module/theme:** block

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('block_test');

    // Create an admin user, log in and enable test blocks.
    $this->admin_user = $this->drupalCreateUser(array('administer blocks', 'access administration pages'));
    $this->drupalLogin($this->admin_user);

    // Enable our test block.
    $edit['blocks[block_test_test_html_id][region]'] = 'sidebar_first';
    $this->drupalPost('admin/structure/block', $edit, t('Save blocks'));

    // Make sure the block has some content so it will appear
    $current_content = $this->randomName();
    variable_set('block_test_content', $current_content);
  }
```

---
_Drupal 7.103 · [modules/block/block.test](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test) · Licensed GPL-2.0-or-later (see LICENSE)._
