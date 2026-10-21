# MenuLinksUnitTestCase::assertMenuLinkParents()

- **Type:** Method
- **File:** [`modules/simpletest/tests/menu.test`](../_file.md), lines 740–749 · [local source](../../../../../../source/modules/simpletest/tests/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test#L740-L749)
- **Class:** [MenuLinksUnitTestCase](../MenuLinksUnitTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function assertMenuLinkParents($links, $expected_hierarchy)
```

## Documentation

```text
Assert that at set of links is properly parented.
```

## Code

```php
  function assertMenuLinkParents($links, $expected_hierarchy) {
    foreach ($expected_hierarchy as $child => $parent) {
      $mlid = $links[$child]['mlid'];
      $plid = $parent ? $links[$parent]['mlid'] : 0;

      $menu_link = menu_link_load($mlid);
      menu_link_save($menu_link);
      $this->assertEqual($menu_link['plid'], $plid, format_string('Menu link %mlid has parent of %plid, expected %expected_plid.', array('%mlid' => $mlid, '%plid' => $menu_link['plid'], '%expected_plid' => $plid)));
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
