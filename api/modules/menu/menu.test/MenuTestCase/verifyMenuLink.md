# MenuTestCase::verifyMenuLink()

- **Type:** Method
- **File:** [`modules/menu/menu.test`](../_file.md), lines 381–406 · [local source](../../../../../source/modules/menu/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test#L381-L406)
- **Class:** [MenuTestCase](../MenuTestCase.md)
- **Module/theme:** menu

## Signature

```php
function verifyMenuLink($item, $item_node, $parent = NULL, $parent_node = NULL)
```

## Documentation

```text
Verify a menu link using the menu module UI.

@param array $item Menu link.
@param object $item_node Menu link content node.
@param array $parent Parent menu link.
@param object $parent_node Parent menu link content node.
```

## Code

```php
  function verifyMenuLink($item, $item_node, $parent = NULL, $parent_node = NULL) {
    // View home page.
    $this->drupalGet('');
    $this->assertResponse(200);

    // Verify parent menu link.
    if (isset($parent)) {
      // Verify menu link.
      $title = $parent['link_title'];
      $this->assertLink($title, 0, 'Parent menu link was displayed');

      // Verify menu link link.
      $this->clickLink($title);
      $title = $parent_node->title;
      $this->assertTitle(t("@title | Drupal", array('@title' => $title)), 'Parent menu link link target was correct');
    }

    // Verify menu link.
    $title = $item['link_title'];
    $this->assertLink($title, 0, 'Menu link was displayed');

    // Verify menu link link.
    $this->clickLink($title);
    $title = $item_node->title;
    $this->assertTitle(t("@title | Drupal", array('@title' => $title)), 'Menu link link target was correct');
  }
```

---
_Drupal 7.103 · [modules/menu/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
