# MenuTreeDataTestCase::testMenuTreeData()

- **Type:** Method
- **File:** [`modules/simpletest/tests/menu.test`](../_file.md), lines 954–964 · [local source](../../../../../../source/modules/simpletest/tests/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test#L954-L964)
- **Class:** [MenuTreeDataTestCase](../MenuTreeDataTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testMenuTreeData()
```

## Documentation

```text
Validate the generation of a proper menu tree hierarchy.
```

## Code

```php
  function testMenuTreeData() {
    $tree = menu_tree_data($this->links);

    // Validate that parent items #1, #2, and #5 exist on the root level.
    $this->assertSameLink($this->links[1], $tree[1]['link'], 'Parent item #1 exists.');
    $this->assertSameLink($this->links[2], $tree[2]['link'], 'Parent item #2 exists.');
    $this->assertSameLink($this->links[5], $tree[5]['link'], 'Parent item #5 exists.');

    // Validate that child item #4 exists at the correct location in the hierarchy.
    $this->assertSameLink($this->links[4], $tree[2]['below'][3]['below'][4]['link'], 'Child item #4 exists in the hierarchy.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
