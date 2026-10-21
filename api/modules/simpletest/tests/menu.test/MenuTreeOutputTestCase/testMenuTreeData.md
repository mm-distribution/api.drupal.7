# MenuTreeOutputTestCase::testMenuTreeData()

- **Type:** Method
- **File:** [`modules/simpletest/tests/menu.test`](../_file.md), lines 1024–1038 · [local source](../../../../../../source/modules/simpletest/tests/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test#L1024-L1038)
- **Class:** [MenuTreeOutputTestCase](../MenuTreeOutputTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testMenuTreeData()
```

## Documentation

```text
Validate the generation of a proper menu tree output.
```

## Code

```php
  function testMenuTreeData() {
    $output = menu_tree_output($this->tree_data);

    // Validate that the - in main-menu is changed into an underscore
    $this->assertEqual($output['1']['#theme'], 'menu_link__main_menu', 'Hyphen is changed to an underscore on menu_link');
    $this->assertEqual($output['#theme_wrappers'][0], 'menu_tree__main_menu', 'Hyphen is changed to an underscore on menu_tree wrapper');
    // Looking for child items in the data
    $this->assertEqual( $output['1']['#below']['2']['#href'], 'a/b', 'Checking the href on a child item');
    $this->assertTrue( in_array('active-trail',$output['1']['#below']['2']['#attributes']['class']) , 'Checking the active trail class');
    // Validate that the hidden and no access items are missing
    $this->assertFalse( isset($output['5']), 'Hidden item should be missing');
    $this->assertFalse( isset($output['6']), 'False access should be missing');
    // Item 7 is after a couple hidden items. Just to make sure that 5 and 6 are skipped and 7 still included
    $this->assertTrue( isset($output['7']), 'Item after hidden items is present');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
