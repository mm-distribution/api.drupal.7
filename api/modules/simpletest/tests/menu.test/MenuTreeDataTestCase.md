# MenuTreeDataTestCase

- **Type:** Class
- **File:** [`modules/simpletest/tests/menu.test`](_file.md), lines 931–981 · [local source](../../../../../source/modules/simpletest/tests/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test#L931-L981)
- **Module/theme:** batch_test

## Signature

```php
class MenuTreeDataTestCase extends DrupalUnitTestCase
```

## Documentation

```text
Menu tree data related tests.
```

## Properties

### $links

```php
var $links = array(
    1 => array('mlid' => 1, 'depth' => 1),
    2 => array('mlid' => 2, 'depth' => 1),
    3 => array('mlid' => 3, 'depth' => 2),
    4 => array('mlid' => 4, 'depth' => 3),
    5 => array('mlid' => 5, 'depth' => 1),
  );
```

```text
Dummy link structure acceptable for menu_tree_data().
```

## Methods (derived index)

- [getInfo()](MenuTreeDataTestCase/getInfo.md)
- [testMenuTreeData()](MenuTreeDataTestCase/testMenuTreeData.md) — Validate the generation of a proper menu tree hierarchy.
- [assertSameLink()](MenuTreeDataTestCase/assertSameLink.md) — Check that two menu links are the same by comparing the mlid.

---
_Drupal 7.103 · [modules/simpletest/tests/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
