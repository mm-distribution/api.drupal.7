# MenuTestCase::verifyAccess()

- **Type:** Method
- **File:** [`modules/menu/menu.test`](../_file.md), lines 597–640 · [local source](../../../../../source/modules/menu/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test#L597-L640)
- **Class:** [MenuTestCase](../MenuTestCase.md)
- **Module/theme:** menu

## Signature

```php
private function verifyAccess($response = 200)
```

## Documentation

```text
Verify the logged in user has the desired access to the various menu nodes.

@param integer $response HTTP response code.
```

## Code

```php
  private function verifyAccess($response = 200) {
    // View menu help node.
    $this->drupalGet('admin/help/menu');
    $this->assertResponse($response);
    if ($response == 200) {
      $this->assertText(t('Menu'), 'Menu help was displayed');
    }

    // View menu build overview node.
    $this->drupalGet('admin/structure/menu');
    $this->assertResponse($response);
    if ($response == 200) {
      $this->assertText(t('Menus'), 'Menu build overview node was displayed');
    }

    // View navigation menu customization node.
    $this->drupalGet('admin/structure/menu/manage/navigation');
        $this->assertResponse($response);
    if ($response == 200) {
      $this->assertText(t('Navigation'), 'Navigation menu node was displayed');
    }

    // View menu edit node.
    $item = $this->getStandardMenuLink();
    $this->drupalGet('admin/structure/menu/item/' . $item['mlid'] . '/edit');
    $this->assertResponse($response);
    if ($response == 200) {
      $this->assertText(t('Edit menu item'), 'Menu edit node was displayed');
    }

    // View menu settings node.
    $this->drupalGet('admin/structure/menu/settings');
    $this->assertResponse($response);
    if ($response == 200) {
      $this->assertText(t('Menus'), 'Menu settings node was displayed');
    }

    // View add menu node.
    $this->drupalGet('admin/structure/menu/add');
    $this->assertResponse($response);
    if ($response == 200) {
      $this->assertText(t('Menus'), 'Add menu node was displayed');
    }
  }
```

---
_Drupal 7.103 · [modules/menu/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
