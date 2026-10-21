# BlockHiddenRegionTestCase::testBlockNotInHiddenRegion()

- **Type:** Method
- **File:** [`modules/block/block.test`](../_file.md), lines 817–835 · [local source](../../../../../source/modules/block/block.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test#L817-L835)
- **Class:** [BlockHiddenRegionTestCase](../BlockHiddenRegionTestCase.md)
- **Module/theme:** block

## Signature

```php
function testBlockNotInHiddenRegion()
```

## Documentation

```text
Tests that hidden regions do not inherit blocks when a theme is enabled.
```

## Code

```php
  function testBlockNotInHiddenRegion() {
    // Create administrative user.
    $admin_user = $this->drupalCreateUser(array('administer blocks', 'administer themes', 'search content'));
    $this->drupalLogin($admin_user);

    // Enable "block_test_theme" and set it as the default theme.
    $theme = 'block_test_theme';
    theme_enable(array($theme));
    variable_set('theme_default', $theme);
    menu_rebuild();

    // Ensure that "block_test_theme" is set as the default theme.
    $this->drupalGet('admin/structure/block');
    $this->assertText('Block test theme(' . t('active tab') . ')', 'Default local task on blocks admin page is the block test theme.');

    // Ensure that the search form block is displayed.
    $this->drupalGet('');
    $this->assertText('Search form', 'Block was displayed on the front page.');
  }
```

---
_Drupal 7.103 · [modules/block/block.test](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test) · Licensed GPL-2.0-or-later (see LICENSE)._
