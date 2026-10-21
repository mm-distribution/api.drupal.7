# MenuTreeOutputTestCase

- **Type:** Class
- **File:** [`modules/simpletest/tests/menu.test`](_file.md), lines 986–1039 · [local source](../../../../../source/modules/simpletest/tests/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test#L986-L1039)
- **Module/theme:** batch_test

## Signature

```php
class MenuTreeOutputTestCase extends DrupalWebTestCase
```

## Documentation

```text
Menu tree output related tests.
```

## Properties

### $tree_data

```php
var $tree_data = array(
    '1'=> array(
      'link' => array( 'menu_name' => 'main-menu', 'mlid' => 1, 'hidden'=>0, 'has_children' => 1, 'title' => 'Item 1', 'in_active_trail' => 1, 'access'=>1, 'href' => 'a', 'localized_options' => array('attributes' => array('title' =>'')) ),
      'below' => array(
        '2' => array('link' => array( 'menu_name' => 'main-menu', 'mlid' => 2, 'hidden'=>0, 'has_children' => 1, 'title' => 'Item 2', 'in_active_trail' => 1, 'access'=>1, 'href' => 'a/b', 'localized_options' => array('attributes' => array('title' =>'')) ),
          'below' => array(
            '3' => array('link' => array( 'menu_name' => 'main-menu', 'mlid' => 3, 'hidden'=>0, 'has_children' => 0, 'title' => 'Item 3', 'in_active_trail' => 0, 'access'=>1, 'href' => 'a/b/c', 'localized_options' => array('attributes' => array('title' =>'')) ),
              'below' => array() ),
            '4' => array('link' => array( 'menu_name' => 'main-menu', 'mlid' => 4, 'hidden'=>0, 'has_children' => 0, 'title' => 'Item 4', 'in_active_trail' => 0, 'access'=>1, 'href' => 'a/b/d', 'localized_options' => array('attributes' => array('title' =>'')) ),
              'below' => array() )
            )
          )
        )
      ),
    '5' => array('link' => array( 'menu_name' => 'main-menu', 'mlid' => 5, 'hidden'=>1, 'has_children' => 0, 'title' => 'Item 5', 'in_active_trail' => 0, 'access'=>1, 'href' => 'e', 'localized_options' => array('attributes' => array('title' =>'')) ), 'below' => array( ) ),
    '6' => array('link' => array( 'menu_name' => 'main-menu', 'mlid' => 6, 'hidden'=>0, 'has_children' => 0, 'title' => 'Item 6', 'in_active_trail' => 0, 'access'=>0, 'href' => 'f', 'localized_options' => array('attributes' => array('title' =>'')) ), 'below' => array( ) ),
    '7' => array('link' => array( 'menu_name' => 'main-menu', 'mlid' => 7, 'hidden'=>0, 'has_children' => 0, 'title' => 'Item 7', 'in_active_trail' => 0, 'access'=>1, 'href' => 'g', 'localized_options' => array('attributes' => array('title' =>'')) ), 'below' => array( ) )
  );
```

```text
Dummy link structure acceptable for menu_tree_output().
```

## Methods (derived index)

- [getInfo()](MenuTreeOutputTestCase/getInfo.md)
- [setUp()](MenuTreeOutputTestCase/setUp.md)
- [testMenuTreeData()](MenuTreeOutputTestCase/testMenuTreeData.md) — Validate the generation of a proper menu tree output.

---
_Drupal 7.103 · [modules/simpletest/tests/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
