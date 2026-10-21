# NewDefaultThemeBlocks::testNewDefaultThemeBlocks()

- **Type:** Method
- **File:** [`modules/block/block.test`](../_file.md), lines 418–450 · [local source](../../../../../source/modules/block/block.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test#L418-L450)
- **Class:** [NewDefaultThemeBlocks](../NewDefaultThemeBlocks.md)
- **Module/theme:** block

## Signature

```php
function testNewDefaultThemeBlocks()
```

## Documentation

```text
Check the enabled Bartik blocks are correctly copied over.
```

## Code

```php
  function testNewDefaultThemeBlocks() {
    // Create administrative user.
    $admin_user = $this->drupalCreateUser(array('administer themes'));
    $this->drupalLogin($admin_user);

    // Ensure no other theme's blocks are in the block table yet.
    $themes = array();
    $themes['default'] = variable_get('theme_default', 'bartik');
    if ($admin_theme = variable_get('admin_theme')) {
      $themes['admin'] = $admin_theme;
    }
    $count = db_query_range('SELECT 1 FROM {block} WHERE theme NOT IN (:themes)', 0, 1, array(':themes' => $themes))->fetchField();
    $this->assertFalse($count, 'Only the default theme and the admin theme have blocks.');

    // Populate list of all blocks for matching against new theme.
    $blocks = array();
    $result = db_query('SELECT * FROM {block} WHERE theme = :theme', array(':theme' => $themes['default']));
    foreach ($result as $block) {
      // $block->theme and $block->bid will not match, so remove them.
      unset($block->theme, $block->bid);
      $blocks[$block->module][$block->delta] = $block;
    }

    // Turn on the Stark theme and ensure that it contains all of the blocks
    // the default theme had.
    theme_enable(array('stark'));
    variable_set('theme_default', 'stark');
    $result = db_query('SELECT * FROM {block} WHERE theme = :theme', array(':theme' => 'stark'));
    foreach ($result as $block) {
      unset($block->theme, $block->bid);
      $this->assertEqual($blocks[$block->module][$block->delta], $block, format_string('Block %name matched', array('%name' => $block->module . '-' . $block->delta)));
    }
  }
```

---
_Drupal 7.103 · [modules/block/block.test](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test) · Licensed GPL-2.0-or-later (see LICENSE)._
